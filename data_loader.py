# data_loader.py

import mne
import h5py

def load_data(file_path):
    """
    Function to load neural time series data from a file.
    :param file_path: Path to the file containing the data.
    :return: Loaded data as an MNE Raw object.
    """
    # Load the data file
    with h5py.File(file_path, 'r') as f:
        data = f['data'][:]
        info = mne.create_info(ch_names=list(f['channel_names']), sfreq=f['sampling_rate'])

    # Create MNE Raw object
    raw = mne.io.RawArray(data, info)

    return raw
