import sys
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

matplotlib.rc('xtick', labelsize=8) 
matplotlib.rc('ytick', labelsize=8) 


def new_plot (data):
    counts = Counter(data)
    labels, values = zip(*counts.items())
    # sort your values in descending order
    indSort = np.argsort(values)[::-1]
    # rearrange your data
    labels = np.array(labels)[indSort]
    values = np.array(values)[indSort]
    indexes = np.arange(len(labels))
    x = labels
    y = indexes

    fig, ax = plt.subplots()
    width = 0.75 # the width of the bars 
    ind = np.arange(len(y))  # the x locations for the groups
    ax.barh(indexes, values, width, color="blue")
    ax.set_yticks(ind+width/2)
    ax.set_yticklabels(x, minor=False)
    #plt.title('Distribution by type (Padma)')
    #plt.title('Distribution by field')
    plt.title('Distribution by geography')

    for i, v in enumerate(values):
        ax.text(v + 0, i + .25, str(v), color='blue')
    plt.show()

if __name__ == "__main__":

    df = pd.read_csv(sys.argv[1])

    col = int(sys.argv[2])

    #data = df['Padma'].str.strip().tolist()
    #data = df['Field'].str.strip().tolist()
    data = df['State/Country'].str.strip().tolist()

    print("data:", data)

    for i in range(0, len(data)):
      print(i+1, data[i])

    #get_plot(data)
    new_plot(data)
