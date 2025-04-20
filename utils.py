import pandas as pd
import os

DATA_FILE = 'student_data.csv'

def init_data():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=['ID', 'Name', 'Marks', 'Grade'])
        df.to_csv(DATA_FILE, index=False)

def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'F'
