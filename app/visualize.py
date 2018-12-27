import plotly
from plotly.graph_objs import *

plotly.tools.set_credentials_file(username="OksanaOleniuk", api_key="DM7OQLpmiskQ2OcKVuFc")


def generate_plotly_url(x, y):
    data = Data([ Scatter(x=x, y=y)])
    return plotly.plotly.plot(data, filename='Title', auto_open=False)