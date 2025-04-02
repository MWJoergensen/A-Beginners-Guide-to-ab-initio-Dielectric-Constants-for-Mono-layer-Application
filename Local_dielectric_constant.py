# This script reads the output from QuantumATK
import numpy as np
import matplotlib.pyplot as plt
#=================================================================================================

# Input z-coordinates of the first and last atom in the molecule in the z-direction in angstrom
a = first_coordinate
b = last_coordinate

# Opening text file and appending data to lists which are converted to arrays
z1_coords = []
p1_coords = []
z2_coords = []
p2_coords = []

with open('text_file_of_negative_bias', 'r') as file1:
    # Initialize a line counter
    line_count = 0    
    for line in file1:
        # Increment the line counter
        line_count += 1
        if line_count <= 5:
            # Skip the first 5 lines
            continue
        if not line.strip():
            # If an empty line is encountered, break out of the loop
            break
        # Split the line by comma
        columns = line.strip().split(',') 
        # Extract x coordinate and append to array as length in z
        z1_coords.append(float(columns[0].strip()))
        # Extract y coordinate and append to array as charge densities p
        p1_coords.append(float(columns[1].strip()))
#print('p1 coords', p1_coords)

with open('text_file_of_positive_bias', 'r') as file2:
    # Initialize a line counter
    line_count = 0    
    for line in file2:
        # Increment the line counter
        line_count += 1
        if line_count <= 5:
            # Skip the first 5 lines
            continue
        if not line.strip():
            # If an empty line is encountered, break out of the loop
            break
        # Split the line by comma
        columns = line.strip().split(',') 
        # Extract x coordinate and append to array as length in z
        z2_coords.append(float(columns[0].strip()))
        # Extract y coordinate and append to array as charge densities p
        p2_coords.append(float(columns[1].strip()))
#print(p2_coords)

# Changing lists into arrays
z1 = np.array(z1_coords)
z2 = np.array(z2_coords)
p1 = np.array(p1_coords)
p2 = np.array(p2_coords)

#=================================================================================================

# Taking the difference in charge density in the z direction
pz= np.subtract(p1, p2)

# Relating the change in charge densities to the induced polarization by d/dz P(z) = -p_ind(z)
dz = np.diff(z1)

# Pad the first difference with the same value as the second difference for consistency
dz = np.insert(dz, 0, dz[0])

# Calculate the polarization P using numerical integration (trapezoidal rule)
Pz = np.cumsum(-pz * dz)

#=================================================================================================

# Converting things to meaningful units
bohr2ang = 0.529177
echarge = -1.60217663*10**(-19) #C
bohr2meter = 5.2918*10**(-11) 

# Converting polarization to C/m^2  
Pz_coulomb = Pz*((1.0/(bohr2meter)**2))*echarge

# Converting the length bohr to angstrom for z_position-coordinetes
z_ang = bohr2ang*z1

#=================================================================================================

# Finding the local dielectric constant from n(z) = (vacc Eext) / (vacc Eext - P(z))
# Remember to change field if different field strength is applied
eps0 = 8.854*10**(-12) #C/Vm
Efield = 5.14*10**8 #V/m

nz = 2.0*eps0*Efield/ (2.0*eps0*Efield - Pz_coulomb)

#================================================================================================

# Calculating the observerbal dielectric constant (Average DC)

# Find the indices of the closest values to a and b in the array
index_a = np.abs(z_ang - a).argmin()
index_b = np.abs(z_ang - b).argmin()

# Trimming the arrays for vacuum (anything before and after the molecule)
# Slice both arrays using the same indices
sliced_z = z_ang[index_a:index_b + 1]
sliced_n = nz[index_a:index_b + 1]
sliced_P = Pz_coulomb[index_a:index_b + 1]

# Counting indices between a and b
length_z = len(sliced_z)

# Using harmonic mean
inverse_sum_nz = sum(1/sliced_n)

DC = length_z/inverse_sum_nz

print('Average dielectric constant:', DC)

#==================================== Visualizing ===================================================
plt.subplot(1, 3, 1)
plt.plot(z_ang, pz)
plt.ylabel('change in density [$e/ang^3$]')
plt.xlabel('Z-axis position [Å]')


plt.subplot(1, 3, 2)
plt.plot(z_ang, Pz_coulomb)
plt.ylabel('polarization [$C/m^2$]')
plt.xlabel('Z-axis position [Å]')


plt.subplot(1, 3, 3)
plt.plot(z_ang, nz)
plt.xlabel('Z-axis position [Å]', fontsize=14)
plt.ylabel(r'$\eta$(z)', fontsize=14)

plt.rcParams["figure.figsize"] = (8,3) # width/height in inches
plt.tight_layout()
plt.show()