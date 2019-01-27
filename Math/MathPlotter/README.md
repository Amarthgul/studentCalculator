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

            
