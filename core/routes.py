from core import app
from flask import render_template

@app.route("/")
@app.route("/home")
@app.route("/index")
def index_page():
    return render_template('index.html')

@app.route('/getstatus')
def getstatus_page():
    return render_template('getstatus.html')

@app.route('/replacement')
def replacement_page():
    return render_template('replacement.html')

@app.route('/repairment')
def repairment_page():
    return render_template('repairment.html')


@app.route('/softwareupdate')
def software_page():
    return render_template('software.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/about')
def about_page():
    return render_template('Aboutus.html')

@app.route('/qna')
def qna_page():
    return render_template('qna.html')

@app.route('/progress')
def progress_page():
    return render_template('progress.html')