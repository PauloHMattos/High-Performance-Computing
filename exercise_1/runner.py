import platform
import subprocess
import os

def run_program(path, n, order):
    if platform.system() == 'Windows':
        path += '.exe'
    
    result = subprocess.run([path, str(n), str(order)], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').lstrip()

def run(program, order):
    folder = '{}/outputs/'.format(program)
    if not os.path.exists(folder):
        os.mkdir(folder)

    output_path = '{}/order_{}.csv'.format(folder, order)
    with open(output_path, 'w', newline='') as f:
        f.write("# Number; Time(s)\n")
        for n in range(0, 28000, 1000):
            result = run_program('./{}/bin/product'.format(program), n, order)
            print(result)
            f.write(result)
            f.flush()

if __name__ == "__main__":
    run('c_source', 0)
    run('c_source', 1)
    run('fortran_source', 0)
    run('fortran_source', 1)
