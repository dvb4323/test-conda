import pandas as pd
import matplotlib.pyplot as plt

# Create a simple DataFrame
data = {'Category': ['A', 'B', 'C', 'D'], 'Value': [10, 25, 15, 30]}
df = pd.DataFrame(data)

print("Data:")
print(df)

# Plot the data
df.plot(kind='bar', x='Category', y='Value', title='Sample Data Analysis')
plt.show()