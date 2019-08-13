import json
import os

from pyecharts import options as opts
from pyecharts.charts import Graph

def graph_base():
    nodes = [
        {"name": "结点1", "symbolSize": 10},
        {"name": "结点2", "symbolSize": 20},
        {"name": "结点3", "symbolSize": 30},
        {"name": "结点4", "symbolSize": 40},
        {"name": "结点5", "symbolSize": 50},
        {"name": "结点6", "symbolSize": 40},
        {"name": "结点7", "symbolSize": 30},
        {"name": "结点8", "symbolSize": 20},
    ]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({'source':i.get('name'),
                          'target':j.get('name')})

    c = (
        Graph()
        .add('', nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title='Graph-base'))
    )

    return c


# c = graph_base()
# c.render('data/b4_graph_base.html')

def graph_with_opts():
    nodes = [
        opts.GraphNode(name="结点1", symbol_size=10),
        opts.GraphNode(name="结点2", symbol_size=20),
        opts.GraphNode(name="结点3", symbol_size=30),
        opts.GraphNode(name="结点4", symbol_size=40),
        opts.GraphNode(name="结点5", symbol_size=50),
    ]
    links = [
        opts.GraphLink(source="结点1", target="结点2"),
        opts.GraphLink(source="结点2", target="结点3"),
        opts.GraphLink(source="结点3", target="结点4"),
        opts.GraphLink(source="结点4", target="结点5"),
        opts.GraphLink(source="结点5", target="结点1"),
    ]

    c = (
        Graph()
        .add('', nodes, links, repulsion=4000)
        .set_global_opts(title_opts=opts.TitleOpts(title='Graph-GraphNode-GraphLink'))
    )

    return c


# c = graph_with_opts()
# c.render('data/b4_graph_node_link.html')

def graph_weibo():
    with open('data/weibo.json', 'r', encoding='utf-8') as f:
        j = json.load(f)
        nodes, links, categories, cont, mid, userl = j

    c = (
        Graph()
        .add('', nodes, links, categories, repulsion=50,
             linestyle_opts=opts.LineStyleOpts(curve=0.2),
             label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(title='Graph-weibo')
        )
    )

    return c


# c = graph_weibo()
# c.render('data/b4_graph_weibo.html')


def graph_les_miserables():
    with open('data/les-miserables.json', 'r', encoding='utf-8') as f:
        j = json.load(f)
        nodes = j['nodes']
        links = j['links']
        categories = j['categories']

    c = (
        Graph(init_opts=opts.InitOpts(width='1000px', height='600px'))
        .add('', nodes=nodes, links=links, categories=categories,
             layout='circular', is_rotate_label=True,
             linestyle_opts=opts.LineStyleOpts(color='source', curve=0.3),
             label_opts=opts.LabelOpts(position='right'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Graph-Les Miserables'),
            legend_opts=opts.LegendOpts(
                orient='vertical', pos_left='2%', pos_top='20%'
            )
        )
    )

    return c


c = graph_les_miserables()
c.render('data/b4_graph_les_miserables.html')