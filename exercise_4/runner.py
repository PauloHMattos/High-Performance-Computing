import platform
import subprocess
import os
import psutil

def cd(path, log = False):
    result = subprocess.run(['cd', path], stdout=subprocess.PIPE)
    if log:
        print(result.stdout.decode('utf-8'))
    
def compile(output, source, flags, log = False):
    args = ['g++']
    args.extend(flags)
    args.extend(source)
    args.append('-o')
    args.append(output)
    print(args)
    result = subprocess.run(args, stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))


def run_program(path, args):
    if platform.system() == 'Windows':
        path += '.exe'
    
    p = subprocess.Popen([path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    program = ' '.join(str(e) for e in args)
    out = p.communicate(program.encode())
    return out

def run(flags, output_file):
    nx_collections = [512, 1024, 2048]
    n_iter = 1000
    eps = 10E-16
    
    for nx in nx_collections:
        result = run_program('./outputs/laplace', [nx, n_iter, eps])
        result = ';'.join(e.decode() for e in result)
        line = "{};{};{}".format(flags, nx, result)
        print(line)
        output_file.write("{}\n".format(line))
        output_file.flush()


def main(src, flags_collection, fileName, max_threads):
    folder = 'outputs/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    output_path = '{}/{}.csv'.format(folder, fileName)
    with open(output_path, 'w', newline='') as f:
        f.write("# Flags; Nx; Result; Time(s); nThreads; \n")
        
        for flags in flags_collection:
            compile('outputs/laplace', src, flags, True)
            
            for i in range(1, max_threads + 1):
                os.environ['OMP_NUM_THREADS'] = str(i)
                run(flags, f)
            
        
        
if __name__ == "__main__":
    flags_collection = [['-fopenmp'], ['-fopenmp', '-O3']]
    main(['src/laplace_omp.cpp'], flags_collection, "table_omp", psutil.cpu_count(logical=False))
    main(['src/laplace.cpp'], [[], ['-O3']], "table", 1)