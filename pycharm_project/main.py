# This is a sample Python script.
# !/home/chris/code/pycharm_project/
import scipy
import matplotlib
import pandas
import sklearn
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def load_data():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(url, names=names)
    print(dataset.shape)
    print(dataset.head)
    print(dataset.describe)
    # box and whisker plots
    dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
    pyplot.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Chris')
    load_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
