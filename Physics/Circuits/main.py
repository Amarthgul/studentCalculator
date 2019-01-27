def R(*args):
    '''Calculate Resistance given volt and ampere, return unit in Ohm
    '''
    units = ["a", "ma", "v"]
    backupList = []
    amp = 0; volt = 0
    for i in args:
        if isinstance(i, str):
            string = i.lower()
            for unit in units:
                pattern = re.compile(r"(\d+)( *)(" + unit + ")")
                result = re.findall(pattern, string)
                if len(result):
                    result = list(result[0])
                    #print("yes ", result)
                    if result[2] == 'ma': amp = float(result[0]) * 0.001
                    elif result[2] == 'a': amp = float(result[0])
                    elif result[2] == 'v': volt = float(result[0])
                    else: 
                        raise Exception("Unable to find value.")
        elif isinstance(i, float) or isinstance(i, int):
            backupList.append(i)

    if len(backupList) == 2:
        volt = backupList[0]; amp = backupList[1]

    return volt / amp
