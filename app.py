from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")

# @app.route()
# def xray():
#     return render_template()

# @app.route()
# def audio():
#     return render_template()

# @app.route()
# def app():
#     return render_template()


app.run(debug=True)
    