# import subprocess
# import os

# def generate_prp(fuel_type, density, specific_heat):
#     # Prepare input file for FCEA2.exe if required
#     with open('input.txt', 'w') as f:
#         f.write(f"Fuel Type: {fuel_type}\n")
#         f.write(f"Density: {density}\n")
#         f.write(f"Specific Heat: {specific_heat}\n")
    
#     # Execute FCEA2.exe using subprocess and pass the input.txt file
#     try:
#         result = subprocess.run(['./FCEA2.exe', 'input.txt'], check=True, shell=True)
#         print("FCEA2 executed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error during execution: {e}")
#         return None

#     # Assuming FCEA2 generates a .prp file
#     prp_file = 'output.prp'
#     if os.path.exists(prp_file):
#         return prp_file
#     else:
#         print("No .prp file generated.")
#         return None


import subprocess
import os

def generate_prp(fuel_type, density, specific_heat):
    # Set the path for FCEA2.exe and the input/output files
    fcea_exe_path = './FCEA2.exe'  # Adjust the path if needed
    input_file = 'input.txt'
    prp_file = 'output.prp'
    
    # Prepare input file for FCEA2.exe in a format it expects
    with open(input_file, 'w') as f:
        f.write(f"prob rocket fac yes\n")
        f.write(f"fuel {fuel_type} wt%=100\n")
        f.write(f"ox O2(L) wt%=100\n")
        f.write(f"output short\n")
        f.write(f"end\n")
    
    # Execute FCEA2.exe using subprocess
    try:
        result = subprocess.run([fcea_exe_path, input_file], check=True, shell=True, capture_output=True, text=True)
        print(result.stdout)  # Output of the command
        print(result.stderr)  # Errors if any
        print("FCEA2 executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e.stderr}")
        return None

    # Check if .prp file is generated
    if os.path.exists(prp_file):
        return prp_file
    else:
        print("No .prp file generated.")
        return None

# Example usage
file = generate_prp("Jet_A", 800, 4.2)
if file:
    print(f".prp file generated: {file}")

# # Example use
# file = generate_prp("Jet A", 800, 4.2)
# if file:
#    print(f".prp file generated: {file}")
