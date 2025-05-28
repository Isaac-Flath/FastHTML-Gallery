from fasthtml.common import *
from monsterui.all import *

app, rt = fast_app(hdrs=Theme.blue.headers())

@rt
def index():
    return Div(cls="flex items-center justify-center h-screen")(
        Button("Show Toast", cls="bg-blue-500 text-white", hx_get="toast", hx_target="body", hx_swap="afterbegin")
    )

@rt
def toast(): return Toast("Here's your toast 🍞!", dur=2, cls=[ToastVT.top, ToastHT.center], alert_cls="text-white bg-green-500 border-green-500")
