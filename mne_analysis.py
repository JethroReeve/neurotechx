# mne_analysis.py

import mne
import numpy as np
from matplotlib import pyplot as plt

def perform_analysis(raw):
    """
    Function to perform MNE analysis on the raw data.
    :param raw: MNE Raw object containing the data.
    :return: Frequencies and power spectral density values.
    """
    # Apply band-pass filter
    raw.filter(1., 40., fir_design='firwin')

    # Pick MEG channels
    picks = mne.pick_types(raw.info, meg=True, eeg=False, stim=False, eog=False,
                           exclude='bads')

    # Calculate power spectral density
    f, psd = mne.time_frequency.psd_multitaper(raw, low_bias=True, tmin=0.0, tmax=10.0, fmin=0.0, fmax=50.0, proj=True, picks=picks, n_jobs=1)

    return f, psd

def plot_psd(f, psd):
    """
    Function to plot the power spectral density.
    :param f: Frequencies.
    :param psd: Power spectral density values.
    """
    plt.figure()
    plt.semilogy(f, psd.T)
    plt.title('Power Spectral Density (PSD)')
    plt.xlabel('Frequency')
    plt.ylabel('Power Spectral Density')
    plt.show()
