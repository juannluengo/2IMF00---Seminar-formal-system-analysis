import pandas as pd

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

# Example usage
# Paths to your input and output files
csd_input_file_path = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/CSD.csv'  # Update this path to the correct location of your CSD.csv file
csd_output_file_path = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/CSD_traces.trace'  # Update this path to the desired output location for CSD

pt_input_file_path = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/PT.csv'  # Update this path to the correct location of your PT.csv file
pt_output_file_path = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/PT_traces.trace'  # Update this path to the desired output location for PT

gpt_input_file_path = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/GPT_12BE_10G.csv'  # Update this path to the correct location of your GPT_12BE_10G.csv file
gpt_output_file_path = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/GPT_traces.trace'  # Update this path to the desired output location for GPT

# Convert the CSD data to traces
convert_to_traces(csd_input_file_path, csd_output_file_path)

# Convert the PT data to traces
convert_to_traces(pt_input_file_path, pt_output_file_path)

# Convert the GPT data to traces
convert_to_traces(gpt_input_file_path, gpt_output_file_path)
