# Student Attendance Tracker

## Description
A Python-based project to track student attendance and marks, and identify students who are at academic risk.

## Features
- Calculates attendance percentage
- Identifies students with attendance below 75% or marks below 40
- Saves list of at-risk students to a separate CSV file

## Requirements
- Python 3.x
- pandas library

## Installation
1. Clone this repository or download the ZIP file.
2. Ensure `pandas` is installed:
   ```bash
   pip install pandas
   ```

## Usage
1. Place `student_data.csv` and `tracker.py` in the same folder.
2. Run the script:
   ```bash
   python tracker.py
   ```
3. View the `students_at_risk.csv` file for results.

## Sample Data
| Name  | Total Classes | Classes Attended | Marks |
|-------|---------------|------------------|-------|
| Amit  | 50            | 45               | 78    |
| Priya | 50            | 30               | 55    |
| Rohit | 50            | 20               | 35    |
| Neha  | 50            | 48               | 90    |
| Vikas | 50            | 37               | 60    |
