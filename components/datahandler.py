import matplotlib.pyplot as plt

class DataHandler:
    network = None
    
    def __init__(self, network):
        self.network = network
        
    # NOTE: path1 is determined as the reconfigurable path if plotting meaningfuls    
    def plot_trp_comparison(self, path1, path2, path1_name="Generic", path2_name="Current", plot_meaningfuls=False, system=1):
        # generate a plot using matplotlib from reconfig_rp, generic_rp, and time 1-8000
        x_axis = range(1, 8000)
        print(len(self.network.reconfigures))

        reconfigures = []
        reconfigures_time = []

        for reconfig in self.network.reconfigures:
            reconfigures_time.append(reconfig["time"])
            reconfigures.append(path1[reconfig["time"]])

        fig, ax = plt.subplots()
        ax.plot(x_axis, path1, label="Reconfigurable Path")
        ax.plot(x_axis, path2, label="Generic Path")
        
        if plot_meaningfuls:
            ax.scatter(reconfigures_time, reconfigures, label="Meaningful", color="red")
        
        ax.legend()

        ax.set_xlabel("Time (s)")
        ax.set_ylabel("E2E Receiver Power (dBm)")
        ax.set_title(f"E2E Receiver Power Comparison (System #{system})")