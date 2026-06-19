from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return"Welcome to the Home Page"

@app.route("/index",methods=["GET"])
def index():
    return"Welcome to the Index Page"

@app.route("/passed/<int:marks>")
def passed(marks):
    return f"Congratulations! You have passed with {marks} marks."

@app.route("/failed/<int:marks>")
def failed(marks):
    return f"Sorry! You have failed with {marks} marks."


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        maths=float(request.form["maths"])
        science=float(request.form["science"])
        english=float(request.form["english"])
        
        average_marks=(maths+science+english)/3
        res=""
        if average_marks>=50:
            res="passed"
        else:
            res="failed"
        return redirect(url_for(res, marks=average_marks))

@app.route("/api", methods=["POST"])
def calculate_sum():
    data = request.get_json()
    a_val=float(dict(data)["a"])
    b_val=float(dict(data)["b"])
    return jsonify(a_val + b_val)

if __name__ == '__main__':
   app.run(debug=True)