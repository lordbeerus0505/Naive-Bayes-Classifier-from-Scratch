""" 
    Next, let’s explore how a participant’s rating to their partner on each of the six attributes
    relate to how likely he/she will decide to give the partner a second date. Please perform the
    following task on dating.csv and include your visualization code in a file named 2_2.py
"""
import pandas as pd
import numpy

def retrieve_success(data_frame):
    dating_success = data_frame[data_frame['decision'] == 1]
    return float(len(dating_success))/len(data_frame)

def part_a(data_frame):
    """ 
        (a) Given an attribute in the set rating_of_partner_from_participant (e.g., attractive partner),
        determine the number of distinct values for this attribute
    """
    number_of_distinct_values = []

    rating_of_partner_from_participant = ['attractive_partner','sincere_partner','intelligence_parter', 'funny_partner', 'ambition_partner', 'shared_interests_partner']

    for attr in rating_of_partner_from_participant:
        # retrieve unique values directly with pandas unique method
        number_of_distinct_values.append(data_frame[attr].unique())
    return number_of_distinct_values

def part_b_c(data_frame, number_of_distinct_values):
    """ 
        (b) Given a particular value for the chosen attribute (e.g., a value of 10 for attribute ‘attractive partner’), 
        compute the fraction of participants who decide to give the partner a second date among all participants whose
        rating of the partner on the chosen attribute (e.g., attractive partner) is the given value (e.g., 10). We refer
        to this probability as the success rate for the group of partners whose rating on the chosen attribute is the
        specified value.

        (c)Repeat the above process for all distinct values on each of the six attributes in the set
        rating of partner from participant.
    """
    rating_of_partner_from_participant = ['attractive_partner','sincere_partner','intelligence_parter', 'funny_partner', 'ambition_partner', 'shared_interests_partner']
    # if decision =1, then second date else no second date.
    success_rate_arr = []

    i=0
    for attr in rating_of_partner_from_participant:
        success_rate_single_attr = []
        for value in number_of_distinct_values[i]:
            success_rate_single_attr.append(retrieve_success(data_frame[data_frame[attr] == value]))
        success_rate_arr.append(success_rate_single_attr)
        i+=1
    # print(success_rate_arr)
    
    return success_rate_arr

def part_d(success_rate_arr, number_of_distinct_values):
    """ 
        (d) For each of the six attributes in the set rating_of_partner_from_participant, draw a scatter
        plot using the information computed above. Specifically, for the scatter plot of a particular 
        attribute (e.g., attractive partner), use x-axis to represent different values on that
        attribute and y-axis to represent the success rate. We expect 6 scatter plots in total.
    """
    import matplotlib.pyplot as plt
    # creating 6 scatter plots, one for each attribute
    # NOTE: intelligence_parter is the name in the dataset so using the same for consistency despite it not being the correct spelling
    rating_of_partner_from_participant = ['attractive_partner','sincere_partner','intelligence_parter', 'funny_partner', 'ambition_partner', 'shared_interests_partner']
   
    for i in range(len(rating_of_partner_from_participant)):
        fig = plt.figure()
        fig.set_figwidth(7)
        fig.set_figheight(7)
        # fig.subplots_adjust(bottom=0.1)
        plt.title('Scatter plot of '+ rating_of_partner_from_participant[i])
        plt.xlabel('Unique values ' + rating_of_partner_from_participant[i])
        plt.ylabel('Corresponding success rate')
        plt.yticks(numpy.arange(0,1.05,0.1))
        plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
        plt.scatter(number_of_distinct_values[i], success_rate_arr[i])
        # plt.show()
        plt.savefig('scatter_for_'+rating_of_partner_from_participant[i]+'.jpg')


def main():
    
    data = pd.read_csv('dating.csv')
    number_of_distinct_values = part_a(data)
    success_rate_arr = part_b_c(data, number_of_distinct_values)
    part_d(success_rate_arr, number_of_distinct_values)
main()