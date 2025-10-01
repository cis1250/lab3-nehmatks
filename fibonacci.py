#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True: 
  try: 
    terms = int(input("Enter the number of terms: "))
    if terms > 0:
      break 
    else: 
      print("Please enter a positive integer!")
  except: 
    print("Please enter a positive integer!")

a = 0 
b = 1 
for x in range(terms):
  print(a, end=" ")
  n_term = a + b
  a = b 
  b = n_term 
