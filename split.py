""" 
    Use the sample function from pandas with the parameters initialized as random state = 47,
    frac = 0.2 to take a random 20% sample from the entire dataset. This sample will serve as your
    test dataset, and the rest will be your training dataset. (Note: The use of the random state will
    ensure all students have the same training and test datasets; incorrect or no initialization of this
    parameter will lead to non-reproducible results). Create a new script called split.py that takes
    dating-binned.csv as input and outputs trainingSet.csv and testSet.csv.
"""
import pandas as pd

def splitDataset(fileName):
    data = pd.read_csv(fileName)
    test_data = data.sample(frac=0.2, random_state=47)
    indexUsed = test_data.index
    data.drop(indexUsed, axis=0, inplace=True) #all rows other than those already in test_data to prevent overfitting
    test_data.to_csv("testSet_5_2.csv", index = False)
    data.to_csv("trainingSet_5_2.csv", index = False)

def main():
    data = pd.read_csv("dating-binned.csv")
    test_data = data.sample(frac=0.2, random_state=47)
    indexUsed = test_data.index
    data.drop(indexUsed, axis=0, inplace=True) #all rows other than those already in test_data to prevent overfitting
    test_data.to_csv("testSet.csv", index = False)
    data.to_csv("trainingSet.csv", index = False)

main()