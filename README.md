In this folder you will find different files. 

Python:
The python file is a script that takes two electron density files and calculates the observable dielectric constant and plots the local dielectric profile. While this script is designed for the file format of QuantumATK, the first part where the file is opened and the data is sorted into arrays can simply be adjusted to fit any format. Just remember to also adjust the unit conversions accordingly. ATK provides the length in bohr and electron density in 1/bohr$^3$. 

Gaussian:
The text files in this folder is example input files for Gaussian16. There is a geometry optimization, volume calulation, static polarizability, dynamic polarizability and a file for the static polarizability calculated at a given field strength. If these files are to be run in Gaussian, remember to convert the file to .com files for execution. 
