In this folder you will find different files. 

Python:
* The python script processes two electron density files to compute the observable dielectric constant and plots the local dielectric profile. 
* While the script is tailored for QuantumATK file formats, the input section can be easily modified to support other formats. Just be sure to adjust the unit conversions accordingly. 
* In QuantumATK, lengths are given in bohr and electron densities in 1/bohr^3. 

Gaussian:
* The .txt files are example input files for Gaussian16, covering:
 * Geometry optimization
 * Volume calculation
 * Static polarizability
 * Dynamic polarizability
 * Static polarizability under an applied field
* If you plan to run these in Gaussian, make sure to convert the files from .txt to .com format.
