import matplotlib.pyplot as plt 
import seaborn as sns

def visualize_penguin_data():
    """
    Load the penguins dataset from seaborn and create a pairplot to visualize pairwise relationships
    between variables, with different species represented by different colors.

    Returns:
    charts of penguin data from the seaborn dataset.
    """
    df = sns.load_dataset("penguins")
    sns.pairplot(df, hue="species")

visualize_penguin_data()
plt.show()



