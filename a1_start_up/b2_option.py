from pyecharts.charts import Bar
from pyecharts import options as opts


bar = (
    Bar()
    .add_xaxis(['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'])
    .add_yaxis('商家A', [5,20,36,10,75,90])
    .set_global_opts(title_opts={'text':'主标题', 'subtext':'副标题'})
)

bar.render('data/b2_options.html')