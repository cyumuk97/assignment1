#!/usr/bin/env python3
# dynamic_protocol.py

"""
Instructs user how to prepare a solution of certain volume with given stock solutions
"""

# Final volume
FV = input("Please enter the final volume of the solution (ml): ")

# NaCl stock
NCS = input("Please enter the NaCl stock (mM): ")

# NaCl final
NCF = input("Please enter the NaCl final (mM): ")

# MgCl2 stock
MC2S = input("Please enter the MgCl2 stock (mM): ")

# MgCl2 final
MC2F = input("Please enter the MgCl2 final (mM): ")

# Step 1
S1 = int(FV) * (int(NCF) / int(NCS))

# Step 2
S2 = int(FV) * (float(MC2F) / int(MC2S))

# Step 3
S3 = float(FV)
print("Add " + str(S1) + " ml NaCl.")
print("Add " + str(S2) + " ml MgCl2.")
print("Add water to a final volume of " + str(S3) + " ml, and mix.")
