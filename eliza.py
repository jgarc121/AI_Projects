#!/usr/bin/env python3
# # -*- coding: utf-8 -*- """ Eliza chatbox bot """
__author__ = "Jose Garcia"

import random
import re

moodQuestions = ['How are you feeling today?', 'How is your day going so far?', 'How was your weekend?',
                 'What is your current mood?']

relationshipQuestions = ['How old is your ', 'When is the last time you talked to your ',
                         'When are going to visit your ']

about_mood = ['Why are you feeling ', 'What is making you feel ', 'Tell me more, why you are feeling ']

verb_response = ['Do you love to ', 'When do you ', 'What is ', 'Can you explain ', 'Can you ', 'Would you ',
                 'Can I give you a ', 'How was the ']
vowel = ['a', 'e', 'i', 'o', 'u']
all_questions = [moodQuestions, relationshipQuestions, about_mood, verb_response]


def is_bye(text):
    bye = re.match(r'.*bye.*', text, re.I)
    return bye is not None


# checks mood
def user_mood(text):
    mood = re.match(r'.*(sad|mad|happy|joyful|good|bad|lovely|amazing).*', text, re.I)
    if mood is not None:
        return all_questions[2][random.randint(0, len(all_questions[2]) - 1)] + mood.group(1).lower() + "?"


# checks relationship
def relationship(text):
    relation = re.match(r'.*(mother|mom|father|dad|brother|sister|friend|aunt|uncle|grandpa|grandfather).*', text, re.I)
    if relation is not None:
        family_member = relation.group(1)
        return all_questions[1][random.randint(0, len(all_questions[1]) - 1)] + relation.group(1).lower() + "?"


# checks to see if a the text being passed in is a vowel
def check_vowel(text):
    for i in vowel:
        if i == text:
            return True
    return False


# finds the ing verb and changes it accordingly
def verbs(text):
    verb = re.search(r'\w*(?<!th)ing\b', text, flags=re.I)
    if verb:
        verb = verb.group().lower()
        # gets rid of the ING
        verb = verb[0:-3]
        # last three chars in the verb
        lastThreeChars = verb[-3:]
        # checks to see if ends in any of these letters
        if verb[-2:] == 'ee' or verb[-2:] == 'ye' or verb[-2:] == 'oe':
            return all_questions[3][random.randint(0, 1)] + verb + '?'
        # checks to see if it ends in the format vowel - l - l
        elif check_vowel(lastThreeChars[0]) and lastThreeChars[1] == 'l' and lastThreeChars[2] == 'l':
            # gets rid of the last letter in the verb
            verb = verb[:-1]
            return all_questions[3][random.randint(2, 3)] + verb + '?'
        # checks to see if it ends in the format vowel - constant - constant
        elif check_vowel(lastThreeChars[0]) and not check_vowel(lastThreeChars[1]) and not check_vowel(
                lastThreeChars[2]):
            verb = verb[:-1]
            return all_questions[3][random.randint(4, 5)] + verb + '?'
        # checks to see if ends in the format vowel - vowel - constant
        elif check_vowel(verb[0]) and check_vowel(verb[1]) and not check_vowel(verb[2]):
            return all_questions[3][6] + verb + '?'
        # checks to see if the second to last char is 'c' and last char is 'k'
        elif lastThreeChars[1] == 'c' and lastThreeChars[2] == 'k':
            verb = verb[:-1]
            return all_questions[3][7] + verb + '?'
        else:
            return all_questions[3][random.randint(0, 7)] + verb + '?'


# outputs random mood question
def random_question():
    return moodQuestions[random.randint(0, len(moodQuestions) - 1)]


def dialogue():
    done = False
    print('Welcome, what is your name?')
    user = input()
    done = is_bye(user)
    if not done:
        print('Hello, ' + user + '.')
        print(moodQuestions[random.randint(0, len(moodQuestions) - 1)])
        user_input = input()
        done = is_bye(user_input)
    while not done:
        if user_mood(user_input) is not None:
            print(user_mood(user_input))

        elif relationship(user_input) is not None:
            print(relationship(user_input))

        elif verbs(user_input) is not None:
            print(verbs(user_input))

        else:
            print(random_question())

        user_input = input()
        done = is_bye(user_input)


if __name__ == "__main__":
    dialogue()
