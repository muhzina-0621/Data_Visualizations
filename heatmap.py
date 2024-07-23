import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = np.random.rand(10, 12)
df = pd.DataFrame(data, columns=[f'Month {i+1}' for i in range(12)], index=[f'Day {i+1}' for i in range(10)])

# Set the size of the plot
plt.figure(figsize=(12, 8))

# Create the heatmap
sns.heatmap(df, annot=True, cmap='coolwarm')

# Add title and labels
plt.title('Sample Heatmap')
plt.xlabel('Months')
plt.ylabel('Days')

# Show the plot
plt.show()
