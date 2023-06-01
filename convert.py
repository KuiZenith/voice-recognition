import os
import soundfile as sf
import numpy as np

def int16_pcm_to_float32(input_file, output_file):
  # Load the input WAV file
  data, samplerate = sf.read(input_file, always_2d=False)
  # Convert the data to 32-bit floating-point format
  converted_data = data.astype(np.float32) / np.iinfo(np.int16).max
  # Write the converted data to a new WAV file
  sf.write(output_file, converted_data[:, 0], 24000, format="WAV", subtype="FLOAT")
  print("Conversion completed successfully.")

# Example usage
for fn in os.listdir("./data/bark/human-1"):
  int16_pcm_to_float32(f"./data/bark/human-1/{fn}", f"./data/bark/human-1/{fn}")
# print(sf.available_subtypes("WAV"))
