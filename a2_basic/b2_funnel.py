#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: b2_funnel.py
@Time: 2019-09-04 16:12
@Last_update: 2019-09-04 16:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Funnel, Page


def funnel_base():
    data = [z for z in zip(Faker.choose(), Faker.values())]
    print(data)
    c = (
        Funnel()
        .add('Items', data)
        .set_global_opts(title_opts=opts.TitleOpts(title='Funnel-base'))
    )

    return c

# c = funnel_base()
# c.render('data/b2_funnel.html')

def funnel_label_inside():
    data = [z for z in zip(Faker.choose(), Faker.values())]
    c = (
        Funnel()
        .add('Items', data, label_opts=opts.LabelOpts(position='inside'))
        .set_global_opts(title_opts=opts.TitleOpts(title='Funnel-Label (insider)'))
    )

    return c

# c = funnel_label_inside()
# c.render('data/b2_funnel_label_inside.html')

def funnel_sort_ascending():
    data = [z for z in zip(Faker.choose(), Faker.values())]
    c = (
        Funnel()
        .add('Items', data, sort_='ascending', label_opts=opts.LabelOpts(position='inside'))
        .set_global_opts(title_opts=opts.TitleOpts(title='Funnel-Sort (ascending)'))
    )

    return c

c = funnel_sort_ascending()
c.render('data/b2_funnel_sort_ascending.html')