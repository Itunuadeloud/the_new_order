import subprocess
import os

def generate_prp(fuel_type, density, specific_heat):
    # Prepare input file for FCEA2.exe if required
    with open('input.txt', 'w') as f:
        f.write(f"Fuel Type: {fuel_type}\n")
        f.write(f"Density: {density}\n")
        f.write(f"Specific Heat: {specific_heat}\n")
    
    # Execute FCEA2.exe using subprocess and pass the input.txt file
    try:
        result = subprocess.run(['./FCEA2.exe', 'input.txt'], check=True, shell=True)
        print("FCEA2 executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")
        return None

    # Assuming FCEA2 generates a .prp file
    prp_file = 'output.prp'
    if os.path.exists(prp_file):
        return prp_file
    else:
        print("No .prp file generated.")
        return None

# Example use
file = generate_prp("Jet A", 800, 4.2)
if file:
    print(f".prp file generated: {file}")
