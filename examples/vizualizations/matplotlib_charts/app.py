from fh_matplotlib import matplotlib2fasthtml
from fasthtml.common import *
import numpy as np
import matplotlib.pylab as plt
from ui_examples import show_code, FastHTML_Gallery_Standard_HDRS

app, rt = fast_app(hdrs=FastHTML_Gallery_Standard_HDRS())

@matplotlib2fasthtml
def generate_chart(num_points):
    plotdata = [np.random.exponential(1) for _ in range(num_points)]
    plt.plot(range(len(plotdata)), plotdata)

@app.get("/")
@show_code
def homepage():
    return Div(
        Div(id="chart"),
        H3("Move the slider to change the graph"),
        Input(
            type="range",
            min="1", max="10", value="1",
            get=update_chart, hx_target="#chart",
            name='slider')
    )

@app.get("/update_charts")
def update_chart(slider: int):
    return Div(
        generate_chart(slider),
        P(f"Number of data points: {slider}")
    )
