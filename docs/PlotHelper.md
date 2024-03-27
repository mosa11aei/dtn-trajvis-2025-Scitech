# `PlotHelper` Class

This class is a helper class to not only generate the wind maps from a given initialized `WindMap`, but also plots the balloons on the wind map. This class is really only for debugging purposes.

## Initialization

```py
MyPlotHelper = PlotHelper(wm=MyWindMap) # only takes in an initialized wind map
```

## Methods

### PlotHelper.populate(show_scale)

*`show_scale` is an optional boolean*. Create a single matrix of vectors that will be plotted. On the plot, the scale of the vectors can be hidden to make the plot less crazy.

### PlotHelper.plot()

Plot the matrices of vectors on a matplotlib quiver plot.

### PlotHelper.plot_balloons(b_1, b_2, ...)

Plot the path of given balloons on the wind map.

### PlotHelper.zoom_in(x,y)

Zoom into a certain area, with (x,y) being the center of the area. Zoom area is dependent on the step size.

## PlotHelper Data

- `plt_x`: x-coordinates (at all steps)
- `plt_y`: y-coordinates (at all steps)
- `plt_vec_x`: x-coordinates of vectors at corresponding x-steps (relative to (0,0))
- `plt_vec_y`: y-coordinates of vectors at corresponding y-steps (relative to (0,0))