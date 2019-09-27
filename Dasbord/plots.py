import plotly
import plotly.express as px
from Datampg import data_mpg,Data_horsepower,Data_irit
import json


def Dist_MPG():
    df=data_mpg()
    fig = px.histogram(df, x='mpg', marginal="rug",)
    fig_json=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def Dist_Horsepower():
    df=data_mpg()
    fig = px.histogram(df, x='horsepower', marginal="rug",)
    fig_json=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json