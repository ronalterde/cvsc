#!/usr/bin/env python3

"""Tools for plotting 'Complexity over Commits'
"""

import os
import subprocess
from matplotlib import pyplot
import lizard


class LizardAnalyzer:
    def determine_ccn(file_path):
        return lizard.analyze_file(file_path).average_cyclomatic_complexity


class GitLog:
    def __init__(self, rootdir, filepath):
        self.rootdir = rootdir
        self.filepath = filepath

    def get_commit_count(self):
        commits = self._commit_string_to_list(self._get_commits_for_file())
        return len(commits)

    def _get_commits_for_file(self):
        return subprocess.check_output(
                ['git', 'log', '--format=%H', self.filepath], cwd=self.rootdir)

    def _commit_string_to_list(self, commits):
        list_of_commits = commits.decode('utf-8').split('\n')
        list_of_commits.pop()  # last element is empty after split()
        return list_of_commits


def collect_plot_data(root, file_list, analyzer):
    result = {'file': [], 'commit_count': [], 'ccn': []}
    for file_path in file_list:
        commit_count = GitLog(root, file_path).get_commit_count()
        ccn = analyzer.determine_ccn(os.path.join(root, file_path))
        print('File: {},\tCommits: {:d}\tCCN: {}'.format(file_path, commit_count, ccn))
        result['file'].append(file_path)
        result['commit_count'].append(commit_count)
        result['ccn'].append(ccn)
    return result


def create_plot(plot_data):
    pyplot.scatter(plot_data['commit_count'], plot_data['ccn'])
    pyplot.xlabel('commit count')
    pyplot.ylabel('avg ccn over all functions')
    for i, txt in enumerate(plot_data['file']):
        pyplot.annotate(
            txt,
            (plot_data['commit_count'][i], plot_data['ccn'][i]))
