import re
import numpy as np
import matplotlib.pyplot as plt


def getCynByAxis(redius = 1, heightStart = 0, heightEnd = 5, \
    offset = [0, 0, 0], devision = 20, mainAxis = 'z'):
    '''
return coordinates parallel to the axis;
offset: initlial position, also where heightStart starts;
mainAxis: which axis it parallels.
    '''

    mainAxis = mainAxis.lower()

    theta = np.linspace(0, 2*np.pi, devision)
    cx = redius * np.cos(theta) 
    cz = np.array([heightStart, heightEnd])
    cx, cz = np.meshgrid(cx, cz)
    cy = redius * np.sin(theta)

    if mainAxis == 'z':
        return offset[0] + cx, offset[1] + cy, offset[2] + cz
    elif mainAxis == 'y':
        return offset[0] + cx, offset[1] + cz, offset[2] + cy
    elif mainAxis == 'x':
        return offset[0] + cz, offset[1] + cy, offset[2] + cx
    else:
        raise ValueError("'x', 'y' or 'z' PLZ")
        

def getCynByCord(start = [0, 0, 0], end = [2, 2, 2], \
    radius = 1, division = 20):
    '''I would spent more time and more code if I did't see it... The core ideas is by @Amy Teegarden
    https://stackoverflow.com/questions/32317247/how-to-draw-a-cylinder-using-matplotlib-along-length-of-point-x1-y1-and-x2-y2#_=_
    It was awesome, guess I have a lot of math work to catch'''

    dirArray = np.array(end) - np.array(start)
    normDir = np.linalg.norm(dirArray)
    dirArray = dirArray / normDir #WTF the object and float
    unDirArray = np.array([1, 0, 0])
    if (dirArray == unDirArray).all():
        unDirArray = np.array([0, 1, 0])

    perpOne = np.cross(dirArray, unDirArray)
    perpOne /= np.linalg.norm(perpOne)
    perpTwo = np.cross(dirArray, perpOne)

    #that is amazing:
    t = np.linspace(0, normDir, 2)
    theta = np.linspace(0, 2 * np.pi, division)
    t, theta = np.meshgrid(t, theta)
    cx, cy, cz = [start[i] + dirArray[i] * t +\
        radius * np.sin(theta) * perpOne[i] +\
        radius * np.cos(theta) * perpTwo[i] \
        for i in [0, 1, 2]]
    
    return cx, cy, cz

def getCynByEqu(inStr, scale = 1, devision = 20,):
    ''' 
inStr: input equation, 3 forms recognizable
    x^2 + (y - 4)^2 = C
    x^{2}+z^{2}=C
    a*z^2 + bx^{2} = C 
scale: how large the plane is, by default -10 to 10
devision: devision of the cylinder
    ''' 
    try:
        findX = re.findall(r'\s*(\d*\.?\d*)\s*\*?\(?\s*[x|X]\s*\+?(\-?\s*\d*\.?\d*)?\s*\)?\s*\^\s*\{?(\d*\.?\d*)\}?', inStr)
        findY = re.findall(r'\s*(\d*\.?\d*)\s*\*?\(?\s*[y|Y]\s*\+?(\-?\s*\d*\.?\d*)?\s*\)?\s*\^\s*\{?(\d*\.?\d*)\}?', inStr)
        findZ = re.findall(r'\s*(\d*\.?\d*)\s*\*?\(?\s*[z|Z]\s*\+?(\-?\s*\d*\.?\d*)?\s*\)?\s*\^\s*\{?(\d*\.?\d*)\}?', inStr)
        findRedius = eval(re.findall(r'.*=\s*(\d*)\s*', inStr)[0])
        if re.match(r'.*\+.*', inStr): positive = True
        else: positive = False
    except: raise ValueError ('Unrecognized input equation!!!')


    coefficients = {}
    for i, k in zip([findX, findY, findZ], ['x', 'y', 'z']):
        if not i: axis = k
        else: 
            coefficients[k] = []
            for _ in i[0]: coefficients[k].append(eval(_) if _ else 1)
           
       
    redius = findRedius ** (1.0 / list(coefficients.values())[0][2])
    theta = np.linspace(0, 2*np.pi, devision)
    axisOne = redius * np.cos(theta)
    axisVer = np.linspace(-10 * scale, 10 * scale, devision)
    axisOne, axisVer = np.meshgrid(axisOne, axisVer)
    axisTwo = redius * np.sin(theta)

    if axis == 'x':
        X = axisVer
        Y = axisOne / coefficients['y'][0] - coefficients['y'][1]
        Z = axisTwo / coefficients['z'][0] - coefficients['z'][1]
    elif axis == 'y':
        Y = axisVer
        X = axisOne / coefficients['x'][0] - coefficients['x'][1]
        Z = axisTwo / coefficients['z'][0] - coefficients['z'][1]
    else:
        Z = axisVer
        Y = axisOne / coefficients['y'][0] - coefficients['y'][1]
        X = axisTwo / coefficients['x'][0] - coefficients['x'][1]

    return X, Y, Z


