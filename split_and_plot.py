import numpy as np
import librosa
import soundfile as sf
import scipy.signal as signal
import matplotlib.pyplot as plt
import librosa.display

def butter_bandpass(lowcut, highcut, fs, order=4):
    sos = signal.butter(order, [lowcut, highcut], btype='band', fs=fs, output='sos')
    return sos

def bandpass_filter(data, sos):
    y = signal.sosfiltfilt(sos, data)
    return y

def plot_waveforms(y, y_low, y_mid, y_high, sr):
    # Select a segment for plotting (e.g., first 10 seconds)
    duration = 10  # seconds
    samples = int(duration * sr)
    time = np.linspace(0, duration, samples)

    plt.figure(figsize=(12, 10))

    plt.subplot(4, 1, 1)
    librosa.display.waveshow(y[:samples], sr=sr)
    plt.title('Original Signal')
    plt.ylabel('Amplitude')

    plt.subplot(4, 1, 2)
    librosa.display.waveshow(y_low[:samples], sr=sr)
    plt.title('Low Frequencies')
    plt.ylabel('Amplitude')

    plt.subplot(4, 1, 3)
    librosa.display.waveshow(y_mid[:samples], sr=sr)
    plt.title('Mid Frequencies')
    plt.ylabel('Amplitude')

    plt.subplot(4, 1, 4)
    librosa.display.waveshow(y_high[:samples], sr=sr)
    plt.title('High Frequencies')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

def main():
    # Load the audio file
    audio_file = 'your_song.mp3'  # Replace with your audio file path
    y, sr = librosa.load(audio_file, sr=None, mono=True)
    print(f"Loaded '{audio_file}' with sample rate {sr} Hz.")

    # Define frequency bands (Hz)
    low_band = (20, 250)       # Low frequencies: 20 Hz to 250 Hz
    mid_band = (250, 4000)     # Mid frequencies: 250 Hz to 4 kHz
    high_band = (4000, 20000)  # High frequencies: 4 kHz to 20 kHz

    # Create band-pass filters
    sos_low = butter_bandpass(low_band[0], low_band[1], sr, order=4)
    sos_mid = butter_bandpass(mid_band[0], mid_band[1], sr, order=4)
    sos_high = butter_bandpass(high_band[0], high_band[1], sr, order=4)

    # Filter the signal
    print("Filtering low frequencies...")
    y_low = bandpass_filter(y, sos_low)
    print("Filtering mid frequencies...")
    y_mid = bandpass_filter(y, sos_mid)
    print("Filtering high frequencies...")
    y_high = bandpass_filter(y, sos_high)

    # Normalize the filtered signals to prevent clipping
    y_low /= np.max(np.abs(y_low)) + 1e-6  # Adding a small value to prevent division by zero
    y_mid /= np.max(np.abs(y_mid)) + 1e-6
    y_high /= np.max(np.abs(y_high)) + 1e-6

    # Plot the waveforms
    plot_waveforms(y, y_low, y_mid, y_high, sr)

    # Save the filtered signals
    print("Saving separated audio files...")
    sf.write('low_frequencies.wav', y_low, sr)
    sf.write('mid_frequencies.wav', y_mid, sr)
    sf.write('high_frequencies.wav', y_high, sr)

    print("Audio has been split into low, mid, and high frequencies.")
    print("Saved files:")
    print("- 'low_frequencies.wav'")
    print("- 'mid_frequencies.wav'")
    print("- 'high_frequencies.wav'")

if __name__ == '__main__':
    main()