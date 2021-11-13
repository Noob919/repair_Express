from core import app,db
from flask import render_template, request
from core.models import Repair
from core.forms import  RepairmentForm

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

@app.route('/repairment', methods= ['GET', 'POST'])
def repairment_page():
    repair_form = RepairmentForm()
    if request.method == 'POST':
        repair = Repair(name = repair_form.name.data,
        email_address = repair_form.email_address.data,
        phone_model = repair_form.phone_model.data,
        warrenty =  repair_form.warrenty.data,
        desc_Repair = repair_form.desc_Repair.data,
        address = repair_form.address.data)
        db.session.add(repair)
        db.session.commit()

    return render_template('repairment.html', form = repair_form)


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