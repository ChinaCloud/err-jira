# coding: utf-8

import pygal
from pandas import Series, DataFrame


def render_horizontalstackedbar(frame:DataFrame, title:str, render_type:str='str', *args, **kwargs):
    bar_chart = pygal.HorizontalStackedBar()
    bar_chart.title = title
    bar_chart.x_labels = frame.index.tolist()

    for col in frame:
        bar_chart.add(col, frame[col].tolist())

    return {
        'str': bar_chart.render,
        'tree': bar_chart.render_tree,
        'table': bar_chart.render_table,
        'pyquery': bar_chart.render_pyquery,
        'data_uri':bar_chart.render_data_uri,
        'png': bar_chart.render_to_png,
        'file': bar_chart.render_to_file,
    }[render_type](*args, **kwargs)