def getSphByAxis(radius = 1, offset = [0, 0, 0], devision = 20,\
    scale = [1, 1, 1]):
    '''easily get a sphere mesh
    offset: initial position, defalut [0, 0, 0]. 
    scale: scale, default [1, 1, 1]'''
    scale = [1 / scale[0], 1 / scale[1], 1 / scale[2]]

    theta = np.linspace(0, 2 * np.pi, devision)
    phi = np.linspace(0, np.pi, devision)
    x = offset[0] + radius * np.outer(np.cos(theta), np.sin(phi)) / scale[0]
    y = offset[1] + radius * np.outer(np.sin(theta), np.sin(phi)) / scale[1]
    z = offset[2] + radius * np.outer(np.ones(np.size(theta)), np.cos(phi)) / scale[2]

    return x, y, z


def getCubeByAxis(offset = [0, 0, 0], xlen = 1, ylen = 1, zlen = 1):
    '''offset: initial position;
    xlen/ylen/zlen: length of axis;
    Have to say, that's pretty idiot'''
    x = np.array([[offset[0], offset[0], offset[0] + xlen, offset[0] + xlen],
                   [offset[0], offset[0], offset[0] + xlen, offset[0] + xlen],
                   [offset[0], offset[0], offset[0] + xlen, offset[0] + xlen],
                   [offset[0], offset[0], offset[0] + xlen, offset[0] + xlen],
                   [offset[0], offset[0], offset[0] + xlen, offset[0] + xlen]])
    y = np.array([[offset[1], offset[1], offset[1], offset[1]],
                   [offset[1], offset[1], offset[1], offset[1]],
                   [offset[1] + ylen, offset[1] + ylen, offset[1] + ylen, offset[1] + ylen],
                   [offset[1] + ylen, offset[1] + ylen, offset[1] + ylen, offset[1] + ylen],
                   [offset[1], offset[1], offset[1], offset[1]]])
    z = np.array([[offset[2] + zlen, offset[2] + zlen, offset[2] + zlen, offset[2] + zlen],
                   [offset[2] + zlen, offset[2], offset[2], offset[2] + zlen],
                   [offset[2] + zlen, offset[2], offset[2], offset[2] + zlen],
                   [offset[2] + zlen, offset[2] + zlen, offset[2] + zlen, offset[2] + zlen],
                   [offset[2] + zlen, offset[2] + zlen, offset[2] + zlen, offset[2] + zlen]])
    return x, y, z

