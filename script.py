import codecademylib
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']


'''Calculate the number of people who answered 'Ceballos' and save the answer to the variable total_ceballos. plusieurs moyens de calculer : avec '.count' ou en important une librairie.    ''' 
total_ceballos = Counter(survey_responses)
#print total_ceballos
total_ceballos = survey_responses.count('Ceballos')
print total_ceballos

survey_length = len (survey_responses)
#print (survey_length)
'''Calculate the percentage of people in the survey who voted for Ceballos and save it to the variable percentage_ceballos.'''
percentage_ceballos = 100 * total_ceballos/ survey_length
print percentage_ceballos

'''They want you to determine if there is something wrong with the poll or if given the sample size, it was an entirely reasonable result.'''
possible_surveys = np.random.binomial(70, 0.54, 10000)/70.
plt.hist(possible_surveys, range = (0,1), bins = 20)
plt.show()
'''As we saw, 47% of people we surveyed said they would vote for Ceballos, but 54% of people voted for Ceballos in the actual election. Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote'''
ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print ceballos_loss_surveys

'''With this current poll, about 20% of the time a survey output would predict Kerrigan winning, even if Ceballos won the actual election.Your co-worker points out that your poll would be more accurate if it had more responders.'''
large_survey = np.random.binomial(7000, 0.54, 10000)/7000.
ceballos_loss_new = 100 * total_ceballos / 7000
print ceballos_loss_new
plt.hist(large_survey, alpha = 0.5, range = (0,1))
plt.show()
