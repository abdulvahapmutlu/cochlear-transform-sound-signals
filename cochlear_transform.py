import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram
import librosa
import librosa.display


# Function to generate ratemap (simulated with spectrogram)
def make_ratemap(audio, sr, lowcf, highcf, nchans, winlen, hoplen, scale):
    f, t, Sxx = spectrogram(audio, sr, nperseg=winlen, noverlap=winlen - hoplen, mode='magnitude')
    if scale == 'log':
        Sxx = np.log10(Sxx + 1e-10)  # Use log10 for better numerical stability
    return Sxx


# Get list of audio files with supported extensions
extensions = ['.m4a', '.ogg', '.mp4']
files = [f for f in os.listdir('.') if os.path.splitext(f)[1].lower() in extensions]

sayac = 1

for file in files:
    try:
        # Load the waveform
        audio, fs = librosa.load(file, sr=None, mono=True)

        # Set parameters for the ratemap
        lowcf = 50  # Hz
        highcf = fs  # Hz
        nchans = 128
        winlen = 1024
        hoplen = 512

        # Generate ratemap representation of the waveform
        ratemap = make_ratemap(audio, fs, lowcf, highcf, nchans, winlen, hoplen, scale='log')

        # Plot the ratemap
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(ratemap, sr=fs, x_axis='time', y_axis='log', cmap='inferno')
        plt.colorbar(format='%+2.0f dB')
        plt.title(f'Ratemap of {file}')
        plt.tight_layout()

        # Save the plot as an image
        output_filename = f"{os.path.splitext(file)[0]}_{sayac}.jpg"
        plt.savefig(output_filename)
        plt.close()

        sayac += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")