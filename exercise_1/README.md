# Exercise 1

## About
This folder houses the first exercise of the COC472 - High Performance Computing course of the Computer Engineering couse at Eng Poli - UFRJ.

## Requirements
### Binaries
The binaries require a suitable compiler and can be built using CMake. In my test's were used GCC and gFortran from MinGW. 

### Python scripts
The auxiliary python scripts require Matplotlib package. To install it open the folder and run

```bash
$ pip install -r requirements.txt
```

## Running
After installing the packages and building the code, run the `runner.py` to execute the binaries and generate the csv output with the n x runtime data. After that, run the `graph.py` to produce the graphs based on the aquired data.