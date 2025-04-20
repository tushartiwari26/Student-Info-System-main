

import pandas as pd
import matplotlib.pyplot as plt
from utils import init_data, calculate_grade, DATA_FILE
from gpa_calculator import calculate_gpa

def add_student():
    df = pd.read_csv(DATA_FILE)
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    grade = calculate_grade(marks)
    new_row = {'ID': student_id, 'Name': name, 'Marks': marks, 'Grade': grade}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    print("Student added successfully.\n")

def update_student():
    df = pd.read_csv(DATA_FILE)
    student_id = input("Enter student ID to update: ")
    if student_id in df['ID'].values:
        marks = float(input("Enter new marks: "))
        df.loc[df['ID'] == student_id, 'Marks'] = marks
        df.loc[df['ID'] == student_id, 'Grade'] = calculate_grade(marks)
        df.to_csv(DATA_FILE, index=False)
        print("Student updated successfully.\n")
    else:
        print("Student ID not found.\n")

def delete_student():
    df = pd.read_csv(DATA_FILE)
    student_id = input("Enter student ID to delete: ")
    df = df[df['ID'] != student_id]
    df.to_csv(DATA_FILE, index=False)
    print("Student deleted successfully.\n")

def view_summary():
    df = pd.read_csv(DATA_FILE)
    print("\nStudent Summary:\n", df)
    print("\nClass Average Marks:", df['Marks'].mean())
    print("Topper:", df.loc[df['Marks'].idxmax()])

def visualize_data():
    df = pd.read_csv(DATA_FILE)
    plt.bar(df['Name'], df['Marks'], color='skyblue')
    plt.xlabel("Student Name")
    plt.ylabel("Marks")
    plt.title("Student Performance")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def export_csv():
    df = pd.read_csv(DATA_FILE)
    df.to_csv('exported_students.csv', index=False)
    print("Data exported to 'exported_students.csv'\n")

def import_csv():
    file_path = input("Enter CSV file path to import: ")
    df_new = pd.read_csv(file_path)
    df_old = pd.read_csv(DATA_FILE)
    df_combined = pd.concat([df_old, df_new], ignore_index=True).drop_duplicates(subset='ID')
    df_combined.to_csv(DATA_FILE, index=False)
    print("Data imported successfully.\n")

def menu():
    init_data()
    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Summary")
        print("5. Visualize Performance")
        print("6. Export to CSV")
        print("7. Import from CSV")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            view_summary()
        elif choice == '5':
            visualize_data()
        elif choice == '6':
            export_csv()
        elif choice == '7':
            import_csv()
        elif choice == '8':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
