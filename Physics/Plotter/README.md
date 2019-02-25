
#dataPlot.py

Ploting data
`
    theta = np.arange(60, 30, -5)
    I_muA = np.array([327, 322, 317, 312, 308, 303])
    
    fig = dataPlot(theta, I_muA)
    fig.xLabel = r'$\theta /^{\circ}C$'; fig.yLabel = r'$I/\mu A$'
    fig.addGrid()
    fig.addScatterPoint()
    
    fig.addRegressLine(lineType = 'b-')
    fig.addLegend()
    fig.save()
    fig.showPlot()
`

<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/dataPlotClass.png" width="400" height="300">
