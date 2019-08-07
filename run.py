#! /usr/bin/env python

# -*- coding: utf-8 -*-

import os
import sys

from main import LibrariesTesting, StatisticPlot


def run():
    """
    Retrieve the number of pages for each PDF and generate plots.
    """

    lib_test = LibrariesTesting(
        path=sys.argv[1]
    )

    lib_test.run()

    while not lib_test.is_ready:
        continue
    else:
        s = StatisticPlot(
            regex=os.path.join('pdfs_processing_time/regex.txt'),
            pypdf2=os.path.join('pdfs_processing_time/pypdf2.txt'),
            pdfrw=os.path.join('pdfs_processing_time/pdfrw.txt'),
            pdfquery=os.path.join('pdfs_processing_time/pdfquery.txt'),
            tika=os.path.join('pdfs_processing_time/tika.txt'),
            pdfminer=os.path.join('pdfs_processing_time/pdfminer.txt'),
            pymupdf=os.path.join('pdfs_processing_time/pymupdf.txt')
        )

        s.generate_bar_plot()

        s.generate_final_statistics_bar_plot(stats_dict=lib_test.final_stats_dict)


if __name__ == '__main__':
    run()
