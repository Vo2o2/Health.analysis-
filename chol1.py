import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your data is saved in a CSV file named 'heart_disease.csv'
data = pd.read_csv(r'C:\Users\91832\OneDrive\Desktop\int project\Heart Disease data.csv')

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(data.describe())  # Numerical features
print(data['ca '].value_counts())  # Categorical feature (chest pain type)

# Correlation Analysis
print("\nCorrelation Matrix:")
correlation = data.corr()
print(correlation)  # Correlation coefficients for numerical features

# Visualization - Scatter Plots
print("\nScatter Plots:")
plt.figure(figsize=(10, 6))

# Explore relationships between some interesting features (adjust as needed)
plt.subplot(2, 2, 1)
plt.scatter(data['age '], data['chol '])
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.title('Cholesterol Level by Age')

plt.subplot(2, 2, 2)
plt.scatter(data['trestbps '], data['thalach '])
plt.xlabel('Resting Blood Pressure')
plt.ylabel('Maximum Heart Rate')
plt.title('Maximum Heart Rate by Resting Blood Pressure')

plt.subplot(2, 2, 3)
plt.scatter(data['fbs '], data['chol '])
plt.xlabel('Fasting Blood Sugar')
plt.ylabel('Cholesterol')
plt.title('Cholesterol Level by Fasting Blood Sugar')

plt.subplot(2, 2, 4)
plt.scatter(data['exang '], data['oldpeak '])
plt.xlabel('Exercise Angina (0=No, 1=Yes)')
plt.ylabel('ST Depression')
plt.title('ST Depression by Exercise Angina Presence')

plt.tight_layout()
plt.show()

# Visualization - Box Plots
print("\nBox Plots:")
plt.figure(figsize=(8, 6))

# Explore feature distributions across categories (adjust as needed)
sns.boxplot(x='sex ', y='chol ', data=data)
plt.xlabel('Sex')
plt.ylabel('Cholesterol')
plt.title('Cholesterol Distribution by Sex')

sns.boxplot(x='target', y='thalach ', data=data)
plt.xlabel('Heart Disease Presence (0=No, 1=Yes)')
plt.ylabel('Maximum Heart Rate')
plt.title('Maximum Heart Rate by Heart Disease Presence')

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))  # Adjust figure size as desired
data['age '].hist(bins=20, edgecolor='black')  # Adjust bin count for better visualization
plt.xlabel('age ')
plt.ylabel('Number of patients')
plt.title('Distribution of age in heart disease data')
plt.grid(True)
plt.show()

disease_groups = data.groupby('target')
disease_groups['chol '].hist(bins=15, alpha=0.5, label=['No Disease','Heart Disease'])
plt.xlabel('Serum Cholesterol (mg/dl)')
plt.ylabel('Number of patients')
plt.title('Cholesterol distribution by heart disease presence')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
data['age group'] = pd.cut(data['age '], bins=[20, 40, 60, 80], labels=['20-39', '40-59', '60+'])
sns.countplot(x='age group', hue='target', data=data)
plt.xlabel('Age Group')
plt.ylabel('Number of Patients')
plt.title('Heart Disease by Age Group')
plt.show()


heart_disease_counts = data[data['target'] == 1].groupby('sex ')['target'].count()

# Create a bar chart
plt.figure(figsize=(6, 5))
sns.barplot(x=heart_disease_counts.index, y=heart_disease_counts.values)
plt.xlabel('Gender')
plt.ylabel('Number of Patients with Heart Disease')
plt.title('Number of Heart Disease Patients by Gender')
plt.xticks(rotation=0)  # Rotate x-axis labels to prevent overlapping for long genders

# Show the plot
plt.show()
