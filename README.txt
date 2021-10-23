Assignment by Abhiram Natarajan
PUID: 0033250677

Instructions to run code:
Requirements:
pip install numpy
pip install pandas
pip install matplotplib

Please add dating-full.csv to this list before running it.

Question 1: Execute question 1 this way, passing the filename of input and output.
python preprocess.py dating-full.csv dating.csv
Output comes up on the terminal as expected

Question 2:
python 2_1.py Creates the barplot image under the name 2_1barplot.jpg No arguments required
                This can be directly viewed in an image viewer, the same is present and explained in the report submitted.
python 2_2.py Creates the scatter plots, one for each of the 6 attributes specified. No arguments required.

Question 3:
python discretize.py dating.csv dating-binned.csv
Passing the input file and output file as arguments. Performs discrtization and output comes on terminal as expected.

Question 4:
python split.py
Splits data-binned data into trainingSet and testSet. No arguments required. The two files are written into csv with same names.

Question 5:
python 5_1.py
Returns the accuracy for train and test sets with bin size = 5 and t_frac = 1. No arguments required.
python 5_2.py
Returns the accuracies for each of the possible bin sizes from the list. No arguments required. Output graph
produced with the name 5_2comparisonPlot.jpg
python 5_3.py
Returns the accuracies for each possible fraction size from the list provided. No arguments required. Output graph
produced with the name 5_3comparisonPlot.jpg

Special Conditions:
1.  For binning, since the answers change based on how we handle interests_correlate field, two possible solutions exist -
[18, 758, 2520, 2875, 573] or [18, 713, 2498, 2883, 632]. As the assumption required is not stated in the question, I 
have gone ahead with the former.
2.  The dataset has an issue, for intelligence_partner, the column useed is instead intelligence_parter
3.  To handle 0 probability values, laplacian smoothing as done in class is used. Only if numerator is a 0
should we add 1 to numerator and k to denominator where k is the number of possible values the attribute can take. 