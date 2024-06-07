from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import Bug

@app.route('/')
def index():
    bugs = Bug.query.all()
    return render_template('index.html', bugs=bugs)

@app.route('/file_bug', methods=['GET', 'POST'])
def file_bug():
    if request.method == 'POST':
        name = request.form['name']
        bug_type = request.form['bug_type']
        bug_description = request.form['bug_description']
        bug_priority = request.form['bug_priority']
        new_bug = Bug(name=name, bug_type=bug_type, bug_description=bug_description, bug_priority=bug_priority)
        db.session.add(new_bug)
        db.session.commit()
        flash('Bug filed successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('file_bug.html')

@app.route('/change_status/<int:bug_id>', methods=['GET', 'POST'])
def change_status(bug_id):
    bug = Bug.query.get_or_404(bug_id)
    if request.method == 'POST':
        bug.bug_status = request.form['bug_status']
        db.session.commit()
        flash('Status updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('change_status.html', bug=bug)

@app.route('/report/<int:bug_id>')
def report(bug_id):
    bug = Bug.query.get_or_404(bug_id)
    return render_template('report.html', bug=bug)
