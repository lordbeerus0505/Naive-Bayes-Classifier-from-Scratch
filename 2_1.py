""" Visualizing interesting trends in data """
import pandas as pd
import numpy

""" 
        First, let’s explore how males and females differ in terms of what are the attributes they value
        the most in their romantic partners. Please perform the following task on dating.csv and
        include your visualization code in a file named 2 1.py.
""" 
def part_a(dataframe):
    
    """ (a)  Divide the dataset into two sub-datasets by the gender of participant """
    grouped = dataframe.groupby(['gender'])
    female, male = [grouped.get_group(x) for x in grouped.groups]

    return female, male

def part_b(dataframe):
    """ (b) Within each sub-dataset, compute the mean values for each column in the set preference scores of participant """
    preference_scores_of_participant =  ['attractive_important', 'sincere_important', 'intelligence_important', 'funny_important', 'ambition_important', 'shared_interests_important']
    mean_arr = []
    size = len(dataframe)
    for i in preference_scores_of_participant:
        mean_arr.append(dataframe[i].sum()/size)
    return mean_arr

def part_c(male_avg, female_avg):
    """ (c) Use a single barplot to contrast how females and males value the six attributes in their
        romantic partners differently. Please use color of the bars to indicate gender.   
    """
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    red_patch = mpatches.Patch(color='red', label='male')
    green_patch = mpatches.Patch(color='green', label='female')
    colors = {'male':'red', 'female':'green'}
    # c = data['Type'].apply(lambda x: colors[x])
    fig = plt.figure()
    fig.set_figwidth(7)
    fig.set_figheight(7)
    fig.subplots_adjust(bottom=0.3)
    preference_scores_of_participant =  ['attractive_important', 'sincere_important', 'intelligence_important', 'funny_important', 'ambition_important', 'shared_interests_important']
    male_plot = plt.bar([1,4,7,10,13,16], male_avg, color=colors['male'])
    female_plot = plt.bar([2,5,8,11,14,17], female_avg, color = colors['female'])
    plt.xlabel('Attributes')
    plt.ylabel('Average Scores')
    plt.title('Attribute preferences for male and female')
    plt.legend(handles=[red_patch, green_patch])
    # rotating axis of ticks as visibility is an issue
    plt.xticks([1.5,4.5,7.5,10.5,13.5,16.5], (preference_scores_of_participant[i] for i in range(len(preference_scores_of_participant))), rotation = 60)
    # directly using range fails hence using numpy arange plt.yticks([x for x in range(0,0.3,0.01)])
    plt.yticks(numpy.arange(0, 0.3, 0.01))
    plt.savefig('2_1barplot.jpg')
    plt.show()

def main():
    data = pd.read_csv('dating.csv')
    female, male = part_a(data)
    male_avg = part_b(male)
    female_avg = part_b(female)
    # print(male_avg, female_avg)
    part_c(male_avg, female_avg)
main()