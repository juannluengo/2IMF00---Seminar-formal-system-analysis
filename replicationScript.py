import os
import shutil

# List of file paths
file_paths = [
    "/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/learning/full_data/smallFT1/example1.dot",
    "/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/learning/full_data/smallFT1/example2.dot",
    "/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/learning/full_data/smallFT1/example3.dot",
    "/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/learning/full_data/smallFT1/example4.dot",
    "/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/learning/full_data/smallFT1/example5.dot"
]

def replicate_files(file_paths, num_copies=15):
    for file_path in file_paths:
        # Extract the directory and base name of the file
        directory = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        
        # Replicate the file num_copies times
        for i in range(1, num_copies + 1):
            new_file_name = f"{name}_{i}{ext}"
            new_file_path = os.path.join(directory, new_file_name)
            shutil.copyfile(file_path, new_file_path)
            print(f"Created: {new_file_path}")

replicate_files(file_paths)
