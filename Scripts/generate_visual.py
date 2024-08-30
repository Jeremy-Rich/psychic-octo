import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('/Volumes/akron/bear_projects/data/output/categorized_files.csv')

# Count the non-empty entries in each column (representing each category)
category_counts = df.notna().sum()

# Create the bar chart
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar')
plt.title('Distribution of File Types')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
