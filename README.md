# Signal Filtering and Frequency Analysis in Python

This project demonstrates how to generate a composite signal, apply digital filters, and analyze it in both time and frequency domains. It serves as a practical introduction to fundamental digital signal processing (DSP) techniques using Python.  
This task was prepared as part of laboratory classes in the basics of digital signal processing.

---

## Features

* Generation of a synthetic multi-frequency sine signal
* Implementation of low-pass, high-pass, and band-pass Butterworth filters
* Frequency-domain analysis using the Fast Fourier Transform (FFT)
* Time-domain comparison of filtered and original signals
* Spectrogram visualization for frequency evolution over time
* Clear and structured plots illustrating each stage of processing

---

## Overview of the Script

The script performs the following steps:

1. Generates a signal composed of three sine wave components (7 Hz, 10 Hz, and 20 Hz).
2. Designs and applies:

   * A low-pass filter
   * A high-pass filter
   * A band-pass filter
     using `scipy.signal.butter` and `scipy.signal.filtfilt`.
3. Computes FFT for the original and filtered signals.
4. Produces multiple visualizations:

   * Time-domain plots of all filtered signals
   * Individual plots for each filter type
   * A four-panel FFT comparison
   * A spectrogram of the original signal

---

## Technologies Used

* Python 3
* NumPy
* SciPy
* Matplotlib

---

## Project Structure

```
├── main.py        # Main script performing signal generation, filtering, and analysis
└── README.md      # Project documentation
```

---

## Installation and Usage

1. Install the required dependencies:

```
pip install -r requirements.txt
```

2. Run the script:

```
python main.py
```

All visualizations will be displayed automatically.

---

## Purpose

The purpose of this project is to illustrate core concepts from the laboratory classes in the basics of digital signal processing. It demonstrates how to generate a composite signal, apply digital filters, and examine the results in both time and frequency domains. The project provides a practical, hands-on introduction to essential DSP techniques using Python.