def getPlaneByEqu(inStr, scale = 1):
    ''' 
inStr: input equation, 3 forms recognizable
    A(x - x0) + B(y - y0) + C(z - z0) = 0 <<<Must equals 0
    Ax + By + Cz + D = 0 <<<Must equals 0
    x/a + y/b + z/c = d
scale: how large the plane is, by default -10 to 10
    ''' 

    X = np.linspace(-10 * scale, 10 * scale, 10)
    Y = np.linspace(-10 * scale, 10 * scale, 10)
    X,Y = np.meshgrid(X, Y)
    recognized = False
    indexVar = {'x': '[x|X]', 'y': '[y|Y]', 'z': '[z|Z]'}


    #=======Plane equation based on point Normal=======
    #===== A(x - x0) + B(y - y0) + C(z - z0) = 0  =====
    pointNormalCoe = []
    basePattern = r'(\-?\s*\d*\.*\d*)\s*\*?\s*\(?{}\s*\+?(\-?\s*\d*\.?\d*)\)?\s*[-|+|=]'
    for index in ['[x|X]', '[y|Y]', '[z|Z]']:
        try: pointNormalCoe.extend(re.findall(basePattern.format(index), inStr)[0])
        except: recognized = False
    try:
        coeName = ['A', 'x0', 'B', 'y0', 'C', 'z0']
        pointNormalCoe = dict((coeName[i], eval(pointNormalCoe[i])) for i in range(len(coeName)))   
        for i in ['x0', 'y0', 'z0']:
            pointNormalCoe[i] = -pointNormalCoe[i]
        if len(pointNormalCoe) == 6: recognized = True
        Z = (-pointNormalCoe['A']*X + pointNormalCoe['A']*pointNormalCoe['x0'] - 
         pointNormalCoe['B']*Y + pointNormalCoe['B']*pointNormalCoe['y0'] +
         pointNormalCoe['C']*pointNormalCoe['z0']) / pointNormalCoe['C']
    except: recognized = False


    #========Plane equation based on intercept========
    #========       Ax + By + Cz + D = 0      ========
    if not recognized:
        interceptPattern = r'\+?(\-?\s*\d*\.*\d*)\s*\*?\s*{}\s*\+?(\-?\s*\d*\.*\d*)\s*\*?\s*{}\s*\+?(\-?\s*\d*\.*\d*)\s*\*?\s*{}\s*\+?(\-?\s*\d*\.*\d*)\s*=\s*0'
        try:
            interceptCoe = list(re.findall(interceptPattern.format(indexVar['x'], indexVar['y'], indexVar['z']), inStr)[0])
            for i in range(len(interceptCoe)):
                if interceptCoe[i] in ['', ' ']: interceptCoe[i] = '1'
                elif interceptCoe[i] in ['-', '- ']: interceptCoe[i] = '-1'
                else: pass
            coeName = ['A', 'B', 'C', 'D']
            interceptCoe = dict((coeName[i], eval(interceptCoe[i])) for i in range(len(coeName))) 
            if len(interceptCoe) == 4: recognized = True
            Z = (-interceptCoe['A']*X - interceptCoe['B']*Y - interceptCoe['D']) / interceptCoe['C']
        except: recognized = False


    #=========Plane equation that is ordinary=========
    #===========    x/a + y/b + z/c = d     ==========
    if not recognized:
        devidedPattern = r'.*[x|X](\/?).*[y|Y](\/?).*[z|Z](\/?).*'
        ordinaryPattern = r'([+|-]?)\s*{}\s*\/?\s*\(?(\-?\s*\d*\.*\d*)\)?\s*([+|-])\s*{}\s*\/?\s*\(?(\-?\s*\d*\.*\d*)\)?'
        ordinaryPattern += r'\s*([+|-])\s*{}\s*\/?\s*\(?(\-?\s*\d*\.*\d*)\)?\s*=\s*\+?(\-?\s*\d*\.*\d*)'
        coeName = ['a_', 'a', 'b_', 'b', 'c_', 'c', 'd']
        try:
            ordinaryCoe = list(re.findall(ordinaryPattern.format(indexVar['x'], indexVar['y'], indexVar['z']), inStr)[0])
            devidedRe = re.findall(devidedPattern, inStr)[0] 
            for ind, dev in zip([1, 3, 5], devidedRe):
                if dev == '': ordinaryCoe[ind] = '1'
            if len(ordinaryCoe) == 7: recognized = True
            ordinaryCoe = dict((coeName[i], ordinaryCoe[i]) for i in range(len(coeName))) 
            ordinaryCoe = {'a': eval(ordinaryCoe['a_']+ordinaryCoe['a']),
                            'b': eval(ordinaryCoe['b_']+ordinaryCoe['b']),
                            'c': eval(ordinaryCoe['c_']+ordinaryCoe['c']),
                            'd': eval(ordinaryCoe['d'])}
            c = ordinaryCoe['c']
            Z = c*ordinaryCoe['d'] - c*X / ordinaryCoe['a'] - c*Y / ordinaryCoe['b']                
        except: recognized = False
        
    if not recognized:
        raise ValueError ('Unrecognized input equation!!!')
    return X, Y, Z


