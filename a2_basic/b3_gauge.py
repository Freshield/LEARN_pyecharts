#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: b3_gauge.py
@Time: 2019-08-09 16:53
@Last_update: 2019-08-09 16:53
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from pyecharts import options as opts
from pyecharts.charts import Gauge


def gauge_base():
    c = (
        Gauge()
        .add('', [('完成率', 66.6)])
        .set_global_opts(title_opts=opts.TitleOpts(title='Gauge-base'),
                         legend_opts=opts.LegendOpts(is_show=False))
    )

    return c

# c = gauge_base()
# c.render('data/b3_gauge.html')


def gauge_color():
    c = (
        Gauge()
        .add('指标', [('完成率', 55.5)],
             axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(
                     color=[(0.3, '#67e0e3'), (0.7, '#37a2da'), (1, '#fd666d')], width=30
                 )
             ))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Gauge-diff color'),
            legend_opts=opts.LegendOpts(is_show=False)
        )
    )

    return c

# c = gauge_color()
# c.render('data/b3_gauge_diff_color.html')


def gauge_splitnum_label():
    c = (
        Gauge()
        .add('指标', [('完成率',55.5)], split_number=5,
             axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(
                     color=[(0.3, '#67e0e3'), (0.7, '#37a2da'), (1, '#fd666d')], width=30
                 )
             ),
             label_opts=opts.LabelOpts(formatter='{value}'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Gauge-splitnum'),
            legend_opts=opts.LegendOpts(is_show=False)
        )
    )

    return c


c = gauge_splitnum_label()
c.render('data/b3_gauge_splitnum.html')