import numpy as np
import wave

# Define parameters
sample_rate = 44100  # 44.1 kHz standard sample rate
duration = 2.0  # 2 seconds
freq = 440.0  # Frequency in Hz (A4 note)

# Generate time points
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Create a sine wave
waveform = (np.sin(2 * np.pi * freq * t) * 32767).astype(np.int16)

# Save to a .wav file
output_file = "sample.wav"
with wave.open(output_file, "w") as wav_file:
    wav_file.setnchannels(1)  # Mono audio
    wav_file.setsampwidth(2)  # 16-bit PCM
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(waveform.tobytes())

print(f"✅ Generated '{output_file}' successfully!")
