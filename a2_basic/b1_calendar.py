#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: b1_calendar.py
@Time: 2019-09-04 15:57
@Last_update: 2019-09-04 15:57
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar


def calendar_base():
    begin = datetime.date(2017,1,1)
    end = datetime.date(2017,12,31)
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 20000)]
        for i in range((end - begin).days + 1)
    ]

    c = (
        Calendar()
        .add('', data, calendar_opts=opts.CalendarOpts(range_='2017'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Calendar-2017 Wechat path'),
            visualmap_opts=opts.VisualMapOpts(
                max_=20000,
                min_=500,
                orient='horizontal',
                is_piecewise=True,
                pos_top='230px',
                pos_left='100px',
            ),
            toolbox_opts=opts.ToolboxOpts()
        )
    )

    return c



c = calendar_base()
c.render('data/b1_calendar.html')