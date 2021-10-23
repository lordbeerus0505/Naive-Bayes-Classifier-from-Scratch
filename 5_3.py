""" 
    Plot the learning curve. Please put your code for this question in a file called 5_3.py.
    (i) For each f in F = {0.01, 0.1, 0.2, 0.5, 0.6, 0.75, 0.9, 1}, randomly sample a fraction of the
    training data in trainingSet.csv with our fixed seed (i.e., random_state=47).

    (ii) Train a NBC model on the selected f fraction of the training dataset (You can call your
    nbc(t_frac) function with t_frac = f). Evaluate the performance of the learned model
    on all examples in the selected samples of training data as well as all examples in the
    test dataset (i.e., testSet.csv), and compute the accuracy respectively. Do so for all
    f ∈ F.

    (iii) Draw one plot of learning curves where the x-axis representing the values of f and
    the y-axis representing the corresponding model’s accuracy on training/test dataset.
    Comment on what you observe in this plot.
"""

import pandas as pd
import importlib
from split import splitDataset
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from discretize import discretize_5_2
fivePart1 = importlib.import_module('5_1')

fractions = [0.01, 0.1, 0.2, 0.5, 0.6, 0.75, 0.9, 1]
trainResult = []
testResult = []
bins = 5

def constructGraph(trainingResult, testResult):
    fig = plt.figure()
    fig.set_figwidth(7)
    fig.set_figheight(5)
    fig.subplots_adjust(bottom=0.3)
    plt.plot(fractions, trainResult, color='red')
    plt.plot(fractions, testResult, color='blue')
    plt.scatter(fractions, trainResult, color='red')
    plt.scatter(fractions, testResult, color='blue')
    plt.xlabel('Fraction value')
    plt.ylabel('Accuracy of train and test')
    red_patch = mpatches.Patch(color='red', label='train set')
    blue_patch = mpatches.Patch(color='blue', label='test set')
    plt.legend(handles=[red_patch, blue_patch])
    plt.savefig('5_3comparisonPlot.jpg')
    plt.show()
    

def main():
    discretize_5_2(data_frame = pd.read_csv('dating.csv'), bins=bins)
    splitDataset('dating-binned.csv')
    for frac in fractions:
        accuracyTrain, accuracyTest = fivePart1.nbc_5_2(frac, 'trainingSet.csv', 'testSet.csv')
        trainResult.append(accuracyTrain)
        testResult.append(accuracyTest)
    print(testResult, trainResult)

    constructGraph(trainResult, testResult)


main()