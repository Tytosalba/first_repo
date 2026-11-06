# This code creates a dictionary for the 50 states and their capitals, then quizzes the user on them.

import random
capitals = {'alabama': 'montgomery',
    'alaska': 'juneau',
    'arizona': 'phoenix',
    'arkansas': 'little rock',
    'california': 'sacramento',
    'colorado': 'denver',
    'conneticut': 'heartford',
    'delaware': 'dover',
    'florida': 'tallahassee',
    'georgia': 'atlanta',
    'hawaii': 'honolulu',
    'idaho': 'boise',
    'illinois': 'springfield',
    'indiana': 'indianapolis',
    'iowa': 'des moines',
    'kansas': 'topeka',
    'kentucky': 'frankfort',
    'louisiana': 'baton rouge',
    'maine': 'augusta',
    'maryland': 'annapolis',
    'massachusetts': 'boston',
    'michigan': 'lansing',
    'minnesota': 'saint paul',
    'mississippi': 'jackson',
    'missouri': 'jefferson city',
    'montana': 'helena',
    'nebraska': 'lincoln',
    'nevada': 'carson city',
    'new hampshire': 'concord',
    'new jersey': 'trenton',
    'new mexico': 'santa fe',
    'new york': 'albany',
    'north carolina': 'raleigh',
    'north dakota': 'bismarck',
    'ohio': 'columbus',
    'oklahoma': 'oklahoma city',
    'oregon': 'salem',
    'pennsylvania': 'harrisburg',
    'rhode island': 'providence',
    'south carolina': 'columbia',
    'south dakota': 'pierre',
    'tennessee': 'nashville',
    'texas': 'austin',
    'utah': 'salt lake city',
    'vermont': 'montpelier',
    'virginia': 'richmond',
    'washington': 'olympia',
    'west virginia': 'charleston',
    'wisconsin': 'madison',
    'wyoming': 'cheyenne'}
# Quiz
def main():
    correct = 0
    incorrect = 0

    print('State Capitals quiz. Type quit to stop.')

    states = tuple(capitals)
    result = ''
    

    while True:
        state = random.choice(states)
        ans = input(f'{result}{state.title()}? ').lower()
        if ans in ('quit', 'stop'):
            break
        if ans == capitals[state]:
            correct += 1
            print("Correct")
        else:
            incorrect += 1
            print("Incorrect")
           
    print("\nYou have",correct,"correct answers")
    print("\nYou have",incorrect,"incorrect answers")
    
main()