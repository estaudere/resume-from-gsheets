import os
from flask import Flask, request, render_template, jsonify
import requests

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')
KEY = "AIzaSyAbcwyz3Ba-7WRyTcIw_X_UBumxYQbhyWA"

@app.route('/<id>')
def resume(id):
  intro = pull_sheet_data(id, "Intro")
  education = pull_sheet_data(id, "Education")
  experience = pull_sheet_data(id,"Experience")
  skills = pull_sheet_data(id, "Skills")

  pdf_url = "https://restpack.io/html2pdf/save-as-pdf?url=" + id

  return render_template('resume.html', intro=intro, education=education, experience=experience, skills=skills, url=pdf_url)

def get_categories(skills):
    categories = [skill[1] for skill in skills[1:]]
    unique_categories = []
    for c in categories:
        if c not in unique_categories:
            unique_categories.append(c)
    return unique_categories
app.jinja_env.globals.update(get_categories=get_categories)

def pull_sheet_data(sheet_id, table_name):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + sheet_id + "/values/" + table_name +"?majorDimension=ROWS&key=" + KEY
    return requests.get(url).json()["values"]


if __name__ == '__main__':
    app.run(debug=True)