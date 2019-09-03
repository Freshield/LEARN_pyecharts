import os
os.environ["webdriver.chrome.driver"] = "/home/freshield/software/chromedriver/chromedriver"

from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts_snapshot.main import make_a_snapshot


bar = (
    Bar()
    .add_xaxis(['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'])
    .add_yaxis('商家A', [5,20,36,10,75,90])
    .set_global_opts(title_opts={'text':'主标题', 'subtext':'副标题'})
)

# import os
# import sys
# sys.path.append(os.path.dirname(__file__))
# print(sys.path)
make_snapshot(snapshot, bar.render(), 'data/bar.png')
# bar.render('data/b3_render.html')
# make_a_snapshot('data/b3_render.html', 'data/b3_render.pdf')