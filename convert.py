import os
import soundfile as sf
import numpy as np

def convert(input_file, output_file):
  data, samplerate = sf.read(input_file)
  sf.write(output_file, data[:, 0], samplerate, subtype="FLOAT")
  print("Conversion completed successfully.")

directory = "./data/bark - human/human-1"

for fn in os.listdir(directory):
  convert(f"{directory}/{fn}", f"{directory}/{fn}")
