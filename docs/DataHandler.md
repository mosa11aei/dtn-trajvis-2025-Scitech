# `DataHandler` Class

This class helps with simple data visualizations and plotting of information that comes from the simulator. The following is an example of one of the plots that can be generated:

![](/docs/imgs/example-dv.png)

## Initialization

```py
MyDataHandler = DataHandler(network=Network()) # your instance of the network class
```

## Utilization

### DataHandler.plot_trp_comparison(path1=[], path2=[], path1_name="Reconfigurable Path", path2_name="Generic Path", plot_meaningfuls=True, system="1")

Plot a plot like the example at the top of this file. "trp_comparison" stands for "total receiver power comparison", which can compare the E2E receiver powers of different path algorithms. The generic use-case is for a generic, unchanging path and a reconfigurable path.

