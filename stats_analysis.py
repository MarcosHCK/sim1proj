from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_path = 'results.csv' 
df = pd.read_csv(data_path)

print("Dataset Head: \n")
print(df.head())

print('='*100)

print("Dataset Columns: \n")
print(df.columns)

print('='*100)

print("Dataset Summary: \n")
print(df.describe())

print('='*100)

print("Basic Statistical Estimators of maxClientWaitTime")
# Mean
means = df['maxClientWaitTime'].mean()
print("Means:\n", means)

# Standard Deviation
std_devs = df['maxClientWaitTime'].std()
print("Standard Deviations:\n", std_devs)

# Variance
variances = df['maxClientWaitTime'].var()
print("Variances:\n", variances)

print('='*100)

print("Basic Statistical Estimators of averageServiceTimePerClient")
# Mean
means = df['averageServiceTimePerClient'].mean()
print("Means:\n", means)

# Standard Deviation
std_devs = df['averageServiceTimePerClient'].std()
print("Standard Deviations:\n", std_devs)

# Variance
variances = df['averageServiceTimePerClient'].var()
print("Variances:\n", variances)

print('='*100)

print("Basic Statistical Estimators of maxClientsInQueue ")
# Mean
means = df['maxClientsInQueue'].mean()
print("Means:\n", means)

# Standard Deviation
std_devs = df['maxClientsInQueue'].std()
print("Standard Deviations:\n", std_devs)

# Variance
variances = df['maxClientsInQueue'].var()
print("Variances:\n", variances)

print('='*100)

print("Basic Statistical Estimators of totalClientsServed ")
# Mean
means = df['totalClientsServed'].mean()
print("Means:\n", means)

# Standard Deviation
std_devs = df['totalClientsServed'].std()
print("Standard Deviations:\n", std_devs)

# Variance
variances = df['totalClientsServed'].var()
print("Variances:\n", variances)

grouped = df.groupby('distribution for client arrival time')
averageServiceTimePerClient = [group['averageServiceTimePerClient'] for _, group in grouped]
fig = plt.figure()
ax = fig.add_subplot(111)
plt.boxplot(averageServiceTimePerClient)
ax.set_xticklabels([name for name, _ in grouped], rotation=45, ha="right")
plt.show()

grouped = df.groupby('distribution for all services time')
averageServiceTimePerClient = [group['averageServiceTimePerClient'] for _, group in grouped]
fig = plt.figure()
ax = fig.add_subplot(111)
plt.boxplot(averageServiceTimePerClient)
ax.set_xticklabels([name for name, _ in grouped], rotation=45, ha="right")
plt.show()

hist_col = ['averageServiceTimePerClient', 'maxClientsInQueue', 'totalClientsServed', 'meanClientWaitTime', 'totalWaitTime', 'maxClientWaitTime']
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(14, 8))
for i in range(2):
    for j in range(3):
        index = i*3 + j
        if index < len(hist_col): 
            ax[i, j].violinplot(df[hist_col[index]])
            ax[i, j].boxplot(df[hist_col[index]], showmeans=True, meanline=True)
            ax[i, j].set_xlabel(hist_col[index])

plt.tight_layout() 
plt.show()

_, p = stats.normaltest(df['totalClientsServed'])
print('P-value: ', p)
if p > 0.05:
    print('Los datos son Normales')
else:
    print('Los datos no son Normales')

stats.probplot(df['totalClientsServed'], dist="norm", plot=plt)
plt.show()

numerical_columns = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numerical_columns].corr()
plt.figure(figsize=(10, 8)) 
plt.title('Matriz de Correlación entre Variables Númericas')
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', xticklabels=numerical_columns, yticklabels=numerical_columns)
plt.show()
