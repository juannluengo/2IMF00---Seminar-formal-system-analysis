# Define the path to the trace file
# trace_file_path = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/PT_traces.trace' 
trace_file_path = '/Users/juanluengo/Desktop/Estudios/Universidades/4° Carrera/Quartile 4/Seminar formal system analysis/CSVinput/COVID_19_traces.trace' 

# Read and display the first few lines of the trace file
with open(trace_file_path, 'r') as file:
    lines = file.readlines()

# Display the first 10 lines of the file for inspection
for line in lines[:100]:
    print(line.strip())
