import csv
import datetime
import os
import matplotlib.pyplot as plt
#Using matplotlib for the graphs for the visual of progress for users

# Global Constants
FILE_NAME = "workout_log.csv"

# Functions for Logging Exercises
def log_exercise():
    print("\nLog New Exercise")
    try:
        exercise_type = input("Enter Exercise Type (e.g., Bicep Curls, Cardio): ").strip()
        sets = input("Enter Number of Sets: ").strip()
        reps = input("Enter Reps per Set (or duration in minutes for cardio): ").strip()
        weight = input("Enter Weight per Rep (lbs, or leave blank for cardio): ").strip()
        
        if not sets.isdigit() or not reps.isdigit() or (weight and not weight.isdigit()):
            print("Invalid input! Sets, reps, and weight should be numerical values.")
            return
        
        # Add Timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save to CSV
        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, exercise_type, sets, reps, weight])
        
        print("Exercise logged successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Functions for BMI Calculation using data on comparing weight to height for body mass (Male & Value variation in progress)
def calculate_bmi():
    print("\nCalculate BMI")
    try:
        weight = float(input("Enter your weight in lbs: "))
        height = float(input("Enter your height in inches: "))
        bmi = (weight / (height ** 2)) * 703
        print(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            print("You are in the underweight range1.")
        elif 18.5 <= bmi <= 24.9:
            print("You have a normal weight range.")
        elif 25 <= bmi <= 29.9:
            print("You are overweight.")
        else:
            print("You are in the obese range.")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

# Functions for Calories Burned (Using averages of MET, weight, and duration)
def calculate_calories():
    print("\nEstimate Calories Burned")
    try:
        weight = float(input("Enter your weight in lbs: "))
        duration = float(input("Enter workout duration in minutes: "))
        met = float(input("Enter MET value (use 6 for moderate intensity weightlifting): "))
        # Convert weight from lbs to kg for calorie formula
        weight_kg = weight / 2.20462
        calories = (met * 3.5 * weight_kg / 200) * duration
        print(f"Estimated Calories Burned: {calories:.2f} kcal")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

# View Progress and Visualization with a graph and automatically populates progress
def view_progress():
    print("\nView Progress Report")
    if not os.path.exists(FILE_NAME):
        print("No workout data found. Log some exercises first!")
        return
    #Values for the graph that is shown for the progress
    dates = []
    weights = []
    exercise_types = []
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row:
                dates.append(row[0])
                exercise_types.append(row[1])
                weights.append(float(row[4]) if row[4] else 0)
    
    if not dates or not weights:
        print("No data available for visualization.")
        return

    # Plotting data points based on data inputted by user
    plt.figure(figsize=(10, 5))
    plt.plot(dates, weights, marker="o", label="Weight (lbs)")
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.title("Progress Over Time")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Weekly Summary
def weekly_summary():
    print("\nWeekly Summary")
    if not os.path.exists(FILE_NAME):
        print("No workout data found. Log some exercises first!")
        return

    current_week = datetime.datetime.now().isocalendar()[1]
    weekly_data = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row:
                log_date = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
                if log_date.isocalendar()[1] == current_week:
                    weekly_data.append(row)

    if not weekly_data:
        print("No workouts logged for this week.")
        return

    total_sets = sum(int(row[2]) for row in weekly_data)
    total_reps = sum(int(row[3]) for row in weekly_data)
    total_weight = sum(float(row[4]) for row in weekly_data if row[4])

    print(f"Workouts This Week: {len(weekly_data)}")
    print(f"Total Sets: {total_sets}")
    print(f"Total Reps: {total_reps}")
    print(f"Total Weight Lifted: {total_weight:.2f} lbs")

# Filter Logs on specific exericises that user did (filter in progress for certain exercises)
def filter_logs():
    print("\nFilter Logs by Exercise Type")
    if not os.path.exists(FILE_NAME):
        print("No workout data found. Log some exercises first!")
        return

    exercise_type = input("Enter the exercise type to filter by: ").strip()
    filtered_data = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row and row[1].lower() == exercise_type.lower():
                filtered_data.append(row)

    if not filtered_data:
        print(f"No logs found for exercise type: {exercise_type}")
        return

    print(f"Logs for {exercise_type}:")
    for log in filtered_data:
        print(f"{log[0]} | Sets: {log[2]}, Reps: {log[3]}, Weight: {log[4]} lbs")

# Main Menu display of different features in the program
def main_menu():
    while True:
        print("\nFitness Tracker")
        print("1. Log Exercise")
        print("2. Calculate BMI")
        print("3. Estimate Calories Burned")
        print("4. View Progress Report")
        print("5. Weekly Summary")
        print("6. Filter Logs by Exercise Type")
        print("7. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            log_exercise()
        elif choice == "2":
            calculate_bmi()
        elif choice == "3":
            calculate_calories()
        elif choice == "4":
            view_progress()
        elif choice == "5":
            weekly_summary()
        elif choice == "6":
            filter_logs()
        elif choice == "7":
            print("Exiting program. Stay healthy & have a great rest of your day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Entry Point
if __name__ == "__main__":
    # Ensure the log file exists
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Exercise Type", "Sets", "Reps", "Weight (lbs)"])
    
    # Run the main menu
    main_menu()
