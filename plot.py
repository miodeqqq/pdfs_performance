#! /usr/bin/env python

# -*- coding: utf-8 -*-

import plotly.graph_objs as go
import plotly.offline as opy

from utils import PLOTLY_COLORS


class StatisticPlot:
    def __init__(self, regex, pypdf2, pdfrw, pdfquery, tika, pdfminer, pymupdf):
        self.regex = self.__read(regex)
        self.pypdf2 = self.__read(pypdf2)
        self.pdfrw = self.__read(pdfrw)
        self.pdfquery = self.__read(pdfquery)
        self.tika = self.__read(tika)
        self.pdfminer = self.__read(pdfminer)
        self.pymupdf = self.__read(pymupdf)

    def __read(self, file_obj):
        """
        General method to return processing results as a dict obj.
        """

        with open(file_obj, 'r') as data_file:
            return dict([x.lower().strip().split(';') for x in data_file])

    def __make_layout(self, x_title, y_title):
        """
        Creates final layout with labels for XY axis.
        """

        return go.Layout(
            title='Python libraries performance with reading PDF and gathering info about the number of pages',
            xaxis=dict(
                title=x_title,
                autorange=True,
                titlefont=dict(
                    family='Verdana',
                    size=18,
                    color='#7f7f7f'
                )
            ),
            yaxis=dict(
                autorange=True,
                title=y_title,
                titlefont=dict(
                    family='Verdana',
                    size=18,
                    color='#7f7f7f'
                )
            ),
        )

    def generate_bar_plot(self):
        """
        General method to generate Bar plot.
        """

        # make Bar plots
        regex_data = go.Bar(
            x=list(self.regex.keys()),
            y=list(self.regex.values()),
            name='REGEX',
            textposition='auto'
        )

        pypdf2_data = go.Bar(
            x=list(self.pypdf2.keys()),
            y=list(self.pypdf2.values()),
            name='PYPDF2',
            textposition='auto'
        )

        pdfrw_data = go.Bar(
            x=list(self.pdfrw.keys()),
            y=list(self.pdfrw.values()),
            name='PDFRW',
            textposition='auto'
        )

        pdfquery_data = go.Bar(
            x=list(self.pdfquery.keys()),
            y=list(self.pdfquery.values()),
            name='PDFQUERY',
            textposition='auto'
        )

        tika_data = go.Bar(
            x=list(self.tika.keys()),
            y=list(self.tika.values()),
            name='TIKA',
            textposition='auto'
        )

        pdfminer_data = go.Bar(
            x=list(self.pdfminer.keys()),
            y=list(self.pdfminer.values()),
            name='PDFMINER',
            textposition='auto'
        )

        pymupdf_data = go.Bar(
            x=list(self.pymupdf.keys()),
            y=list(self.pymupdf.values()),
            name='PYMUPDF',
            textposition='auto'
        )

        data = [
            regex_data,
            pypdf2_data,
            pdfrw_data,
            pdfquery_data,
            tika_data,
            pdfminer_data,
            pymupdf_data
        ]

        layout = self.__make_layout(
            x_title='filename',
            y_title='processing time (seconds)'
        )

        fig = go.Figure(
            data=data,
            layout=layout
        )

        fig.update_layout(barmode='group')

        opy.plot(
            fig,
            filename='./plots/pdfs_performance_bar.html'
        )

    def generate_final_statistics_bar_plot(self, stats_dict):
        """
        General method to generate final statistics Bar plot.
        """

        final_time_stats = [(k, v) for k, v in stats_dict.items() if 'parsing_time' in k.lower()]

        d = {}

        for item in final_time_stats:
            d[item[0].split('_')[0]] = item[1]

        _x = list(d.keys())
        _y = list(d.values())

        final_data = go.Bar(
            x=list(_x),
            y=_y,
            name='Final statistics',
            textposition='auto',
            marker_color=PLOTLY_COLORS
        )

        data = [
            final_data,
        ]

        layout = self.__make_layout(
            x_title='Library',
            y_title='Overall processing time (seconds)'
        )

        fig = go.Figure(
            data=data,
            layout=layout
        )

        fig.update_layout(barmode='group')

        opy.plot(
            fig,
            filename='./plots/pdfs_performance_final_stats_bar.html'
        )
