#!/usr/bin/env python3
# calc_number_amino_acids.py

"""
Calculates the number of amino acids in the resulting protein and its molecular weight
"""
import sys

# Get gene name as input
GN = input("Please enter a name for the DNA sequence: ")
print("Your sequence name is " + GN)

# Sequence length
SL = input("Please enter the length of the sequence: ")

if int(SL) % 3 != 0:
    sys.exit("Error: the DNA sequence is not a multiple of 3")

# Sequence length divided by 3
SL3 = int(SL) / 3

# Molecular weight
MW = SL3 * 0.11

# Print output
print("The length of the DNA sequence is: " + str(SL))
print("The length of the decoded protein is: " + str(SL3))
print("The average weight of the protein sequence is: " + str(MW))
