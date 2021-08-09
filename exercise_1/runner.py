import platform
import subprocess

def run_program(path, n, order):
    if platform.system() == 'Windows':
        path += '.exe'
    
    result = subprocess.run([path, str(n), str(order)], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').lstrip()

def run(program, order):
    output_path = '{}/outputs/order_{}.csv'.format(program, order)
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
