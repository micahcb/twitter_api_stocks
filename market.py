import pandas as pd
import pickle 
# import a pickle file called all_banks.pickle
filename = 'all_banks.pickle'
with open(filename, 'rb') as f:
    classification_dict = pickle.load(f)
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the Morning Star dataset into a Pandas DataFrame
# df = pd.read_csv('morningstar_data.csv')

# # Calculate and plot the moving averages for different stocks
# # over varying periods
# df.groupby('Stock')['Close'].rolling(window=7).mean().unstack().plot()
# plt.title('Moving Averages for Different Stocks')
# plt.show()

# # Plot heatmaps and cluster maps to visualize the correlation
# # between different attributes
# sns.heatmap(df.corr(), annot=True)
# plt.title('Heatmap of Attribute Correlations')
# plt.show()

# sns.clustermap(df.corr(), annot=True)
# plt.title('Cluster Map of Attribute Correlations')
# plt.show()
