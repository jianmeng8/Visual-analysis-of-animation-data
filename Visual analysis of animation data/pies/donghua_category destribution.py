
import pandas as pd
from sqlalchemy import create_engine

sql = 'select * from zhuanlan_donghua'
conn = create_engine('mysql+pymysql://root:123456@localhost:3306/bilibili')

df = pd.read_sql("SELECT F1,art_words,art_like,art_view FROM  donghua_one ", conn)
df0 = df[['art_words']]
df0_tolist = [df0.iloc[i].tolist() for i in range(len(df0))]
df1 = df[['art_view']]
df1_tolist = [df1.iloc[i].tolist() for i in range(len(df1))]
df2 = df[['art_like']]
df2_tolist = [df2.iloc[i].tolist() for i in range(len(df2))]

df3 = pd.read_sql("SELECT F1,art_like,art_reply,art_favorite FROM  donghua_two ", conn)
df4 = df[['art_like']]
df4_tolist = [df4.iloc[i].tolist() for i in range(len(df4))]
# df5 = df[['art_reply']]
# df5_tolist = [df5.iloc[i].tolist() for i in range(len(df5))]
# df6 = df[['art_favorite']]
# df6_tolist = [df6.iloc[i].tolist() for i in range(len(df6))]
#
df7 = pd.read_sql("SELECT F1,art_coin,art_share FROM  donghua_three ", conn)
# df8 = df[['art_coin']]
# df8_tolist = [df8.iloc[i].tolist() for i in range(len(df8))]
# df9 = df[['art_share']]
# df9_tolist = [df9.iloc[i].tolist() for i in range(len(df9))]


from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.charts import Scatter
from pyecharts.charts import Funnel
from pyecharts.charts import Polar
from pyecharts.commons.utils import JsCode

def bar_datazoom() -> Bar:
    c = (
        Bar()
        .add_xaxis(xaxis_data=list(df.F1))
        .add_yaxis("文章字数", [199, 66, 33, 46, 21, 24, 13, 13, 12, 9, 99])
        .set_global_opts(title_opts=opts.TitleOpts(title="文章字数分布图"),)
    )
    return c

def line_markpoint() -> Line:
    c = (
        Line()
        # 配置x轴数据
        .add_xaxis(xaxis_data=list(df.F1))
        # 配置Y轴数据
        .add_yaxis("art_view", df1_tolist)
        # 全局配置
        .set_global_opts(
            # AxisOpts：坐标轴配置项。 is_scale 是否显示 x 轴。
            xaxis_opts=opts.AxisOpts(is_scale=True),
            # y轴配置项
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                # 分割区域配置项
                splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)),
            ),
            # 区域缩放配置项
            datazoom_opts=[opts.DataZoomOpts()],
            # 标题配置项
            title_opts=opts.TitleOpts(title="文章浏览数目分布图"),
        )

    )
    return c

def Scatter_point() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(xaxis_data=list(df.F1))
        .add_yaxis("art_like", df2_tolist)
        .set_global_opts(title_opts=opts.TitleOpts(title="文章点赞数散点分布图"))

    )
    return c

def Scatter_point_one() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(xaxis_data=list(df3.F1))
        .add_yaxis("文章点赞数", [441, 35, 13, 8, 8, 30])
        .set_global_opts(title_opts=opts.TitleOpts(title="文章点赞数散点分布图"))

    )
    return c


cate = list(df3.F1)
data = [526, 6, 2, 0, 0, 1]
def Funnel_tu() -> Funnel:
    c = (
        Funnel()
        .add("文章评论数漏斗图", [list(z) for z in zip(cate, data)])
    )
    return c


cate1 = list(df3.F1)
data1 = [520, 10, 1, 2, 0, 2]
def Polar_tu() -> Polar:
    c = (
        Polar()
        .add_schema(
            radiusaxis_opts=opts.RadiusAxisOpts(data=cate, type_="category"),
        )
        .add("文章收藏数极坐标图", data, type_='bar')
    )
    return c

def title() -> Pie():
    title = (
        Pie(
            init_opts=opts.InitOpts(
                chart_id='view_title',
                width='100vw',
                # theme='dark',
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="动画数据可视化大屏",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=40,
                    # color='white'
                ),
                # 标题居中
                pos_left='center'
            ),
            legend_opts=opts.LegendOpts(
                is_show=False
            )
        )
    )
    return title

label = list(df7.F1)
values = [488, 37, 6, 2, 2]
def Pie_tu() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(label, values)])
        .set_global_opts(title_opts=opts.TitleOpts(title="文章投币数饼图"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c} {d}%"))
    )
    return c

L1 = list(df7.F1)
num  = [529, 5, 1, 0, 0]
def Pie_tu_one() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(L1, num)])
        .set_global_opts(title_opts=opts.TitleOpts(title="文章分享类别比例图"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

# def page_draggable_layout():
#     page = Page(layout=Page.DraggablePageLayout)
#     page.add(
#         bar_datazoom(),
#         line_markpoint(),
#         Scatter_point(),
#         Scatter_point_one(),
#         Funnel_tu(),
#         Polar_tu(),
#         title(),
#         Pie_tu(),
#         Pie_tu_one(),
#     )
#     page.render("static/PDL.html")


if __name__ == "__main__":
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        bar_datazoom(),
        line_markpoint(),
        Scatter_point(),
        Scatter_point_one(),
        Funnel_tu(),
        title(),
        Polar_tu(),
        Pie_tu(), 
        Pie_tu_one(),
    )
    page.render("static/PDL.html")
    # page.save_resize_html('static/PDL.html', cfg_file='static/chart_config.json', dest='result.html')

