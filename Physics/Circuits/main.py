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