def getLineByEqu(inStr, scale = 1, forthPara = 't'):
    '''
Generate a stright line by formula
inStr: input equation, 3 forms recognizable
    x = x0 + ta; y = y0 + tb; z = z0 + tc
    (x0, y0, z0) + t(a, b, c)
    (x - x0)/a = (y - y0)/b = (z - z0)/c 
scale: how large the plane is, by default -10 to 10
forthPara: the 4th parameter besides x, y and z, literally useless
    '''

    t = np.linspace(-10*scale, 10*scale, 10)
    indexVar = ['[x|X]', '[y|Y]', '[z|Z]']
    recognized = False; paraCoe = []
    
    #=================Parametric Form=================
    basicPattern = r'{}\s*=\s*\+?(\-?\s*\d*\.*\d*)?\s*\+?(\-?\s*\d*\.*\d*)\s*\*?\s*' + forthPara
    cor = ['x0', 'a', 'y0', 'b', 'z0', 'c']
    for index in indexVar:
        try: paraCoe.extend(re.findall(basicPattern.format(index), inStr)[0])
        except: err = 'Not Parametric'
    if len(paraCoe) == 6: 
        for index in range(len(paraCoe)): 
            if re.fullmatch(r'\- *', paraCoe[index]): paraCoe[index] = '-1'
            elif re.fullmatch(r' *', paraCoe[index]): paraCoe[index] = '1'
        paraCoe = dict((cor[i], eval(paraCoe[i])) for i in range(len(paraCoe)))
        recognized = True

    #================Symmetric Form==================
    if not recognized:
        paraCoe = []; symPattern = r'\(?{}\s*\+?(\-?\s*\d*\.*\d*)\)?\/\(?\+?(\-?\s*\d*\.*\d*)\)?'
        try:
            for index in indexVar:
                paraCoe.extend(re.findall(symPattern.format(index), inStr)[0])
            for index in range(len(paraCoe)): 
                if re.fullmatch(r' *', paraCoe[index]): paraCoe[index] = '0'
            paraCoe = dict((cor[i], eval(paraCoe[i])) for i in range(len(paraCoe)))
            if len(paraCoe) == 6: recognized = True
        except: err += ', Symmetric'

    #==================Vector Form===================
    if not recognized:
        cor = ['x0', 'y0', 'z0', 'a', 'b', 'c']
        vectorPattern = r'\(\s*\+?(\-?\s*\d*\.*\d*)\s*[,|;]\s*\+?(\-?\s*\d*\.*\d*)\s*[,|;]\s*\+?(\-?\s*\d*\.*\d*)\)'
        try: 
            paraCoe = list(sum(re.findall(vectorPattern, inStr), ()))
            paraCoe = dict((cor[i], eval(paraCoe[i])) for i in range(len(paraCoe)))
            if len(paraCoe) == 6: recognized = True
        except: err += ' or Vector'

    if not recognized:
        raise ValueError ('Unrecognized input equation!!! {} form!!!'.format(err))

    X = paraCoe['x0'] + paraCoe['a']*t
    Y = paraCoe['y0'] + paraCoe['b']*t
    Z = paraCoe['z0'] + paraCoe['c']*t
    return X, Y, Z

def simpleLinearbyEqu2D(inStr, start = 0, end = 10, divd = 20):
    '''
Generate the x and y coordinate for a given linear formula. 
inStr:  input equation, multiple forms recognizable:
    y = 0.5x + 4
    3.7- 2/3x
    3.6 * x
start: where to start;
end: where to end;
sample: how many intervals are there;
    '''
    aPattern = re.compile(r"([-| ]*\d+\.?\d* */? *\d*)[ |\*]*([x|X])")
    bPattern = re.compile(r"([-| ]*\d+\.?\d* */? *\d*)[\+|-| ]?")
    
    a = re.findall(aPattern, inStr)
    b = re.findall(bPattern, inStr)
    a = [ i. replace(" ", "")for i in a[0]]
    
    if len(a) - 1: aValue = eval(a[0])
    else: aValue = 1

    if len(b):
        b = [i.replace(" ", "") for i in b]
        bValue = [eval(i) for i in b]
        bValue.remove(aValue)
        if len(bValue): bValue = bValue[0]
        else: bValue = 0
        
    sample = np.linspace(start, end, divd)
    return sample, aValue * sample + bValue


'''========================================='''
#==============================================
def simplePlot3D(*args):
    import mpl_toolkits.mplot3d 

    fig = plt.figure(figsize = (23, 20))
    ax = plt.axes(projection = '3d')
    x, y, z = getPlaneByEqu("12 * (x - 22) + 3*(y - 13.8) + 4.7*(z -30) = 0 ")
    ax.plot_surface(x, y, z, rstride = 1, cstride = 1, linewidth = 0, cmap='coolwarm')
    plt.show()
    return 0

def simplePlot2D():
    x, y = simpleLinearbyEqu2D("3.6 * x")
    #print(x, y)
    plt.plot(x, y)
    plt.show()




def main():
    
    simplePlot2D()

if __name__ == "__main__":
    main()


