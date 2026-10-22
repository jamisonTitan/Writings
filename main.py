from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        # determine what button was pressed from the main page
        # by querying the request object sent from the POST req
        # and render the appropriate html from static/templates
        match list(request.form.to_dict().keys())[0]:
            case "creative":
                return redirect(url_for("creative"))
            case "opinion":
                return redirect(url_for("opinion"))
    else:
        return render_template('index.html')

@app.route("/creative")
def creative():
    return render_template('creative.html')

@app.route("/opinion")
def opinion():
    return render_template('opinion.html')

if __name__ == "__main__":
    app.run()

