import numpy as np
import librosa
import soundfile as sf
from scipy.signal import butter, sosfilt
import matplotlib.pyplot as plt

instrument_freq_ranges = {
    'violin': (196, 3520),        # G3 to A7
    'viola': (130, 1319),         # C3 to E6
    'cello': (65, 987),           # C2 to B5
    'double bass': (41, 294),     # E1 to D4
    'flute': (262, 2093),         # C4 to C7
    'oboe': (220, 1760),          # A3 to A6
    'clarinet': (98, 1760),       # G2 to A6
    'bassoon': (55, 698),         # A1 to F5
    'trumpet': (164, 988),        # E3 to B5
    'trombone': (82, 659),        # E2 to E5
    'french horn': (65, 880),     # C2 to A5
    'tuba': (41, 349),            # E1 to F4
    'piano': (27, 4186),          # A0 to C8
    'harp': (27, 4186),           # A0 to C8
    'timpani': (65, 262),         # C2 to C4
    'saxophone': (138, 1568),     # C#3 to G6
    'guitar': (82, 880),          # E2 to A5
    'voice': (85, 1100),          # Male and female vocal range
}

def butter_bandpass(lowcut, highcut, fs, order=5):
    sos = butter(order, [lowcut, highcut], btype='band', fs=fs, output='sos')
    return sos

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    sos = butter_bandpass(lowcut, highcut, fs, order=order)
    y = sosfilt(sos, data)
    return y

def main():
    # Ask the user for the instrument to extract
    print("Available instruments:")
    for instrument in instrument_freq_ranges.keys():
        print(f"- {instrument}")
    selected_instrument = input("Enter the instrument you want to extract: ").strip().lower()

    if selected_instrument not in instrument_freq_ranges:
        print(f"Instrument '{selected_instrument}' not recognized.")
        return

    # Get the frequency range for the selected instrument
    lowcut, highcut = instrument_freq_ranges[selected_instrument]
    print(f"Extracting '{selected_instrument}' with frequency range {lowcut} Hz to {highcut} Hz.")

    # Load the audio file
    input_file = 'multiple_instruments.mp3'  # Replace with your input file path
    output_file = f'{selected_instrument}_extracted.wav'  # Output file path

    # Load the audio data
    data, sample_rate = librosa.load(input_file, sr=None, mono=True)

    # Apply the band-pass filter
    filtered_data = bandpass_filter(data, lowcut, highcut, sample_rate, order=6)

    # Normalize the filtered data to prevent clipping
    max_val = np.max(np.abs(filtered_data))
    if max_val > 0:
        normalized_data = filtered_data / max_val
    else:
        normalized_data = filtered_data

    # Create subplots for original and filtered waveforms
    fig, axs = plt.subplots(2, 1, figsize=(14, 10))

    # Time axis for plotting
    time_axis = np.linspace(0, len(data) / sample_rate, num=len(data))

    # Plot the original waveform
    axs[0].plot(time_axis, data)
    axs[0].set_title('Original Audio Waveform')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Amplitude')

    # Plot the filtered waveform
    axs[1].plot(time_axis, normalized_data)
    axs[1].set_title(f'Filtered Audio Waveform - {selected_instrument.capitalize()}')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Amplitude')

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

    # Save the output audio file
    sf.write(output_file, normalized_data, sample_rate)

    print(f"Filtered audio saved to {output_file}")

if __name__ == '__main__':
    main()