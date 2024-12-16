#Using matplotlib for visual of the progress of the users over time w/ different workouts
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI plotting

import csv
#Datetime is used to track exact dates and times
import datetime
import os
from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from collections import defaultdict

# Flask App Initialization
app = Flask(__name__)

# Global Constants
FILE_NAME = "workout_log.csv"

# Ensure the log file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Exercise Type", "Sets", "Reps", "Weight (lbs)"])

# Routes that is used for easy access of features
@app.route('/')
def home():
    return render_template('index.html')

#Logging is used for primarily gym goers who life weights. Our tracker features only weight, reps, and set tracking overtime.
@app.route('/log', methods=['GET', 'POST'])
def log_exercise():
    if request.method == 'POST':
        exercise_type = request.form['exercise_type']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']

        if not sets.isdigit() or not reps.isdigit() or (weight and not weight.isdigit()):
            return "Invalid input! Sets, reps, and weight should be numerical values.", 4000

        # Add Timestamp for graphs in later progress feature
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV file that is later used by the progress tracker
        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file) #Transfers log into file
            writer.writerow([timestamp, exercise_type, sets, reps, weight]) #Set data points for use of the graphs

        return redirect(url_for('home'))
    return render_template('log.html')

@app.route('/bmi', methods=['GET', 'POST'])
def calculate_bmi():
    bmi_result = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight']) #Weight is used in lbs for US users
            height = float(request.form['height']) #Height is measured in inches for exact calculations
            bmi = (weight / (height ** 2)) * 703 #Formula used to correctly calculate standard BMI for adults
            if bmi < 18.5:
                category = "Underweight Range"
            elif 18.5 <= bmi <= 24.9:
                category = "Normal weight Range"
            elif 25 <= bmi <= 29.9:
                category = "Overweight Range"
            else:
                category = "Obese Range" #Obese range rather than exactly saying a user is obese. Making it less harsh.
            bmi_result = {"bmi": round(bmi, 2), "category": category}
        except ValueError:
            return "Invalid input! Please enter numerical values.", 400 
    return render_template('bmi.html', bmi_result=bmi_result)

#Main appeal of code that allows users to track their progress overtime and see if they made any positve or negative change
@app.route('/progress')
def view_progress():
    if not os.path.exists(FILE_NAME): #Defenisve code in case of error with input
        return "No workout data found. Log some exercises first!"

    try:
        data = defaultdict(list)
        dates = []

        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) < 5 or not row[4]:
                    continue  # Skip rows with missing data
                try:
                    date = row[0]
                    exercise_type = row[1]
                    weight = float(row[4])

                    if date not in dates: #Defensive code in case of possible errors
                        dates.append(date)
                    data[exercise_type].append((date, weight))
                except ValueError:
                    continue

        # Generate plots for each exercise type. No limit of which exercise the user wants to track progress of.
        plots = {}
        for exercise, values in data.items():
            values.sort()  # Sort by date
            exercise_dates, weights = zip(*values)

            # Plotting the data
            plt.figure(figsize=(10, 5))
            plt.plot(exercise_dates, weights, marker="o", label=f"{exercise} (lbs)")
            plt.xlabel("Date") #Realtime data and time tracking
            plt.ylabel("Weight (lbs)") 
            plt.title(f"Progress for {exercise}")
            plt.legend()
            plt.grid()
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Save plot as an image in base64 format
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            buffer.close()
            plots[exercise] = image_base64
            plt.close()

        return render_template('progress.html', plots=plots)
    except Exception as e:
        return f"An error occurred: {e}", 500   
@app.route('/exercise-list')
def exercise_list():
    return render_template('exercise_list.html')

if __name__ == "__main__":
    app.run(debug=True)
