# Numpy And Matplotlib Tools

I always neeed to plot something, like a 3d cylinder in matplotlib. Fairly speaking it's not difficult but may take some effort. Yet there's no built-in cylinder, and to calculate its cordinates is annoying.
  
So I came up with this, some small tools that you may use.



# Functions Index
  
## Matplotlib Tools:
    


### getPlaneByEqu()
Given an equation of a plane, generate that plane.  
supported equations:   
  
    A*(x - x0) + B*(y - y0) + C*(z - z0) = 0   
    A*x + B*y + C*z + D = 0   
    x/a + y/b + z/c = d  
    
Where characters like `A`, `a` and `x0` are numbers. The `*` is optional and `x`, `y`, `z` can be either lower letter or capital letter.  
For example:

    import matplotlib.pyplot as plt
    import mpl_toolkits.mplot3d 

    fig = plt.figure(figsize = (23, 20))
    ax = plt.axes(projection = '3d')
    x, y, z = getPlaneByEqu("12 * (x - 22) + 3*(y - 13.8) + 4.7*(z -30) = 0 ")
    ax.plot_surface(x, y, z, rstride = 1, cstride = 1, linewidth = 0, cmap='coolwarm')
    plt.show()

Will yield this:

<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/STDTLdemoPlotOne.png" width="400" height="400">


### getLineByEqu()   
Given an equation of a space line, generate that line.
Supported equations:

    x = x0 + t*a; y = y0 + t*b; z = z0 + t*c
    (x0, y0, z0) + t(a, b, c)
    (x - x0)/a = (y - y0)/b = (z - z0)/c 
    
Where characters like `A`, `a` and `x0` are numbers. The `*` is optional and `x`, `y`, `z` can be either lower letter or capital letter.
    
### getCynByEqu()
Given an equation of a cylinder, Generate a cylinder.
Supported equations:

    x^2 + (y - 4)^2 = C
    x^{2}+z^{2}=C
    a*z^2 + bx^{2} = C
    
Where characters like `a`, `b` and `C` are numbers. The `*` is optional and `x`, `y`, `z` can be either lower letter or capital letter.

### getCynByAxis()
Given parameters, generate a cylinder parallel to the axis.

### getCynByCord()
Given start and end point, with redius, generate a cylinder pointing the direction of the 2 points. 

### getSphByAxis()
Given initial position and redius, generate a sphere.

### getCubeByAxis()
Given the position of one corner point and length/height/width, generate a cube.

### simpleLinearbyEqu2D()
Generate the x and y coordinate for a given linear formula. 
Supported equations:

    y = 0.5x + 4
    3.7- 2x
    3.6 * x
    
For example:

    plt.style.use('ggplot')
    x, y = simpleLinearbyEqu2D("y = 2x - 3.6")
    #print(x, y)
    plt.plot(x, y)
    plt.show()

Would yield this: 

<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/STDTLdemoPlot2.png" width="400" height="400">


## Numpy Tools:

### regMatrix()
Given some strings in a form of a matrix, generate that matrix in the type of python list.  
e.g.  
input:
    
      '''  
      1 ,   34  , 4.6    
      5.03   4      7     
      '''  
      
Output:  
    
      [[1.0, 34.0, 4.6],   
       [5.03, 4.0, 7.0]]  

            
