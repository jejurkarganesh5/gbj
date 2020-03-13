from flask_doctor.models import *
from flask import render_template,request


@app.route("/doctor/welcome/")
def welcome_doctor_page():
    return render_template('dashboard.html',  drlist=Doctor.query.all(), doctor= Doctor.dummy_doctor())


@app.route("/doctor/add/")
def doctor_add():
    return render_template('dashboard.html',page=1,
                           drlist = Doctor.query.all(),
                           doctor = Doctor.dummy_doctor()
                           )

@app.route("/repoarts/welcome/")
def repoarts_welcome():
    return render_template('dashboard.html',page=2,
                           drlist = Doctor.query.all(),
                           doctor = Doctor.dummy_doctor()
                           )


@app.route('/doctor/save/',methods = ['POST'])
def save_or_update_doctor():
    print('user given values...',request.form)
    uservalues = request.form

    msg = ''
    if int(uservalues['drid'])>0:
        dbdr = Doctor.query.filter_by(drid=int(uservalues['drid'])).first()
        dbdr.name = uservalues['name']
        dbdr.contact = uservalues['contact']
        dbdr.specialization = uservalues['specialization']
        dbdr.hospitalcontact = uservalues['hospitalcontact']
        dbdr.hospitaladdress = uservalues['hospitaladdress']
        dbdr.hospitaltiming = uservalues['hospitaltiming']
        db.session.commit()
        msg = "Doctor Record updated..!"
    else:
        doctor = Doctor(name=uservalues['name'],
                    contact=uservalues['contact'],
                    specialization=uservalues['specialization'],
                    hospitalcontact=uservalues['hospitalcontact'],
                    hospitaladdress=uservalues['hospitaladdress'],
                    hospitaltiming=uservalues['hospitaltiming'])
        db.session.add(doctor)
        db.session.commit()
        msg ='Doctor Added...!'
    return render_template('dashboard.html', page=1, drlist=Doctor.query.all(), doctor=Doctor.dummy_doctor())


@app.route("/doctor/edit/<int:drid>")
def edit_doctor_info(drid):
    return render_template('dashboard.html',page=1, drlist=Doctor.query.all(),
                           doctor=Doctor.query.filter(Doctor.drid== drid).first())



@app.route("/doctor/delete/<int:drid>")
def delete_doctor(drid):
    dbdr = Doctor.query.filter_by(drid=drid).first()
    msg = ''
    if dbdr:
        db.session.delete(dbdr)
        db.session.commit()
        msg = "Record Removed..."

    return render_template('dashboard.html',
                           drlist=Doctor.query.all(),
                           doctor=Doctor.dummy_doctor(),
                           msg= msg
                           )


if __name__=='__main__':

    app.run(debug=True)