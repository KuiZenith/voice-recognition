import os
import soundfile as sf
import numpy as np

def convert(input_file, output_file):
  data, sample_rate = sf.read(input_file)
  sf.write(output_file, data[:, 0].astype(np.float32), 24000, format="WAV", subtype="FLOAT")
  print("Conversion completed successfully.")

directory = "./data/bark - human/human-2"

for fn in os.listdir(directory):
  convert(f"{directory}/{fn}", f"{directory}/{fn}")
