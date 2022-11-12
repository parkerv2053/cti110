#CTI-110
#P4HW1 - Score List
#Victor Parker
#12 November
#


Num_scores = int(input('How many scores do you want to enter?'))  #Begining of variables
score_question = int(0)
scores = []

#Looping the question to add 1 each time around, took me 2 hours to fix the bugs on this part
while score_question < Num_scores:
    score_question += 1
    print(f'Enter score #{score_question}:')
    enter_score = int(input())
    if (0 <= enter_score <= 100):
        scores.append(float(enter_score))
    else: #repeating the quetion while not adding an extra number to the overall loop
        print('\nINVALID Score entered!!!!\nScore should be between 0 and 100')
        print(f'Enter score #{score_question} again:')
        enter_score = int(input())    
        scores.append(float(enter_score))
else: #create space for the results and end the loop
    print('\n')
    
lowest = float(min(scores)) #low=(lowest_score from {scores})

scores.sort() #score = place_in_order{scores} 
scores.remove(lowest) #take_out = lowest
mean = float((sum(scores) / len(scores))) #average = total_scores/ Number_in_list

if mean >= 90: #grading scale
    grade = 'A'
elif mean >= 80:
    grade = 'B'
elif mean >= 70:
    grade = 'C'
elif mean >= 60:
    grade = 'D'
else:
    grade = 'F'
#the final results
print('-------------Results-------------')
print(f'Lowest Score  :  {lowest:.1f}')
print(f'Modified List :  {scores}')
print(f'Scores Average:  {mean:.2f}')
print(f'Grade         :  {grade}')
print('----------------------------------')
