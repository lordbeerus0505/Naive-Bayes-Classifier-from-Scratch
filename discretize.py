""" 
Write a Python script named discretize.py to discretize all columns in continuous valued columns
by splitting them into 5 bins of equal-width in the range of values for that column (check fieldmeaning.pdf
for the range of each column; for those columns that you’ve finished pre-processing in Question 1(iv), 
the range should be considered as [0, 1]). If you encounter any values that lie outside the specified range
of a certain column, please treat that value as the max value specified for that column. The script reads
dating.csv as input and produces dating-binned.csv as output. As an output of your scripts, please print
the number of items in each of the 5 bins. Bins should be sorted from small value ranges to large value
ranges for each column in continuous valued columns.
"""
import pandas as pd
import numpy
import sys
import copy

def part_a(data_frame, outputFile):
    otherCols = ['sports', 'tvsports', 'exercise', 'dining', 'museums', 'art', 'hiking', 
    'gaming', 'clubbing', 'reading', 'tv', 'theater', 'movies', 'concerts', 'music', 
    'shopping', 'yoga' , 'expected_happy_with_sd_people', 'like', 'interests_correlate'
    ]
    # Rest of the fields have already been handled for and seem fine. All of these have 
    # a range 0-10 (except interest corr) so check max and min

    improper_data_list = []

    for col in otherCols[:-1]:
        maxi = data_frame[col].max()
        mini = data_frame[col].min()
        improper_data_list.append([mini, maxi])
    
    max_interests = data_frame[otherCols[len(otherCols)-1]].max()
    min_interests = data_frame[otherCols[len(otherCols)-1]].min()

    issue_data = []

    if (max_interests > 1.0 or min_interests < -1.0):
        issue_data.append(len(otherCols)-1)
    
    for i in range(len(improper_data_list)):
        if improper_data_list[i][0]<0 or improper_data_list[i][1]>10:
            issue_data.append(i)

    #issue_data has 7,9 so gaming and reading have max issues. The values correspond to 14 and 13 respectively.
    for i in [7,9]:
        col = otherCols[i]
        # for every row where data_frame[col]>10
        data_frame.loc[data_frame[col]>10, col] = 10

    discrete_cols = ['gender', 'race', 'race_o', 'samerace', 'field', 'decision'] 
    attributes = ['pref_o_attractive','pref_o_sincere','pref_o_intelligence','pref_o_funny','pref_o_ambitious',
    'pref_o_shared_interests', 'attractive_important', 'sincere_important', 'intelligence_important', 'funny_important',
    'ambition_important', 'shared_interests_important'] 

    for col in data_frame:
        if col not in discrete_cols:
            # Hasn't already been binned

            if col in attributes:
                bin_range = numpy.arange(0,1.001,0.2)
            elif col in ['age', 'age_o']:
                bin_range = numpy.arange(18,58.001,8)
            elif col == 'interests_correlate':
                # if using -1.0001 instead, values slightly change [18, 713, 2498, 2883, 632]
                bin_range = numpy.arange(-1.00,1.001,0.4)
            else:
                bin_range = numpy.arange(0,10.01,2) 
                # 5 bins for all other kinds which are 
                #in the 0-10 range - basically otherCols

            # Using pd.cut as cut splits as equal width bins opposed to qcut which is equal frequency bins
            data_frame[col] = pd.cut(data_frame[col], bin_range, labels = numpy.arange(5), 
            include_lowest = True, retbins = False)
            
            # Final list is sorted by default but pdf shows like:[] is not sorted in 
            # terms of frequencies, hence not sorting
            print("%s:"%col, data_frame[col].value_counts(sort=False).to_list())
    data_frame.to_csv(outputFile, index = False, mode = 'w')
    return data_frame

def discretize_5_2(data_frame, bins):
    otherCols = ['sports', 'tvsports', 'exercise', 'dining', 'museums', 'art', 'hiking', 
    'gaming', 'clubbing', 'reading', 'tv', 'theater', 'movies', 'concerts', 'music', 
    'shopping', 'yoga' , 'expected_happy_with_sd_people', 'like', 'interests_correlate'
    ]
    # Rest of the fields have already been handled for and seem fine. All of these have 
    # a range 0-10 (except interest corr) so check max and min

    improper_data_list = []

    for col in otherCols[:-1]:
        maxi = data_frame[col].max()
        mini = data_frame[col].min()
        improper_data_list.append([mini, maxi])
    
    max_interests = data_frame[otherCols[len(otherCols)-1]].max()
    min_interests = data_frame[otherCols[len(otherCols)-1]].min()

    issue_data = []

    if (max_interests > 1.0 or min_interests < -1.0):
        issue_data.append(len(otherCols)-1)
    
    for i in range(len(improper_data_list)):
        if improper_data_list[i][0]<0 or improper_data_list[i][1]>10:
            issue_data.append(i)

    # issue_data has 7,9 so gaming and reading have max issues. The values correspond to 14 and 13 respectively.
    for i in [7,9]:
        col = otherCols[i]
        # for every row where data_frame[col]>10
        data_frame.loc[data_frame[col]>10, col] = 10

    discrete_cols = ['gender', 'race', 'race_o', 'samerace', 'field', 'decision'] 
    attributes = ['pref_o_attractive','pref_o_sincere','pref_o_intelligence','pref_o_funny','pref_o_ambitious',
    'pref_o_shared_interests', 'attractive_important', 'sincere_important', 'intelligence_important', 'funny_important',
    'ambition_important', 'shared_interests_important'] 

    for col in data_frame:
        if col not in discrete_cols:
            # Hasn't already been binned

            if col in attributes:
                bin_range = numpy.arange(0,1.001,float(1)/bins)
            elif col in ['age', 'age_o']:
                bin_range = numpy.arange(18,58.001,float(58-18)/bins)
            elif col == 'interests_correlate':
                # if instead -1.001 we would get the answers as [18, 713, 2498, 2883, 632]
                # Based on this assumption, the values would change
                bin_range = numpy.arange(-1.000,1.001,float(2)/bins)
            else:
                bin_range = numpy.arange(0,10.01,float(10)/bins) 
                # 5 bins for all other kinds which are 
                #in the 0-10 range - basically otherCols
            
            # Using pd.cut as cut splits as equal width bins opposed to qcut which is equal frequency bins
            data_frame[col] = pd.cut(data_frame[col], bin_range, labels = numpy.arange(bins), 
            include_lowest = True, retbins = False)
            
            # Final list is sorted by default but pdf shows like:[] is not sorted in 
            # terms of frequencies, hence not sorting
            # print("%s:"%col, data_frame[col].value_counts(sort=False).to_list())
    data_frame.to_csv("dating-binned_5_2.csv", index = False, mode = 'w')
    return data_frame

def main(inputFile, outputFile):
    
    # all columns not in this list need to be discretized
    # Each of these need to be split into 5 equal width columns
    data = pd.read_csv(inputFile)
    data = part_a(copy.deepcopy(data), outputFile)
    # print(data['age'])

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])