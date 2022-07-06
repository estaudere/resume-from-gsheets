import os
from flask import Flask, request, render_template, jsonify, url_for, send_file, send_from_directory
import requests
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')
KEY = "AIzaSyAbcwyz3Ba-7WRyTcIw_X_UBumxYQbhyWA"

host = "http://127.0.0.1:5000/"

@app.route('/<id>')
def resume(id):
    intro = pull_sheet_data(id, "Intro")
    education = pull_sheet_data(id, "Education")
    experience = pull_sheet_data(id,"Experience")
    skills = pull_sheet_data(id, "Skills")

    return render_template('resume.html', intro=intro, education=education, experience=experience, skills=skills)

@app.route('/<id>/pdf')
def resume_pdf(id):
    intro = pull_sheet_data(id, "Intro")
    education = pull_sheet_data(id, "Education")
    experience = pull_sheet_data(id,"Experience")
    skills = pull_sheet_data(id, "Skills")

    html_string = render_template('resume.html', intro=intro, education=education, experience=experience, skills=skills)
    html = HTML(string=html_string)
    font_config = FontConfiguration()
    css = CSS(filename='./public/pdf.css', font_config=font_config)
    html.write_pdf('resume.pdf', stylesheets=[css])

    return "hello"

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'public'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


def get_skills_map(skills):
    categories = [skill[1] for skill in skills[1:]]
    unique_categories = list(set(categories))

    if "Other" in unique_categories:
        unique_categories.remove("Other")
        unique_categories.append("Other")

    skill_dict = {cat: [] for cat in unique_categories}
    for skill in skills[1:]:
        skill_dict[skill[1]].append(skill[0])

    for k, v in skill_dict.items():
        skill_dict[k] = ", ".join(v)

    return skill_dict.items()
app.jinja_env.globals.update(get_skills_map=get_skills_map)

def pull_sheet_data(sheet_id, table_name):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + sheet_id + "/values/" + table_name +"?majorDimension=ROWS&key=" + KEY
    return requests.get(url).json().get('values')



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)