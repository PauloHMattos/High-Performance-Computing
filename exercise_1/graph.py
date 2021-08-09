import matplotlib.pyplot as plt
import csv
import sys
import os
import glob

def read_csv(path: str) -> tuple:
    x = []
    y = []
    legend = path.split(os.sep)[-1].replace('.csv', '')
    with open(path, 'r') as csv_file:
        dataset = csv.reader(csv_file, delimiter=';')
        next(dataset)
        for line in dataset:
            n, time = line
            x.append(int(n.strip()))
            y.append(float(time.strip()))

    return x, y, legend


def plot_scatter(data_path: str, save_path: str, title: str) -> None:
    data = []
    for f in glob.glob(f'{data_path}{os.sep}*.csv'):
        data.append(read_csv(f))

    legend = []
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.set_ylabel('Runtime (s)')
    ax.set_xlabel('N')

    ax.set_title(title)

    for x, y, archive_name in data:
        ax.plot(x, y)
        legend.append(archive_name)
    
    ax.legend(legend)
    fig.savefig(save_path)
    print(f'Graph generated: {title}')


if __name__ == '__main__':
    plot_scatter('c_source/outputs', 'c_source/outputs/graph', 'Graph for C')
    plot_scatter('fortran_source/outputs', 'fortran_source/outputs/graph', 'Graph for Fortran')