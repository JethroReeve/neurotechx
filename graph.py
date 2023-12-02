# graph.py

import matplotlib.pyplot as plt
from data_loader import load_data
from mne_analysis import perform_analysis

def live_graph(file_path):
    """
    Function to load data, perform MNE analysis and plot the results live.
    :param file_path: Path to the file containing the data.
    """
    # Load the data
    raw = load_data(file_path)

    # Perform MNE analysis
    f, psd = perform_analysis(raw)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the initial data
    line, = ax.semilogy(f, psd.T)

    # Set the title and labels
    ax.set_title('Live Power Spectral Density (PSD)')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Power Spectral Density')

    # Function to update the graph
    def update_graph():
        # Perform MNE analysis
        f, psd = perform_analysis(raw)

        # Update the data
        line.set_ydata(psd.T)

        # Redraw the figure
        fig.canvas.draw()

    # Set the update function to be called periodically
    plt.ion()
    plt.show()

    while True:
        update_graph()
        plt.pause(0.1)

if __name__ == "__main__":
    live_graph('path_to_your_file')
