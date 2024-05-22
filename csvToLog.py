import pandas as pd
import os

def convert_to_traces(input_file_path, output_file_path):
    # Load the data from the CSV file
    data = pd.read_csv(input_file_path)
    
    # Identify the basic event columns and the target column
    columns = data.columns
    be_columns = [col for col in columns if col.startswith('BE')]
    target_column = columns[-1]  # Assuming the target column is the last one

    # Create a trace file in the required format
    with open(output_file_path, 'w') as file:
        for index, row in data.iterrows():
            # Create a trace string by concatenating the BE columns and the target column
            trace = ''.join([str(row[be_col]) for be_col in be_columns]) + str(row[target_column])
            file.write(f"{trace}\n")

    print(f"Trace file created at: {output_file_path}")

# Paths to your input and output files
base_dir = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/'

files = [
    'COVID_19.csv',
    'CSD.csv',
    'DDFT.csv',
    'GPT_12BE_10G.csv',
    'GPT_15BE_12G.csv',
    'MAX_MCS_FT.csv',
    'MPPS.csv',
    'PT.csv',
    'SMS.csv',
    'SYMLEARN.csv'
]

# Convert each CSV file to traces
for file in files:
    input_file_path = os.path.join(base_dir, file)
    output_file_path = os.path.join(base_dir, f"{os.path.splitext(file)[0]}_traces.trace")
    convert_to_traces(input_file_path, output_file_path)

