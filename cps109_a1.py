"""
'Who Wants to be a Millionaire' Game Show in Python by Arshdeep Sandhu
"""

# For this assignment, create a Python program to replicate the popular game show ‘Who Wants 
# to Be a Millionaire?’ For this, you will need a text file that contains 15 multiple choice questions. 
# Each line in the file should contain a question with the corresponding options and correct 
# answer on the same line, for a total of 15 lines. The program should read input from the file 
# using a function and show each question and the associated options one at a time to the user. 

# The user should then have the option to use one of three lifelines, continue answering the 
# question, or quit and leave with the amount they’ve won. The first lifeline is “Ask the Audience,” 
# where the options are presented with percentages representing what percentage of the 
# audience thinks each option is correct. The second lifeline is “50:50,” where two incorrect 
# answers are removed from the options. And the third lifeline is “Ask the Expert,” where an 
# expert helps answer the question. If they want to use a lifeline, then run the function for the 
# specific lifeline they choose, and eliminate that lifeline from the options since they cannot use it 
# twice. After the lifeline is used, they must answer the question.
# Take their input and compare it to the correct answer. If they get the answer wrong, 
# print “Sorry, that was the wrong answer” and print the amount they have won so far. If they get 
# the question right, increment their level by 1, increase their winnings, and print “Congratulations! 
# That was the right answer! You just won $ {winnings}!” If at any point they choose to quit, print 
# “You won a total of $ {winnings}! Thank you for playing ‘Who Wants to Be a Millionaire?’” and 
# exit the program. If they reach level 15 and get the right answer, print “Congratulations!!! You 
# just became a millionaire!!!” and exit the program. 


#importing necessary libraries
import random
import time


def get_questions(filename):
    """
    Function to open the file with the questions and return a list of lists with each inner list
    containing a question, the corresponding options, and the corresponding answer
    """
    
    with open(filename, 'r') as f:
        lines = f.readlines()       # Make a list of the lines in the file
        return [line.strip().split('/') for line in lines]  # Make a list for each line


def choices_after_question():
    """
    Function to present the choices the user has (if any lifelines are present)
    after being presented with the question and taking their input
    """
    # Print the user's options after getting the question if they have lifelines
    print('\n-------------------------------------------------------------------------\n'
          'Would you like to:\n'
          '   1: Answer the question?\n'
          '   2: Use a lifeline?\n'
          '   3: Or quit and walk away?\n'
          '-------------------------------------------------------------------------')
    while True:    # Run a while loop to ensure a valid input
        choice = input('Choose 1, 2, or 3: ')
        if choice not in ['1', '2', '3']:
            print('Input either 1, 2, or 3')
        else:
            return int(choice)  # Will only return something other than True when input is valid


def choices_no_lifes():
    """
    Function to present the choices the user has (if no lifelines are present)
    after being presented with the question and taking their input
    """
    # Print the user's options after getting the question if they have NO lifelines
    print('\n-------------------------------------------------------------------------\n'
          'Would you like to:\n'
          '   1: Answer the question?\n'
          '   3: Or quit and walk away?\n'
          '-------------------------------------------------------------------------')
    while True:    # Run a while loop to ensure a valid input
        choice = input('Choose 1 or 3: ')
        if choice not in ['1', '3']:
            print('Input either 1 or 3')
        else:
            return int(choice)  # Will only return something other than True when input is valid


def get_answer():
    """
    Function to get a valid answer from user
    """
    # Get a valid answer if user decides to answer question
    while True:     # Run a while loop to ensure a valid input
        ans = input('Your Answer: ')
        if ans not in ['a','A','b','B','c','C','d','D']:
            print('Please input a valid answer')
        else:
            return ans.lower()  # Will only return something other than True when input is valid


def are_you_sure():
    """
    Function to ask user if they're sure with their choice
    """
    # Loop to get a yes or no
    while True:     # Run a while loop to ensure a valid input
        decision = input('Are you sure? (Y/N): ')
        if decision not in ['y', 'Y', 'n', 'N']:    #Input must be a yes or no (y or n)
            print('Input either Y or N')
        else:
            return decision.lower() # Will only return something other than True when input is valid


