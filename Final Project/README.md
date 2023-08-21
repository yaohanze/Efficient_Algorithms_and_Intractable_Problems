# project-fa19
CS 170 Fall 2019 Project
Team Member: Colin Kou, Lin Yang, Hanze Yao

In this project, besides the package used in the starter code: os, sys, argparse, random, math and 
numpy, our team only uses networkx

Our team uses the functions in utils.py and student_utils.py to parse the data from the input files and write the results from solver.py to output files. Then we use output_validator.py to validate all the outputs. After getting all the outputs, we use compress_output.py to compress the outputs into outputs.json. (input_output_generator.py is used for generating input and output files for Phase 1)

Instructions:
1. In the terminal, type in "python3 solver.py --all <inputs directory> <outputs directory>", and click Enter
to run the code
2. Then the all the inputs in the inputs directory will be passed into the solver and the generated outputs will be stored in the outputs directory
3. Type "python3 output_validator.py --all <inputs directory> <outputs directory>" in terminal to validate all the outputs
4. Type "python3 compress_output.py <outputs directory>" to compress all the outputs into a .json file.
