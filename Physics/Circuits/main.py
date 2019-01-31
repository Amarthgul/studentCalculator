import re


def R(*args):
    '''Calculate Resistance given volt and ampere, return unit in Ohm.
    '''
    units = ["a", "ma", "amp", "v", "volt"]
    backupList = []
    amp = 0; volt = 0
    for i in args:
        if isinstance(i, str):
            string = i.lower()
            for unit in units:
                pattern = re.compile(r"(\d+\.?\d*)( *)(" + unit + ")")
                result = re.findall(pattern, string)
                if len(result):
                    result = list(result[0])
                    print("yes ", result)
                    if result[2] == 'ma': amp = float(result[0]) * 0.001
                    elif result[2] == ('a' or 'amph'): amp = float(result[0])
                    elif result[2] == ('v' or 'volt'): volt = float(result[0])
                    else: 
                        raise Exception("Unable to find value.")
        elif isinstance(i, float) or isinstance(i, int):
            backupList.append(i)

    if len(backupList) == 2:
        amp = backupList[0]; volt = backupList[1]

    return volt / amp

def I(*args):
    '''Calculate Current given volt and resistance, return unit in apmere.
    '''
    units = ["o", "ohm", "Ω", "v", "volt"]
    backupList = []
    amp = 0; volt = 0
    for i in args:
        if isinstance(i, str):
            string = i.lower()
            for unit in units:
                pattern = re.compile(r"(\d+\.?\d*)( *)(" + unit + ")")
                result = re.findall(pattern, string)
                if len(result):
                    result = list(result[0])
                    #print("yes ", result)
                    if result[2] == ('o' or 'ohm' or 'Ω'): 
                        ohm = float(result[0])
                    if result[2] == ('v' or 'volt'): volt = float(result[0])
                    elif result[2] not in units: 
                        raise Exception("Unable to find value.")
        elif isinstance(i, float) or isinstance(i, int):
            backupList.append(i)
    print(volt, ohm)
    if len(backupList) == 2:
        ohm = backupList[0]; volt = backupList[1]

    return volt / ohm;

def V(*args):
    '''Calculate Voltage given current and resistance, return unit in volt.
    '''
    units = ["o", "Ω", "a", "ma", "amp"]
    backupList = []
    amp = 0; volt = 0
    for i in args:
        if isinstance(i, str):
            string = i.lower()
            for unit in units:
                pattern = re.compile(r"(\d+\.?\d*)( *)(" + unit + ")")
                result = re.findall(pattern, string)
                if len(result):
                    result = list(result[0])
                    #print("yes ", result)
                    if result[2] == 'ma': amp = float(result[0]) * 0.001
                    if result[2] == ('a' or 'amph'): amp = float(result[0])
                    if result[2] == ('o' or 'Ω'): ohm = float(result[0])

                    elif result[2] not in units: 
                        raise Exception("Unable to find value.")
        elif isinstance(i, float) or isinstance(i, int):
            backupList.append(i)

    if len(backupList) == 2:
        amp = backupList[0]; ohm = backupList[1]

    return amp * ohm;


def P(*args):
    '''
Calculate electric power using any aviliable parameter. Resistive circuit only.    
    '''
    def extractNum(inStr):
        numStr = re.findall(r"(\d+\.?\d*|\d+)", inStr)[0]
        return float(numStr)
    
    patterns = {"volt": r"([U|u|V|v] *=* *\d+\.?\d*|\d+\.?\d* *[V|v|olt])",
                "amp": r"([I|i] *=* *\d+\.?\d*|\d+\.?\d* *[A|a])",
                "ohm": r"(R|r] *=* *\d+\.?\d*|\d+\.?\d* *[O|o|Ω])"};
    strs = {"volt": None, "amp": None, "ohm": None};
    values = {"volt": None, "amp": None, "ohm": None}
    
    for i in args:
        if isinstance(i, str):
            for para in patterns:
                strs[para] = re.findall(re.compile(patterns[para]), i)
                if len(strs[para]): values[para] = extractNum(strs[para][0])
            
    #print(values)
    if values["ohm"] == None: return values["volt"] * values["amp"];
    elif values["volt"] == None: return values["amp"] ** 2 * values["ohm"];
    else: return (values["volt"] ** 2) / values["ohm"]
