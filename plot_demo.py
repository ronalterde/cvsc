#!/usr/bin/env python3

import cvsc
from matplotlib import pyplot

OUTPUT_FILE = 'cvsc-demo.png'

if __name__ == "__main__":
    file_list = ['demo.cpp',
                 'demo1.cpp',
                 'demo2.cpp']

    plot_data = cvsc.collect_plot_data('demo_project', file_list, cvsc.LizardAnalyzer)
    cvsc.create_plot(plot_data)
    pyplot.xlim(xmin=-1, xmax=10)
    print('Saving to ' + OUTPUT_FILE)
    pyplot.savefig(OUTPUT_FILE, dpi=90)
    pyplot.show()
