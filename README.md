# Cochlear Transform Sound Signals
This repository contains a Python script for generating and visualizing cochlear transforms (ratemaps) from sound signals. The ratemap is simulated using a spectrogram, providing a visual representation of the auditory processing of sound signals.

## Features

- *Cochlear Transform*: Simulates cochlear transforms using spectrograms.
- *Support for Multiple Audio Formats*: Processes .m4a, .ogg, and .mp4 audio files.
- *Ratemap Generation*: Creates ratemaps with configurable parameters.
- *Logarithmic Scaling*: Applies logarithmic scaling for better numerical stability and visualization.
- *Visualization*: Plots and saves ratemaps as images.

## Code Overview

### Main Components

1. *Ratemap Generation*:
   - Uses the spectrogram function from scipy.signal to generate a ratemap from the audio signal.
   - Allows for logarithmic scaling of the ratemap for improved visualization.

2. *File Processing*:
   - Scans the current directory for audio files with supported extensions (.m4a, .ogg, .mp4).
   - Loads each audio file using librosa and processes it to generate and save the ratemap.

3. *Visualization*:
   - Uses matplotlib and librosa.display to plot the ratemap.
   - Saves the generated plots as images.

### Parameters

- *lowcf*: Lower cutoff frequency (Hz).
- *highcf*: Higher cutoff frequency (Hz, set to the sampling rate of the audio file).
- *nchans*: Number of channels for the ratemap.
- *winlen*: Window length for the spectrogram.
- *hoplen*: Hop length for the spectrogram.
- *scale*: Scaling mode for the ratemap ('log' for logarithmic scaling).

## How to Use

1. *Clone the Repository*:
   sh
   git clone https://github.com/abdulvahapmutlu/cochlear-transform-sound-signals.git
   cd cochlear-transform-sound-signals
   

2. *Prepare Your Audio Files*: Place your .m4a, .ogg, and .mp4 audio files in the repository directory.

3. *Install Dependencies*:
   sh
   pip install numpy matplotlib scipy librosa
   

4. *Run the Script*:
   sh
   python cochlear_transform.py
