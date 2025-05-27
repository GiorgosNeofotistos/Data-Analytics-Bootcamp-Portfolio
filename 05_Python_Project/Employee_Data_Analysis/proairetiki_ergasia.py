import pandas as pd
import matplotlib.pyplot as plt
#Φόρτωμα του CSV αρχείου στο DataFrame
df = pd.read_csv("C:/Users/George/Desktop/filtered-employees.csv")
print(df.head())
#Ομαδοποίηση κατά Department και υπολογισμός μέσου όρου Salary και EmpSatisfaction
grouped = df.groupby('Department').agg({
    'Salary' : 'mean',
    'EmpSatisfaction' : 'mean'
}).reset_index()
print(grouped)
#Δημιουργία γραφήματος
fig, ax1 = plt.subplots(figsize=(10, 6))
# Plot για τον μισθό (Bar Chart)
ax1.bar(grouped['Department'], grouped['Salary'], color='b', alpha=0.6, label='Average Salary')
ax1.set_xlabel('Department')
ax1.set_ylabel('Average Salary', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Δημιουργία του δεύτερου άξονα y (για την ικανοποίηση)
ax2 = ax1.twinx()
ax2.plot(grouped['Department'], grouped['EmpSatisfaction'], color='r', marker='o', label='Employee Satisfaction')
ax2.set_ylabel('Employee Satisfaction', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Προσθήκη τίτλου και legend
plt.title('Average Salary and Employee Satisfaction by Department')
fig.tight_layout()

# Εμφάνιση του γραφήματος
plt.show()
#Υπολογισμός αριθμού εργαζομένων ανά τμήμα
department_counts = df['Department'].value_counts()
print(department_counts)
# Στατιστικά μισθών ανά τμήμα
salary_stats = df.groupby('Department')['Salary'].describe()
print(salary_stats)
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Viridis χρωματικός χάρτης
colors = cm.viridis([i/len(department_counts) for i in range(len(department_counts))])

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Employee Distribution by Department')
plt.axis('equal')  # Για να είναι κυκλικό το διάγραμμα
plt.show()