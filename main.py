import computation
import plotter
import Tkinter


delta = 0.22222  # our step
limit = 4  # rightmost interval border
IVPx = 1  # X of IVP
IVPy = 1  # Y of IVP

one, two, thre, four, five, six, seven, eight = computation.compute(delta, IVPx, IVPy, limit)
plotter.plot_graphs(one, two, thre, four, five, six, seven, eight)
plotter.plot_max_error_graph(10, 4, 1, 1)