def fifty_fifty(q):
    """
    Function to run the '50:50' lifeline
    """
    # 
    time.sleep(0.5)
    print("\nHost: 'Computer, can you please remove two wrong answers?'\n") # Simulated interaction with the host
    time.sleep(2)
    print('Your new options:')
    time.sleep(1)
    random1 = q[0][2]   # Save the answer into random1
    random2 = q[0][2]   # Save the answer into random2
    while random2 == q[0][2]:   # Run the loop until random2 is not the answer
        random2 = random.choice(['A','B','C','D'])
    for i in q[0][1].split(','):    # This for loop checks each option for the variables random1 and random2
        i = i.strip()               # and saves the entire string for the options in rstr1 and rstr2
        if i[0] == random1:
            rstr1 = i
        elif i[0] == random2:
            rstr2 = i
    if random1 < random2:       # This if-else ensures that the options are presented in alphabetical order
        print('   ' + rstr1)    # I.e. A must come before D in the options
        time.sleep(1)
        print('   ' + rstr2)
        time.sleep(1)
    else:
        print('   ' + rstr2)
        time.sleep(1)
        print('   ' + rstr1)
        time.sleep(1)
    print("\nHost: 'One of these is right and one of these is wrong'")
    time.sleep(2)
    print("Host: 'Which one would you like to choose?'\n")
    time.sleep(1)


def ask_expert(q):
    """
    Function to run the 'Ask the Expert' lifeline
    """
    # Simple function that prints a simulated interaction with the expert
    time.sleep(0.5)
    print("Expert: 'Hello there! It looks like you need my help with this question'")
    time.sleep(3)
    print("Expert: 'Let me read it and see how I can help!'")
    time.sleep(3)               # Time.sleep() used to delay the function and add the effect
    print("Expert: '...'")      # that someone is actually interacting with the user
    time.sleep(2)               # i.e. the expert takes time to think about the question
    print("Expert: '...'")      # rather than instantly giving the answer
    time.sleep(2)
    print("Expert: 'Oh yes, this is a very difficult question'")
    time.sleep(3)
    print("Expert: '...'")
    time.sleep(2)
    print("Expert: 'But I think the answer is...'")
    time.sleep(2)
    print("Expert: '...'")
    time.sleep(2)
    print("Expert: '...'")
    time.sleep(2)
    print("Expert: '...'")
    time.sleep(3)
    print("Expert: 'The answer is " + q[0][2] + "!'\n") # The expert ultimately gives the answer
    time.sleep(1)


def ask_audience(q):  
    """
    Function to run the 'Ask the Audience' lifeline
    """
    # This function simulates an audience poll using the module random
    percents = ['24%', '10%', '15%']    # Save percentages for wrong answers in percents
    op = ['A', 'B', 'C', 'D']    # Save the options in op
    random.shuffle(percents)    # Shuffle the order of the percentages
    
    for i in range(len(op)):        #Loop through the indexes of op
        if op[i] == q[0][2]:        
            op[i] = q[0][2] + ': 51%'       # If op[i] is the answer, then op[i] is the answer with its associated
        else:                               # percentage (51%). This ensures that the answer always has the higher percentage
            op[i] = op[i] + ': ' + percents[0]  # Else, op[i] is a random percentage
            percents.pop(0)     # Remove the added percentage to ensure it doesn't occur twice
 
    time.sleep(0.5)
    print("\nHost: 'Let's ask the audience what they think the right answer is!'") # Simulated interaction with the host
    time.sleep(2)
    print("Host: 'Audience, can you please use the keypads in front of you to input your answers?'")
    time.sleep(3)
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print("Host: 'And the results have come in'\n")
    time.sleep(2)
    print("Audience results:")
    
    for j in op:
        print('   ' + j.strip())    # Print the audience poll: the options with their associated percentages
    time.sleep(2)
    print("\nHost: 'Which one would you like to choose?'\n")
    time.sleep(1)


