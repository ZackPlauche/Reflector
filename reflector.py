# Reflector/reflector.py

'''Reflector is an app that allows it's user to walk through useful thought processes using high-quality questions from different success resources.

"Everytime I use this app, it feels like coming home."

'''

# -*- coding: utf-8 -*-
import time
import os
from activities import MainActivities
from answerlogic import smart_choice


class Reflector(MainActivities):
    '''Reflector(activity=None)
    '''

    def __init__(self, activity=None):
        self.activity = activity


    def intro(self):
        '''Introduction to the program.'''
        print('\nWelcome to Reflector!')
        print('\nPlease choose an activity.\n')

    def selector(self):
        '''
    Lists the activities a user can select, predefined by the coder.
        '''

        if self.activity:
            choice = self.activity

        else:

            activity_list = [
                'Morning Reflection',
                'End of Day Reflection',
                'Weekly Reflection',
                'Birthday Reflection',
                'Acclaim System',
                'Prismatic System',
                '10 Ideas',
                'Goals',
                'Priorities',
                'Physiology Check',
            ]

        choice = smart_choice(activity_list)

        # Begin timer
        starttimer = time.time()

        # Run activites based on choice
        if choice == '10 Ideas':
            self.ten_ideas()
        elif choice == 'Acclaim System':
            self.acclaim_system()
        elif choice == 'Breather':
            self.breather()
        elif choice == 'Birthday Reflection':
            self.birthday_reflection()
        elif choice == 'Dave Asprey\'s Gratitude Questions':
            self.dave_asprey()
        elif choice == 'End of Day Reflection':
            self.end_of_day_reflection()
        elif choice == 'Gratitude List':
            self.gratitude()
        elif choice == 'Morning Reflection':
            self.morning_reflection()
        elif choice == 'Prismatic System':
            self.prismatic_system()
        elif choice == 'The One Thing':
            self.the_one_thing()
        elif choice == 'Tony Robin\'s Power Questions':
            self.power_questions()
        elif choice == 'Goals':
            self.goals()
        elif choice == 'Priorities':
            self.priorities('daily', write_checklist=True)
        elif choice == 'Physiology Check':
            self.physiology_check()
        elif choice == 'Lessons':
            self.lessons()
        elif choice == 'Weekly Reflection':
            self.weekly_reflection()

        # End Timer
        total_time = round(time.time() - starttimer)
        print(f'Your reflection took {total_time} seconds.')
        os.system('pause')

reflector = Reflector()


def main():
    '''This function executes the code.'''
    reflector.intro()
    while True:
        reflector.selector()
        play_again = input('\n Would you like to do something else? (y/n): ')
        print()
        if play_again == 'n':
            break
        elif play_again == 'y':
            pass
        elif play_again != 'n' or play_again != 'y':
            print('Answer not valid.')

if __name__ == '__main__':
    main()