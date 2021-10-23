""" 
 2. Examine the effects of varying the number of bins for continuous attributes during the discretization step. Please put your code for this question parts(ii, iii, iv) in a file called 5 2.py.
    (i) Given the number of bins b ∈ B = {2, 5, 10, 50, 100, 200}, perform discretization for all
    columns in set continuous valued columns by splitting the values in each column into b
    bins of equal width within its range. For this task, you can re-use your discretize.py
    code to perform the binning procedure, now taking the number of bins as a parameter
    and using dating.csv as input as earlier.)

    (ii) Repeat the train-test split as described in Question 4 for the obtained dataset after
    discretizing each continuous attribute into b bins.

    (iii) For each value of b, train the NBC on the corresponding new training dataset by calling your nbc(t frac) function with t frac = 1, and apply the learned model on the
    corresponding new test dataset.

    (iv) Draw a plot to show how the value of b affects the learned NBC model’s performance
    on the training dataset and the test dataset, with x-axis representing the value of b and

"""
from discretize import discretize_5_2
# directly importing the function instead of repeating code here.
import matplotlib.pyplot as plt
import pandas as pd
import importlib
from split import splitDataset
import matplotlib.patches as mpatches
import copy
# cant import like this due to file name hence using importlib
# from 5_1.py import nbc
fivePart1 = importlib.import_module('5_1')

bArray = [2, 5, 10, 50, 100, 200]
trainResult = []
testResult = []

# taking the plots from 2_2 but now as a comparison graph
def constructGraph(trainingResult, testResult):
    fig = plt.figure()
    fig.set_figwidth(7)
    fig.set_figheight(5)
    fig.subplots_adjust(bottom=0.3)
    plt.plot(bArray, trainResult, color='red')
    plt.plot(bArray, testResult, color='blue')
    plt.scatter(bArray, trainResult, color='red')
    plt.scatter(bArray, testResult, color='blue')
    plt.xlabel('Number of bins')
    plt.ylabel('Accuracy of train and test')
    red_patch = mpatches.Patch(color='red', label='train set')
    blue_patch = mpatches.Patch(color='blue', label='test set')
    plt.legend(handles=[red_patch, blue_patch])
    plt.savefig('5_2comparisonPlot.jpg')
    plt.show()
    

def main():

    for b in bArray:
        discretize_5_2(data_frame = pd.read_csv('dating.csv'), bins=b)
        splitDataset('dating-binned_5_2.csv')
        accuracyTrain, accuracyTest = fivePart1.nbc_5_2(1, 'trainingSet_5_2.csv', 'testSet_5_2.csv')
        trainResult.append(accuracyTrain)
        testResult.append(accuracyTest)
        print('Bin size: %s\nTraining Accuracy: %.2f\nTesting Accuracy: %.2f'% (b, accuracyTrain, accuracyTest))
    constructGraph(trainResult, testResult)

main()