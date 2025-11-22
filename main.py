import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scipy_signal

duration = 5
sampling_freq = 1000
signal_freq1 = 7
signal_freq2 = 10
signal_freq3 = 20
amplitude1 = 3
amplitude2 = 3
amplitude3 = 3

t = np.arange(0, 1, 1/ sampling_freq)
signal = amplitude1 * np.sin(2 * np.pi * signal_freq1 * t)
signal += amplitude2 * np.sin(2 * np.pi * 2 * signal_freq2 * t)
signal += amplitude3 * np.sin(2 * np.pi * 3 * signal_freq3 * t)

lowcut = min(signal_freq1, signal_freq2, signal_freq3)
b, a = scipy_signal.butter(4, lowcut, btype='low', fs=sampling_freq)
low_passed_signal = scipy_signal.filtfilt(b, a, signal)

highcut = max(signal_freq1, signal_freq2, signal_freq3)
d, c = scipy_signal.butter(4, highcut , btype='high', fs=sampling_freq)
high_passed_signal = scipy_signal.filtfilt(d, c, signal)

bandcut_low = min(signal_freq1, signal_freq2, signal_freq3)
bandcut_high = max(signal_freq1, signal_freq2, signal_freq3)
b, a = scipy_signal.butter(4, [bandcut_low / (0.5 * sampling_freq), bandcut_high / (0.5 * sampling_freq)], btype='band')
band_passed_signal = scipy_signal.filtfilt(b, a, signal)

fft_original = np.fft.fft(signal)
fft_low_passed = np.fft.fft(low_passed_signal)
fft_high_passed = np.fft.fft(high_passed_signal)
fft_band_passed = np.fft.fft(band_passed_signal)

plt.plot(t, signal, label='Oryginalny sygnał')
plt.plot(t, low_passed_signal, label='Dolnoprzepustowy')
plt.title('Sygnał dolnoprzepustowy')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.legend()
plt.show()

plt.plot(t, signal, label='Oryginalny sygnał')
plt.plot(t, high_passed_signal, label='Górnoprzepustowy')
plt.title('Sygnał górnoprzepustowy')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.legend()
plt.show()

plt.plot(t, signal, label='Oryginalny sygnał')
plt.plot(t, band_passed_signal, label='Pasmowo przepustowy')
plt.title('Sygnał pasmowo przepustowy')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.legend()
plt.show()

plt.figure()
plt.plot(t, signal, label='Oryginalny sygnał')
plt.plot(t, low_passed_signal, label='Dolnoprzepustowy')
plt.plot(t, high_passed_signal, label='Górnoprzepustowy')
plt.plot(t, band_passed_signal, label='Pasmowo przepustowy')
plt.title('Sygnały')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.legend()
plt.show()

freqs = np.fft.fftfreq(len(signal), 1 / sampling_freq)

plt.figure()

plt.subplot(2, 2, 1)
plt.plot(freqs[:100], np.abs(fft_original)[:100], label='Oryginalny sygnał')
plt.title('FFT Oryginalny sygnał')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')

plt.subplot(2, 2, 2)
plt.plot(freqs[:100], np.abs(fft_low_passed)[:100], label='Dolnoprzepustowy')
plt.title('FFT Dolnoprzepustowy')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')

plt.subplot(2, 2, 3)
plt.plot(freqs[:100], np.abs(fft_high_passed)[:100], label='Górnoprzepustowy')
plt.title('FFT Górnoprzepustowy')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')

plt.subplot(2, 2, 4)
plt.plot(freqs[:100], np.abs(fft_band_passed)[:100], label='Pasmowo przepustowy')
plt.title('FFT Pasmowo przepustowy')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')

plt.tight_layout()
plt.show()

plt.specgram(signal, Fs=sampling_freq)
plt.title('Spektrogram sygnału oryginalnego')
plt.xlabel('Czas [s]')
plt.ylabel('Częstotliwość [Hz]')

plt.tight_layout()
plt.show()