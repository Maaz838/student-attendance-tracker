import pandas as pd

# Load data
data = pd.read_csv('student_data.csv')

# Display data
print("Student Data:")
print(data)

# Calculate attendance percentage
data['Attendance %'] = (data['Classes Attended'] / data['Total Classes']) * 100

# Check students at risk (less than 75% attendance or marks below 40)
at_risk = data[(data['Attendance %'] < 75) | (data['Marks'] < 40)]

print("\nAttendance and Marks with Percentage:")
print(data)

print("\nStudents at Risk:")
print(at_risk)

# Save at risk students to file
at_risk.to_csv('students_at_risk.csv', index=False)
print("\nData of students at risk saved to 'students_at_risk.csv'")
