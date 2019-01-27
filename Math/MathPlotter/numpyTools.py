def regMatrix(inStr, align = False):
    '''return float type matrix, default return float
    inStr: input string
    align: control whether using None as completion
    '''
    import re
    from itertools import groupby

    regex = re.compile(r'\s*(\d+\.?\/?\d*)+(\n)?')
    find = re.findall(regex, inStr)

    find = [i for sub in find for i in sub if i != '']
    find = [list(g) for k, g in groupby(find, '\n'.__eq__) if not k]
    rowLength = []
    for index in range(len(find)):
        find[index] = [eval(i) for i in find[index]]
        rowLength.append(len(find[index]))

    if align:
        maxLength = max(rowLength)
        for index in range(len(find)):
            find[index].extend([None for i in range(maxLength - len(find[index]))])

    return find
