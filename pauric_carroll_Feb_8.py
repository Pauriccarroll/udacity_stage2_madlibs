# -*- coding: utf-8 -*-

# The following are the madlibs strings to pass in to the play_game function.

easy = '''
        Zlatan Ibrahimović born 3 October 1981) is a Swedish professional
        footballer who plays as a forward for Manchester United. He was also a
        member of the Sweden national team, making his senior international
        debut in 2001 and serving as captain from 2010 until he retired from
        international football in 2016
        '''

medium = '''
        Wayne Mark Rooney (/ˈruːni/; born 24 October 1985) is an English
        professional footballer who plays for and captains both Manchester
        United and the England national team. He has played much of his career
        as a forward, but he has also been used in various midfield roles.
        He is the highest goal scorer for Manchester United
        '''

hard = '''
        Ryan Joseph Giggs, OBE (né Wilson; born 29 November 1973)[3] is a Welsh
        football coach and former player who is the co-owner of Salford City.
        He played his entire professional career for Manchester United.
        '''

# Set up madlibs strings into a list
paragraphs = [easy, medium, hard]

# A list of replacement words from the madlibs to be passed in to the play
# game function.
input_list = [["October", "Swedish", "forward", "captain"],  # for easy
              ["English", "captain", "highest", "Mark"],  # for medium
              ["Joseph", "November", "Manchester", "Salford"]]  # for hard


# Prompt the user to choose a madlib level from the list until they choose a
# valid one.
def choose_level():
    '''
    This is my function that will select which string the user will answer
    questions with.
    '''
    level = raw_input("Enter your difficulty level (easy/medium/hard): ")

    if level == "easy":
        print "Easy level selected"
        return 0
    elif level == "medium":
        print "Medium level selected"
        return 1
    elif level == "hard":
        print "Hard level selected"
        return 2
    else:
        print "Invalid level selected"
        return choose_level()  # if the level is invalid, choose a level again,
        # and return that value


# Process the paragraph for the given level
def process_paragraph(level, blank):
    '''
    Replaces the words in input_list for the level, from the given blank.
    '''
    paragraph = paragraphs[level]

    # replace all the input_list from current blank to the last one
    while blank < len(input_list[level]):
        word_to_replace = input_list[level][blank]
        list_of_words = paragraph.split(" ")
        index = 0
        # Replace the word_to_replace with ___number___
        while index < len(list_of_words):
            if list_of_words[index] == word_to_replace:
                list_of_words[index] = "___" + str(blank + 1) + "___"
            index += 1

        blank += 1
        paragraph = " ".join(list_of_words)

    return paragraph


# play the game for the given level
def play_game(level):
    '''
    Plays a full game of mad_libs. A player is prompted to replace blanks in
    madlibs level with the correct words.
    '''
    blank = 0

    # while not all input_list are filled, keep asking to guess the input_list
    # until the correct word is provided
    while blank < len(input_list[level]):
        print process_paragraph(level, blank)

        question = "\nWhat should go in blank number " + str(blank + 1) + "?"
        answer = raw_input(question).lower()

        correct_answer = input_list[level][blank].lower()
        if correct_answer == answer:
            print "Correct!"
            blank += 1
        else:
            print "Try again!"

    print paragraphs[level]
    print "\n Well played, you're pretty awesome!"


# Take the steps to play the game, prompt to advance to the next level
# when a level is completed
def main():
    """
    Opening and closing ceremony of the game. Add a loop so that you can keep
    telling Madlibs without having to restart the program each time.
    """
    print "~~~ Welcome to Computer Programming Reverse-Mad-Libs ~~~"

    level = choose_level()

    while level < 3:
        play_game(level)

        # If we're at easy or medium, prompt to advance
        if level < 2:
            proceed = raw_input(
                    "Would you like to attempt a different level?(YES/NO)")
            if proceed == "YES":
                level += 1
            else:
                break
        else:
            break

    print " \n ~~~ Thanks for playing! ~~~ "


main()
