# Exercise 2

## About
This folder houses the second exercise of the COC472 - High Performance Computing course of the Computer Engineering couse at Eng Poli - UFRJ.

## Requirements
To run the code you will need to compile it using any C++ compiler. In this exercise we were instructed to use the GCC compiler.
Since the objetice of the exercise is profiling the code, the flag -pg must be used.

```bash
# Compile the C++ code using the pg flag
$ g++ -pg src/laplace.cxx -o laplace

# Execute the laplace code
$ ./laplace

# Parameters specified in the assignement: 500 100 0.0000000000000001
Enter nx n_iter eps --> 500 100 0.0000000000000001

# The code execution will generate a gmon.out archive. Now execute gprof
$ gprof laplace gmon.out > output.txt
```

## Running
After installing the packages and building the code, run the `runner.py` to execute the binaries and generate the csv output with the n x runtime data. After that, run the `graph.py` to produce the graphs based on the aquired data.


## Results
A report was made as part of the assignment (in portuguese), and the result of the profiling before and after de optimizations is available in the folders "reports"
