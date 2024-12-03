import pandas as pd

# Load your CSV file
data = pd.read_csv('processed_dataset.csv')
data2 = pd.read_csv('pre_dataset.csv')

# Count the number of missing (NaN) values in each column
missing_counts = data.isnull().sum()

# Display the result
print(data.shape)
print(data2.shape)
print("Number of missing values in each column:")
print(missing_counts)

value_counts = data2["facades"].value_counts()

print(value_counts)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_correlation(filepath: str):
    # Load the dataset
    data = pd.read_csv(filepath)
    
    # Calculate the correlation matrix
    corr_matrix = data.corr()
    
    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))
    
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    
    # Set the title
    plt.title('Correlation Matrix Heatmap', fontsize=16)
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    visualize_correlation("processed_dataset.csv")