from flask import Flask, jsonify, request
from datetime import datetime, timedelta

# "use": "@liudonghua123/now-flask"


app = Flask(__name__)

# Function to calculate due date based on last menstrual period (LMP)
def calculate_due_date(lmp_date):
    # Assuming 40 weeks gestation period
    due_date = lmp_date + timedelta(weeks=40)
    return due_date.strftime("%Y-%m-%d")

# Function to calculate trimester based on current week
def calculate_trimester(current_week):
    if current_week <= 13:
        return "First Trimester"
    elif current_week <= 26:
        return "Second Trimester"
    else:
        return "Third Trimester"

# Function to calculate fetal size based on current week
def calculate_fetal_size(current_week):
    # Dummy fetal size calculation for testing
    # Replace with actual data or calculations
    if current_week <= 13:
        return {"length": "2.9 cm - 7.4 cm", "mass": "2 g - 14 g"}
    elif current_week <= 26:
        return {"length": "22.6 cm - 36.6 cm", "mass": "430 g - 820 g"}
    else:
        return {"length": "33.6 cm - 50.7 cm", "mass": "1300 g - 3700 g"}

# Function to calculate current pregnancy week
def calculate_current_week(lmp_date):
    today = datetime.today()
    # Calculate difference in days between today and LMP
    days_since_lmp = (today - lmp_date).days
    # Calculate weeks since LMP
    current_week = days_since_lmp // 7
    return current_week

# Function to calculate remaining weeks until due date
def calculate_remaining_weeks(lmp_date):
    due_date = calculate_due_date(lmp_date)
    today = datetime.today()
    # Calculate difference in days between today and due date
    days_until_due_date = (due_date - today).days
    # Calculate remaining weeks
    remaining_weeks = max(0, days_until_due_date // 7)
    return remaining_weeks

# Function to calculate days left until due date
def calculate_days_left(lmp_date):
    due_date = calculate_due_date(lmp_date)
    today = datetime.today()
    # Calculate difference in days between today and due date
    days_left = max(0, (due_date - today).days)
    return days_left

# API endpoints
@app.route('/duedate/<lmp_date>')
def get_due_date(lmp_date):
    lmp_date = datetime.strptime(lmp_date, "%Y-%m-%d")
    due_date = calculate_due_date(lmp_date)
    return jsonify({"due_date": due_date})

@app.route('/trimester/<lmp_date>')
def get_trimester(lmp_date):
    lmp_date = datetime.strptime(lmp_date, "%Y-%m-%d")
    current_week = calculate_current_week(lmp_date)
    trimester = calculate_trimester(current_week)
    return jsonify({"trimester": trimester})

@app.route('/fetal_size/<lmp_date>')
def get_fetal_size(lmp_date):
    lmp_date = datetime.strptime(lmp_date, "%Y-%m-%d")
    current_week = calculate_current_week(lmp_date)
    fetal_size = calculate_fetal_size(current_week)
    return jsonify({"fetal_size": fetal_size})

@app.route('/current_week/<lmp_date>')
def get_current_week(lmp_date):
    lmp_date = datetime.strptime(lmp_date, "%Y-%m-%d")
    current_week = calculate_current_week(lmp_date)
    return jsonify({"current_week": current_week})

@app.route('/remaining_weeks/<lmp_date>')
def get_remaining_weeks(lmp_date):
    lmp_date = datetime.strptime(lmp_date, "%Y-%m-%d")
    remaining_weeks = calculate_remaining_weeks(lmp_date)
    return jsonify({"remaining_weeks": remaining_weeks})

@app.route('/days_left/<lmp_date>')
def get_days_left(lmp_date):
    lmp_date = datetime.strptime(lmp_date, "%Y-%m-%d")
    days_left = calculate_days_left(lmp_date)
    return jsonify({"days_left": days_left})



"""MENSTRUAL TRACKING
    ENDPOINTS AND FUNCTIONS START HERE"""

# Function to calculate the current menstrual cycle phase
def calculate_cycle_phase(last_period_date):
    today = datetime.today().date()
    cycle_length = 28  # Default menstrual cycle length (can be adjusted)
    # Calculate days since the last period
    days_since_last_period = (today - last_period_date).days
    # Calculate the day within the menstrual cycle
    cycle_day = (days_since_last_period % cycle_length) + 1
    # Determine the cycle phase based on the cycle day
    if cycle_day <= 5:
        return "Menstrual Phase"
    elif cycle_day <= 14:
        return "Follicular Phase"
    elif cycle_day <= 21:
        return "Ovulatory Phase"
    else:
        return "Luteal Phase"

# Function to estimate the chance of pregnancy
def calculate_pregnancy_chance():
    # Dummy pregnancy chance calculation for testing
    # Replace with actual calculation based on user data or algorithms
    return "Low"  # Placeholder value

# Function to calculate the date of the next period
def calculate_next_period_date(last_period_date):
    cycle_length = 28  # Default menstrual cycle length (can be adjusted)
    next_period_date = last_period_date + timedelta(days=cycle_length)
    return next_period_date.strftime("%Y-%m-%d")

# API endpoints for menstrual tracking
@app.route('/cycle_phase', methods=['POST'])
def get_cycle_phase():
    data = request.json
    last_period_date = datetime.strptime(data['last_period_date'], "%Y-%m-%d").date()
    cycle_phase = calculate_cycle_phase(last_period_date)
    return jsonify({"cycle_phase": cycle_phase})

@app.route('/pregnancy_chance')
def get_pregnancy_chance():
    pregnancy_chance = calculate_pregnancy_chance()
    return jsonify({"pregnancy_chance": pregnancy_chance})

@app.route('/next_period_date', methods=['POST'])
def get_next_period_date():
    data = request.json
    last_period_date = datetime.strptime(data['last_period_date'], "%Y-%m-%d").date()
    next_period_date = calculate_next_period_date(last_period_date)
    return jsonify({"next_period_date": next_period_date})

if __name__ == '__main__':
    app.run(debug=True)
