from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)


#     __name__ kya hota hai?

# Python har file ko ek special variable deta hai.

# Us variable ka naam hai:

# __name__

# Ye batata hai ki file kaise run hui.

# Case 1: File directly run hui

# Maan lo file hai

# server.py

# Aur tum terminal me likhti ho

# python server.py

# Ab Python bolega

# Ye meri main file hai.

# To

# __name__

# ki value hogi

# "__main__"

# Isliye

# if __name__ == "__main__":

# True ho jayega.

# Aur ye chalega

# app.run(debug=True)

# Server start ho jayega.

# Case 2: File import hui

# Maan lo ek aur file hai

# test.py

# Aur usme likha

# import server

# Ab Python sochega

# Server.py ko run nahi kiya gaya.

# Bas import kiya gaya hai.

# To

# __name__

# ki value hogi

# "server"

# Na ki

# "__main__"

# Ab condition

# if __name__ == "__main__":

# False ho jayegi.

# Aur

# app.run()

# Nahi chalega.


# app.run(debug=True) kya karta hai?

# Ye Flask server ko start karta hai.

# app.run()

# Matlab

# Flask application chala do.

# debug=True ka matlab?

# Development mode ON.

# Iske fayde:

# 1. Automatic Reload

# Code save karte hi server automatically restart ho jata hai.

# Tumhe baar-baar

# python server.py

# nahi chalana padta.

# 2. Errors achhe se dikhata hai

# Agar code me mistake ho

# print(x)

# Aur x exist nahi karta.

# Browser me pura error page aa jayega.

# Without debug:

# Internal Server Error

# With debug:

# NameError:
# name 'x' is not defined