from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("feedback.html")

@app.route('/feedback',methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("message")

        return render_template("thankyou.html", user=name, message=message)
    return render_template("feedback.html")

