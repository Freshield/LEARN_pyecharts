from pyecharts import options as opts
from pyecharts.charts import Liquid, Page
from pyecharts.globals import SymbolType


def liquid_base():
    c = (
        Liquid()
        .add('lq', [0.8,0.6,0.4])
        .set_global_opts(title_opts=opts.TitleOpts('Liquid-base'))
    )

    return c


c = liquid_base()
c.render('data/b5_liquid_base.html')