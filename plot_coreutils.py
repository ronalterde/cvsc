#!/usr/bin/env python3

import os
import cvsc
from matplotlib import pyplot

SRC_DIR = './coreutils/src'
OUTPUT_FILE = 'cvsc-coreutils.png'


def remove_common_prefix(path, common):
    prefix = os.path.commonprefix([path, common])
    return path[len(prefix)+1:]


def get_all_source_files(src_dir):
    source_files = []
    for root, dirs, files in os.walk(src_dir):
        for name in files:
            if name.endswith('.c'):
                filepath_rel = remove_common_prefix(
                        os.path.join(root, name), src_dir)
                source_files.append(filepath_rel)
    return source_files


if __name__ == "__main__":
    file_list = get_all_source_files(SRC_DIR)
    print('Collecting plot data (this may take a while)...')
    plot_data = cvsc.collect_plot_data(SRC_DIR,
                                       file_list, cvsc.LizardAnalyzer)
    cvsc.create_plot(plot_data)
    print('Saving to ' + OUTPUT_FILE)
    pyplot.savefig(OUTPUT_FILE, dpi=90)
