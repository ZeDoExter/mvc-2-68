from flask import Flask, render_template, request, redirect, url_for, flash
import controller
import model

app = Flask(__name__, template_folder='view')
app.secret_key = 'secret-key'

model.init_db()

@app.route('/')
def index():
    shelters = controller.get_shelters()
    citizens = controller.get_all_citizens()
    unassigned = [c for c in citizens if not c['assigned']]
    return render_template('index.html', shelters=shelters, total=len(citizens), unassigned=len(unassigned))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        result = controller.register_citizen(
            request.form['id'],
            request.form['name'],
            int(request.form['age']),
            request.form['health'],
            request.form['type']
        )
        flash(result['message'], 'success' if result['success'] else 'error')
        return redirect('/register')
    
    all_c = controller.get_all_citizens()
    vip = controller.get_citizens_by_type('vip')
    risk = controller.get_citizens_by_type('risk_group')
    normal = controller.get_citizens_by_type('normal')
    
    return render_template('register.html', all=all_c, vip=vip, risk=risk, normal=normal)

@app.route('/shelters')
def shelters():
    shelters = controller.get_shelters()
    citizens = controller.get_all_citizens()
    unassigned = [c for c in citizens if not c['assigned']]
    return render_template('shelters.html', shelters=shelters, unassigned=len(unassigned))

@app.route('/allocate', methods=['POST'])
def allocate():
    controller.allocate_citizens()
    flash('จัดสรรเสร็จแล้ว', 'success')
    return redirect('/shelters')

@app.route('/report')
def report():
    data = controller.get_report()
    return render_template('report.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