def wwtbam():
    """
    Main function to run the WWTBAM game
    """
    # Print welcome string
    print('\n\n=========================================================================')
    time.sleep(0.5)
    print('=========================================================================\n')
    time.sleep(0.5)
    print("                Welcome to 'Who Wants to be a Millionaire!'\n")
    time.sleep(0.5)
    print('=========================================================================')
    time.sleep(0.5)
    print('=========================================================================\n\n')
    time.sleep(2)
    
    level = 0   # Initialize level to be zero
    level_dict = {1:'$ 100', 2: '$ 200', 3: '$ 300', 4: '$ 500', 5: '$ 1,000',   # Dictionary with keys as levels and values
              6: '$ 2,000', 7: '$ 4,000', 8: '$ 8,000', 9: '$ 16,000',           # as the earnings at each level
              10: '$ 32,000', 11: '$ 64,000', 12: '$ 125,000', 13: '$ 250,000', 
              14: '$ 500,000', 15: '$ 1,000,000'}
    
    file = open("cps109_a1_output.txt", 'w')   # Open the file to write output to
    file.write(f"Game Winnings:\n")
    q = get_questions('questions.txt')  # Save the list of lists for each question into a variable
    
    esc = False         # Initializing flags
    audience = True     # Audience, fifty, and expert flags are flags to keep track of which lifelines have been used
    fifty = True        # Initially, none have been used so they're all True
    expert = True
    
    while not esc:      # Run loop while esc is False. This loop will run as long as they get the right answer
                        # This loop will break if they get the wrong answer or if they win the game
        print('\n\n\n=========================================================================\n'
              + q[0][0] + '\n'      # Print the first question
              '=========================================================================')
        time.sleep(2)
        for i in q[0][1].split(','):        # Print each option for the question using a for loop
            print('   ' + i.strip())
            time.sleep(1)
        print('=========================================================================')
        time.sleep(1)
        
        if not audience and not fifty and not expert:   # Presenting the options that the user has after showing them the question
            ch = choices_no_lifes()                     # If no lifeline is available, the options won't include the lifelines
        else:
            ch = choices_after_question()       # Otherwise, the user is able to choose any option
        
        
        decision = are_you_sure()       # Asks if they're sure
        while decision == 'n':      # While they're not sure, program presents the options again and asks if they're sure again
            if not audience and not fifty and not expert:
                ch = choices_no_lifes()
            else:
                ch = choices_after_question()
            decision = are_you_sure()
        
        
        if ch == 3:         # If they chose 3, they chose to quit, and print message depending on their level
            if level == 0:
                file.write("Quit at level: 1 - Total winnings: $ 0")    # Writes output to file
                print('\n=========================================================================')
                time.sleep(0.5)
                print("                    Sorry, you didn't win anything today")
                time.sleep(1)
                print('=========================================================================\n\n')
                time.sleep(1)
            else:
                file.write(f"Quit at level: {level+1} - Total winnings: {winnings}")    # Writes output to file
                print('\n=========================================================================')
                time.sleep(0.5)
                print(f"                   You won a total of {winnings} today!")
                time.sleep(1)
                print('=========================================================================\n\n')
                time.sleep(1)
            esc = True      # esc = True breaks the while loop so that the game can end
        
        if ch == 2:     # If they chose to use a lifeline, present them with options depending on how many lifelines are available
            if audience and fifty and expert:   # If all 3 are available, present them with all 3
                life = input('\n-------------------------------------------------------------------------\n'
                             'Which lifeline would you like to use:\n'
                             '   1: Ask the Audience\n'
                             '   2: 50:50\n'
                             '   3: Ask the Expert\n'
                             '-------------------------------------------------------------------------\n'
                             'Choose 1, 2, or 3: ')
                
                if life not in ['1', '2', '3']: 
                    flag = False
                    while not flag: # While loop using flag to ensure a valid input
                            life = input('Input either 1, 2, or 3: ')
                            if life in ['1', '2', '3']: # The loop will run until they input a valid answer and the
                                flag = True             # flag is True, otherwise the flag will remain False
                                
                if int(life) == 1:      # Once a certain lifeline is chosen, the program runs it, then changes its flag
                    ask_audience(q)     # to False since they cannot use it twice
                    audience = False
                    ch = 1              # ch = 1 so that the user can answer the question 
                elif int(life) == 2:
                    fifty_fifty(q)
                    fifty = False
                    ch = 1
                else:
                    ask_expert(q)
                    expert = False
                    ch = 1
            
            elif not audience and fifty and expert: # If only two are available, present only the ones that have flags equal to True
                life = input('\n-------------------------------------------------------------------------\n'
                             'Which lifeline would you like to use:\n'
                             '   1: 50:50\n'
                             '   2: Ask the Expert\n'
                             '-------------------------------------------------------------------------\n'
                             'Choose 1 or 2: ')
                if life not in ['1', '2']:
                    flag = False
                    while not flag:     # While loop using flag to ensure a valid input
                            life = input('Input either 1 or 2: ')
                            if life in ['1', '2']:
                                flag = True
                
                if int(life) == 1:      # Once a certain lifeline is chosen, the program runs it, then changes its flag
                    fifty_fifty(q)      # to False since they cannot use it twice
                    fifty = False
                    ch = 1              # ch = 1 so that the user can answer the question 
                else:
                    ask_expert(q)
                    expert = False
                    ch = 1
            
            elif audience and not fifty and expert:
                life = input('\n-------------------------------------------------------------------------\n'
                             'Which lifeline would you like to use:\n'
                             '   1: Ask the Audience\n'
                             '   2: Ask the Expert\n'
                             '-------------------------------------------------------------------------\n'
                             'Choose 1 or 2: ')
                if life not in ['1', '2']:
                    flag = False
                    while not flag:
                            life = input('Input either 1 or 2: ')
                            if life in ['1', '2']:
                                flag = True
                
                if int(life) == 1:
                    ask_audience(q)
                    audience = False
                    ch = 1
                else:
                    ask_expert(q)
                    expert = False
                    ch = 1
            
            elif audience and fifty and not expert:
                life = input('\n-------------------------------------------------------------------------\n'
                             'Which lifeline would you like to use:\n'
                             '   1: Ask the Audience\n'
                             '   2: 50:50\n'
                             '-------------------------------------------------------------------------\n'
                             'Choose 1 or 2: ')
                if life not in ['1', '2']:
                    flag = False
                    while not flag:
                            life = input('Input either 1 or 2: ')
                            if life in ['1', '2']:
                                flag = True
                
                if int(life) == 1:
                    ask_audience(q)
                    audience = False
                    ch = 1
                else:
                    fifty_fifty(q)
                    fifty = False
                    ch = 1
            
            elif audience:          # If all three or two are not available, then only one is available. This block of code 
                time.sleep(0.5)     # checks which one is available and runs the corresponding lifeline function
                life = input('\n-------------------------------------------------------------------------\n'
                             'You have one lifeline left:\n'
                             '   1. Ask the Audience\n'         # The user does not have to choose which one, the lifeline function will by itself
                             '-------------------------------------------------------------------------\n')
                ask_audience(q)     # Once a certain lifeline is chosen, the program runs it, then changes its flag
                audience = False    # to False since they cannot use it twice
                ch = 1              # ch = 1 so that the user can answer the question 
            
            elif fifty:
                time.sleep(0.5)
                print('\n-------------------------------------------------------------------------\n'
                      'You have one lifeline left:\n'
                      '   1. 50:50\n'
                      '-------------------------------------------------------------------------\n')
                fifty_fifty(q)
                fifty = False
                ch = 1
            
            elif expert:
                time.sleep(0.5)
                print('\n-------------------------------------------------------------------------\n'
                      'You have one lifeline left:\n'
                      '   1. Ask the Expert\n'
                      '-------------------------------------------------------------------------\n')
                ask_expert(q)
                expert = False
                ch = 1
        
        if ch == 1: # If the user chose 1 or ch == 1, user must input an answer to the question
            answer = get_answer() # Get an answer from the user using get_answer() function
            if answer == q[0][2].lower():   # Checks if user's answer is same as the actual answer
                level += 1                          # If user is correct, they move on to the next level
                winnings = level_dict[level]        # and their winnings increase
                file.write(f"Level: {level} - Winnings: {winnings}\n")  # Write the level and the winnings to the file
                if level == 15:     # If they are at level 15, they have won $1,000,000. Program ends game after this
                    file.write(f"Congratulations!!! You won {winnings}!\nYou won 'Who Wants to be a Millionaire'!")
                    print('\n=========================================================================')
                    time.sleep(2)
                    print(f'              CONGRATULATIONS!!! YOU JUST WON {winnings}!!!')
                    time.sleep(2)
                    print("                YOU WON 'WHO WANTS TO BE A MILLIONAIRE'!!!")
                    time.sleep(2)
                    print('=========================================================================\n\n')
                    time.sleep(3)
                    esc = True      # Escape the while loop and end game
                else:   # If level is not 15, print out congratulations message
                    print('\n=========================================================================')
                    time.sleep(0.5)
                    print('               Congratulations! That was the right answer!')
                    time.sleep(1)
                    print(f'                          You just won {winnings}!')
                    time.sleep(1)
                    print('=========================================================================\n\n')
                    time.sleep(1)
            else:       # If answer was incorrect, run this block of code
                if level == 0:
                    file.write("Incorrect input at level: 1 - Total winnings: $ 0") # Writes output to file
                    print('\n=========================================================================')
                    time.sleep(0.5)
                    print('                      Sorry, that was the wrong answer')
                    time.sleep(1)
                    print(f'                         The correct answer was {q[0][2].upper()}')
                    time.sleep(1)
                    print("                       You didn't win anything today")
                    time.sleep(1)
                    print('=========================================================================\n\n')
                    time.sleep(1)
                else:
                    file.write(f"Incorrect input at level: {level+1} - Total winnings: {winnings}") # Writes output to file
                    print('\n=========================================================================')
                    time.sleep(0.5)
                    print('                      Sorry, that was the wrong answer')
                    time.sleep(1)
                    print(f'                         The correct answer was {q[0][2].upper()}')
                    time.sleep(1)
                    print(f'                    You won a total of {winnings} today!')
                    time.sleep(1)
                    print('=========================================================================\n\n')
                    time.sleep(1)
                esc = True      # Escape the while loop and end game
        
        q = q[1:]   # At the end of the loop, remove first question using list slicing and repeat the loop until esc == True
    
    file.close()    # Close the output file

    print('\n\n\n=========================================================================') # Print closing message
    time.sleep(0.5)
    print('=========================================================================\n')
    time.sleep(0.5)
    print("          Thank you for playing 'Who Wants to Be a Millionaire'!")
    time.sleep(0.5)
    print('                       We hope to see you again!\n')
    time.sleep(0.5)
    print('=========================================================================')
    time.sleep(0.5)
    print('=========================================================================')
    time.sleep(0.5)

if __name__ == "__main__":      # Calling the main function to start the game
    wwtbam()
    



