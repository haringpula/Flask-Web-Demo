import os
import json
import re
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from .helper import apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # check radio button values
        def setCheck(value):
            if value == "on":
                return "yes"
            else:
                return "no"
        # Get data from form
        fname = request.form.get("fname")
        mname = request.form.get("mname")
        lname = request.form.get("lname")
        uname = request.form.get("uname")
        address = request.form.get("address")
        region = request.form.get("region")
        province = request.form.get("province")
        city = request.form.get("city")
        barangay = request.form.get("barangay")
        postal = request.form.get("postal")
        phone = request.form.get("phone")
        email = request.form.get("email")
        gender = request.form.get("gender")
        bdate = request.form.get("bdate")
        bplace = request.form.get("bplace")
        nationality = request.form.get("nationality")
        civil = request.form.get("civil")
        maiden = request.form.get("maiden")
        employment = request.form.get("employment")
        company = request.form.get("company")
        funding = request.form.get("funding")
        q1a = setCheck(request.form.get("q1a"))
        q1b = setCheck(request.form.get("q1b"))
        q1c = setCheck(request.form.get("q1c"))
        q1d = setCheck(request.form.get("q1d"))
        q1e = setCheck(request.form.get("q1e"))
        q1f = setCheck(request.form.get("q1f"))
        q1g = setCheck(request.form.get("q1g"))
        q2 = setCheck(request.form.get("q2"))
        q3 = setCheck(request.form.get("q3"))
        q4 = setCheck(request.form.get("q4"))
        q5a = setCheck(request.form.get("q5a"))
        if q5a == "yes":
            q5b = request.form.get("q5b")
        else:
            q5b = "null"
        q6 = setCheck(request.form.get("q6"))
        q7 = setCheck(request.form.get("q7"))
        auth = request.form.get("auth")

        # create dict
        guest = {
            "fname": fname,
            "mname": mname,
            "lname": lname,
            "uname": uname,
            "address": address,
            "region": region,
            "province": province,
            "city": city,
            "barangay": barangay,
            "postal": postal,
            "phone": phone,
            "email": email,
            "gender": gender,
            "birthdate": bdate,
            "birthplace": bplace,
            "nationality": nationality,
            "civil": civil,
            "maiden": maiden,
            "employment": employment,
            "company": company,
            "funding": funding,
            "q1": {
                "q1a": q1a,
                "q1b": q1b,
                "q1c": q1c,
                "q1d": q1d,
                "q1e": q1e,
                "q1f": q1f,
                "q1g": q1g
            },
            "q2": q2,
            "q3": q3,
            "q4": q4,
            "q5": {
                "q5a": q5a,
                "q5b": q5b
            },
            "q6": q6,
            "q7": q7,
            "auth": auth
        }
        # function snippet from geekforgeeks

        def writeJson(new_data, filename='registration.json'):
            with open(filename, 'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                file_data["guests"].append(new_data)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent=4)
        writeJson(guest)
        return redirect("/")
    else:
        return render_template("index.html")

@app.route("/display")
def display():

    with open("registration.json") as f:
        data = json.load(f)
        stringJson = json.dumps(data)
        print("here")
        print(stringJson)
        return helper.apology("TODO")
    # return render_template("display.html", stringJson = stringJson)

if __name__ == '__main__':
    app.run()
