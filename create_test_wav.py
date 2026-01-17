import numpy as np
import soundfile as sf

sr = 16000            # sample rate
t = np.linspace(0, 1, int(sr * 1.0), endpoint=False)  # 1 second
tone = 0.4 * np.sin(2 * np.pi * 220 * t)  # A low sine tone (220 Hz)

sf.write('test.wav', tone, sr)
print("Wrote test.wav (1s, 16kHz)")
