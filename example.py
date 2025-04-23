from fasthtml.common import *
app = FastHTML()

@app.get("/")
def home():
    page = Html(
        Head(Title('Some page')),
        Body(Div('Some text, ', Img(src="https://raw.githubusercontent.com/maytlim/demo_fasthtml/main/images/image2.png"), Img(src="https://raw.githubusercontent.com/maytlim/demo_fasthtml/main/images/image1.png"), cls='myclass')))
    return page

serve()

