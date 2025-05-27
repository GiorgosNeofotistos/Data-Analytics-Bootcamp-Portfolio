# Employee Data Analysis - Intermediate Assignment

This project analyzes employee data to extract insights regarding employee salaries, satisfaction, performance, and department distribution. The analysis is done using Python and SQL, with visualizations for deeper understanding.

## Project Overview

In this assignment, we work with a dataset (`employees.csv`) containing information about employees, such as:

- Employee details (name, ID, gender, marital status, etc.)
- Employment information (status, department, position, salary, performance score, etc.)
- Engagement metrics (satisfaction scores, absences, etc.)

The goal is to perform a series of tasks that will provide insights into employee data across multiple dimensions:

1. **Filtering Employee Data Using SQL**: Extract data with specific filters, including high-performing employees with a salary above $60,000 and high satisfaction scores.
2. **Salary & Satisfaction Analysis**: Compute the average salary and employee satisfaction for each department.
3. **Absences & Performance**: Analyze the relationship between absences and performance.
4. **Department Distribution & Salary Insights**: Visualize the distribution of employees across departments and explore salary statistics within each department.

## Project Requirements

- **Libraries/Tools Used**:
  - Python: `pandas`, `matplotlib`, `seaborn`
  - SQL for data filtering (using MySQL Workbench or any other DBMS)
  - Visualizations: Bar chart, Pie chart, Line plot
  
- **Dataset**: `employees.csv` file. The dataset is rich with detailed information on employee demographics, satisfaction, performance, and salary.

### Task Breakdown

1. **Task 1: Filtering Employee Data Using SQL**  
   SQL was used to filter employees with:
   - Performance scores of 'Exceeds' or 'Fully Meets'.
   - Salary above $60,000.
   - High employee satisfaction scores (4 or higher).
   - Currently employed individuals.
   
   The result was exported to a CSV file for further Python analysis.

2. **Task 2: Analyzing Employee Salaries & Satisfaction**  
   Using Python:
   - Grouped employees by department.
   - Calculated the average salary and satisfaction for each department.
   - Visualized the data using a dual-axis bar chart and line plot to show the relationship between salary and satisfaction.

3. **Task 3: Examining Absences & Performance**  
   Analyzed the average number of absences for employees with different performance scores, visualized using a bar chart.

4. **Task 4: Department Distribution & Salary Insights**  
   Analyzed the distribution of employees across departments and visualized the results in a pie chart. Also, computed salary statistics (mean, std, etc.) for each department.

## How to Run

To run the Python script, ensure you have the necessary libraries installed. You can install them via `pip`:

```bash
pip install -r requirements.txt
Step 1: SQL Filtering
Filter the dataset as per the requirements and export the results as filtered-employees.csv.

Step 2: Python Analysis
Use the Python script provided to:

Load the filtered dataset.

Perform analysis and generate visualizations.

Example Code
python
import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered dataset
df = pd.read_csv("filtered-employees.csv")

# Group by Department and calculate mean salary and satisfaction
grouped = df.groupby('Department').agg({
    'Salary': 'mean',
    'EmpSatisfaction': 'mean'
}).reset_index()

# Create a plot with dual Y axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot for average salary (Bar Chart)
ax1.bar(grouped['Department'], grouped['Salary'], color='b', alpha=0.6, label='Average Salary')
ax1.set_xlabel('Department')
ax1.set_ylabel('Average Salary', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second Y-axis for employee satisfaction (Line Plot)
ax2 = ax1.twinx()
ax2.plot(grouped['Department'], grouped['EmpSatisfaction'], color='r', marker='o', label='Employee Satisfaction')
ax2.set_ylabel('Employee Satisfaction', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Add a title and legends
plt.title('Average Salary and Employee Satisfaction by Department')
fig.tight_layout()

# Display the plot
plt.show()
Insights
Salary Distribution: Average salaries vary across departments, with some departments having significantly higher or lower salaries compared to others.

Employee Satisfaction: Satisfaction levels are somewhat correlated with salary but show varying trends across departments.

Absence Trends: Employees in higher performance categories tend to have fewer absences.

Conclusion
This analysis provides valuable insights into employee data, helping identify trends related to salary, performance, and satisfaction. It highlights areas where companies can improve employee engagement and optimize salary structures.

Disclaimer
This project is part of an intermediate data analysis assignment in Workearly's Data Analytics Bootcamp. The purpose of this assignment is to demonstrate proficiency in SQL, Python data analysis, and data visualization.

License
This project is licensed under the MIT License - see the LICENSE file for details.
