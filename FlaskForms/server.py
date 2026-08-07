from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def write_to_file(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    with open("database.txt", mode="a") as database:
        database.write(f"\n{email}, {subject}, {message}")


@app.route("/")
def home():
    return render_template("contact.html")

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect("/thankyou.html")

    return "Something went wrong!"

@app.route("/thankyou.html")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)