from flask import Blueprint, render_template, request, redirect, url_for

angela_bp = Blueprint(
    'angela_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/angelas_world/static'
)

@angela_bp.route('/')
def start():
    return render_template("angela's_world.html")


@angela_bp.route('/band-name-generator')
def home():
    return render_template('band_name_generator.html', band_name=None)

@angela_bp.route('/greet', methods=['POST'])
def greet():
    city = request.form['city']
    city = city.title()
    pet_name = request.form['pet_name']
    pet_name = pet_name.title()
    band_name = f"{city} {pet_name}"
    return render_template('band_name_generator.html', band_name
                           =band_name)

# Added this new route to reset the form on refresh
@angela_bp.route('/reset', methods=['GET', 'POST'])
def reset():
    return redirect(url_for('angela_bp.home'))


@angela_bp.route('/tip_calculator')
def tip_calc():
    return render_template('tip_calculator.html', bill_per_person=None)

@angela_bp.route('/tip_info', methods=['POST'])
def tip_info():
    bill = float(request.form['bill'])
    tip_percentage = float(request.form['tip_percentage'])
    people = int((request.form['people']))
    calc_tip = 1 + (tip_percentage)/100
    bill_per_person = (bill * calc_tip)/people
    bill_per_person = f"The total bill per person is ${bill_per_person:.2f}" 
    return render_template('tip_calculator.html', bill_per_person=bill_per_person)

@angela_bp.route('/reset_tip', methods=['GET'])
def reset_tip():
    return redirect(url_for('angela_bp.tip_calc'))




