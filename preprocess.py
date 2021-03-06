import numpy
import sys
import pandas as pd

encoderDict = {}

def encoder(pd_series):
    # More information here https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.categories.html easier that pandas.factorize
    encoding = {}
    name = pd_series.name
    count = 0
    for category in pd_series.cat.categories:
        encoding[category] = count
        count += 1
    
    encoderDict[name] = encoding
    return pd_series.cat.codes

def read_dataset(fromFile, toFile):
    """ The format of values in some columns of the dataset is not unified. Strip the surrounding
        quotes in the values for columns race, race_o and field (e.g., ‘Asian/Pacific Islander/AsianAmerican’ → Asian/Pacific Islander/Asian-American), count how many cells are changed
        after this pre-processing step, and output this number.
     Expected output line: Quotes removed from [count-of-changed-cells] cells. 0 indexed 
     race - col3
     race_o - col4
     field - col8
    """
    number_of_quotes = 0
    data = pd.read_csv(fromFile)
    race = data['race']
    race_o = data['race_o']
    field = data['field']
    # print(race.head())
    # print(race_o.head())
    # print(field.head())

    # using regex to remove quotes

    number_of_quotes += race.str.count("\'.*\'").sum()
    data['race'] = race.str.strip('\'')

    number_of_quotes += race_o.str.count("\'.*\'").sum()
    data['race_o'] = race_o.str.strip('\'')

    number_of_quotes += field.str.count("\'.*\'").sum()
    data['field'] = field.str.strip('\'')
    
    print ('Quotes removed from %s cells' %number_of_quotes)

    """ Convert all the values in the column field to lowercase if they are not already in lowercases
        (e.g., Law → law). Count the number of cells that are changed after this pre-processing step,
        and output this number.
            Expected output line: Standardized [count-of-changed-cells] cells to lower case. 
    """

    number_of_lowercase_conversions = 0
    
    # Needs to be purely lowercase, so subtracting from total if even 1 char is not lower case.
    # This is done by subtracting all PURE lowercase words
    number_of_lowercase_conversions += len(data) - data['field'].str.islower().sum()
    data['field'] = data['field'].str.lower()
    print("Standardized %s cells to lower case"%(number_of_lowercase_conversions))

    """ 
    Use label encoding to convert the categorical values in columns gender, race, race_o and
    field to numeric values start from 0. The process of label encoding works by mapping
    each categorical value of an attribute to an integer number between 0 and nvalues − 1 where
    nvalues is the number of distinct values for that attribute. Sort the values of each categorical
    attribute lexicographically/alphabetically before you start the encoding process. You
    are then asked to output the mapped numeric values for ‘male’ in the gender column, for
    ‘European/Caucasian-American’ in the race column, for ‘Latino/Hispanic American’ in the
    race o column, and for ‘law’ in the field column.
        Expected output lines:
            Value assigned for male in column gender: [value-for-male].  
            Value assigned for European/Caucasian-American in column race: [valuefor-European/Caucasian-American].
            Value assigned for Latino/Hispanic American in column race_o: [value-forLatino/Hispanic American].
            Value assigned for law in column field: [value-for-law].
            2 values for gender - assigning female as 0 male as 1
            5 values for race
            5 values for race_o
            209 values for field

    """
    data['gender'] = encoder(data['gender'].astype('category'))
    data['race'] = encoder(data['race'].astype('category'))
    data['race_o'] = encoder(data['race_o'].astype('category'))
    data['field'] = encoder(data['field'].astype('category'))
    # import pdb; pdb.set_trace()

    print("Value assigned for male in column gender: %s"% encoderDict['gender']['male'])
    print("Value assigned for European/Caucasian-American in column race: %s"% encoderDict['race']['European/Caucasian-American'])
    print("Value assigned for Latino/Hispanic American in column race_o: %s"% encoderDict['race_o']['Latino/Hispanic American'])
    print("Value assigned for law in column field: %s"% encoderDict['field']['law'])

    """ 
    Normalization: As the speed dating experiments are conducted in several different batches,
    the instructions participants received across different batches vary slightly. For example, in
    some batches of experiments participants are asked to allocate a total of 100 points among the
    six attributes (i.e., attractiveness, sincerity, intelligence, fun, ambition, shared interests) to
    indicate how much they value each of these attributes in their romantic partner—that is, the
    values in preference scores of participant columns of a row should sum up to 100 (similarly,
    values in preference scores of partner columns of a row should also sum up to 100)—while in
    some other batches of experiments, participants are not explicitly instructed to do so.
    To deal with this problem, let’s conduct one more pre-process step for values in preference scores of participant and preference scores of partner columns. For each row, let’s first
    sum up all the values in the six columns that belong to the set preference scores of participant
    (denote the sum value as total), and then transform the value for each column in the set preference scores of participant in that row as follows: new value=old value/total. We then conduct
    similar transformation for values in the set preference scores of partner.
    Finally, you are asked to output the mean values for each column in these two sets after
    the transformation.
        Expected output lines: (All 6 attrs of both kinds so total of 12)
            Mean of attractive important: [mean-rounded-to-2-digits].
            Mean of shared interests important: [mean-rounded-to-2-digits].
            Mean of pref o attractive: [mean-rounded-to-2-digits].
            ...
            Mean of pref o shared interests: [mean-rounded-to-2-digits].
    """
    importance = ['attractive_important', 'sincere_important', 'intelligence_important', 'funny_important', 'ambition_important', 'shared_interests_important']
    partner_metrics = ['pref_o_attractive','pref_o_sincere','pref_o_intelligence','pref_o_funny','pref_o_ambitious','pref_o_shared_interests']

    sum_importance = 0
    for i in importance:
        sum_importance += data[i]
    sum_partner_metrics = 0
    for i in partner_metrics:
        sum_partner_metrics += data[i]
    
    # most sum up to 100 but not all, divding all by the sum so % will be the same.

    for i in range(len(importance)):
        # both importance and partner_metrics are of length 6
        data[importance[i]] = data[importance[i]]/sum_importance
        data[partner_metrics[i]] = data[partner_metrics[i]]/sum_partner_metrics

    sum_importance_arr = []
    for i in importance:
        sum_importance_arr.append(data[i].sum())
    sum_partner_metrics_arr = []
    for i in partner_metrics:
        sum_partner_metrics_arr.append(data[i].sum())

    size = len(data)
    # Finding the mean value of these params. Take sum of the entire column at once and then divide by length
    for i in range(6):
        print ('Mean of %s : %s' %(importance[i],round(sum_importance_arr[i]/size, 2)))
    for i in range(6): 
        print ('Mean of %s : %s' %(partner_metrics[i],round(sum_partner_metrics_arr[i]/size, 2)))

    # Writing preprocessed data to dating.csv To prevent first column of serial numbers, using index = False
    data.to_csv(toFile, index = False, mode = 'w')


if __name__ == '__main__':
    read_dataset(sys.argv[1], sys.argv[2])