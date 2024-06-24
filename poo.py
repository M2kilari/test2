import os
import argparse


parser = argparse.ArgumentParser(description='IMDB model training')
parser.add_argument('--epochs', help='number of epochs to run', default='10')
args = parser.parse_args()    

epochs = int(args.epochs)
  
# Specify the directory and filename
directory = "output/"
filename = f"out_{epochs}.txt"

# Create the full path
file_path = os.path.join(directory, filename)

# Open the file and write to it
with open(file_path, "w") as file:
  file.write("Hello, world!\n")
      
print(f"File saved to: {file_path}")
