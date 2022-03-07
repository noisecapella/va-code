from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    first_name_phrase = request.args.get("first_name")
    if first_name_phrase:
        frame = pd.read_csv("./data/patient_tb.csv")
        matching_rows = frame[frame["PatientFirstName"].str.lower() == first_name_phrase.lower()]
        matching_rows = matching_rows.drop_duplicates(subset=["PatientID", "MostRecentTestDate", "TestName"], keep='last')
        return render_template("search.html", matching_rows=matching_rows, first_name_phrase=first_name_phrase)
    return render_template("search.html")
