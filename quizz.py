import time

# Define messages used throughout the quiz
dmessages = {
    'title': "\n*** Welcome to the Ultimate Knowledge Quizz! ***",
    'welcome': "\nGet ready to test your knowledge and have some fun!",
    'intro': "\nYou have 3 lives. Answer carefully, and good luck!",
    'validate': '* Correct answer! *',
    'invalidate': '* Oops! Try again. *',
    'lifecount': 'Remaining lives:',
    'errorcatch': 'Invalid input, please enter a number.',
    'congratulate': '\n*** Congratulations, you won the quizz! ***',
    'loose': '\nYou lost! Better luck next time!',
    'stop': '\nQuizz interrupted by the user. Goodbye!'
}

# List of questions with multiple-choice options and correct answers
lquestions = [
    [
        {'options': ['Elon Musk', 'Larry Page', 'Mark Zuckerberg']},
        {'question': 'Which CEO dances frenetically with Donald Trump? '},
        {'answer': '0'}
    ],
    [
        {'options': ['Pi', 'Obi Wan Kenobi', '42']},
        {'question': 'What is the answer to the great question about the origin of the Universe? '},
        {'answer': '2'}
    ],
    [
        {'options': ['Yes', 'No', 'Can you repeat the question?']},
        {'question': 'Is scribe a good career choice? '},
        {'answer': '1'}
    ],
    [
        {'options': ['Blue', 'White', 'Red']},
        {'question': 'What is the color of Henri IV’s white horse? '},
        {'answer': '1'}
    ]
]

# Initial number of lives for the player
NB_OF_INITIAL_LIVES = 3 #number of lives given to the user

def display_intro():
    """
    Displays the intro message for the quiz.
    """
    print('Coucou')
    print(dmessages['title'])
    time.sleep(1)
    print(dmessages['welcome'])
    time.sleep(1)
    print(dmessages['intro'])
    time.sleep(1)
    print("\nLet's get started!\n")
    time.sleep(1)

def ask_question(lives, question_index):
  """
    Displays a question with multiple-choice options, checks user's answer, and adjusts lives based on correctness.

    Args:
        lives (int): The current number of lives remaining for the user.
        num (int): The index of the current question in the list.

    Returns:
        int: The updated number of lives after the question is attempted.
  """
  while lives > 0:
    # Display the multiple-choice options
    for i, option in enumerate(lquestions[question_index][0]['options']):
        # Format multiple choices lines as : i. CHOICE_OPTION_NB_i (i+1 because list index begins with 0)
        print(f"{i + 1}. {option}")

    # Display the question prompt
    question = lquestions[question_index][1]['question']
    try:
        input_str = input(f'{question}')
        answer_num = lquestions[question_index][2]['answer']
        answer_str = lquestions[question_index][0]['options'][int(answer_num)]

        # Check if user input matches the correct answer (by number or text)
        if str(int(input_str) - 1) == answer_num:
            print(dmessages['validate'])
            print(f"{dmessages['lifecount']} {lives}\n")
            break # Exit loop if answer is correct
        else:
          lives -= 1 # Deduct a life for incorrect answer
          print(dmessages['invalidate'])
          print(f"{dmessages['lifecount']} {lives}\n")

    except ValueError:
        # Handle non-integer inputs
        print(dmessages['errorcatch'])
        print(f"{dmessages['lifecount']} {lives}\n")
        continue
    except KeyboardInterrupt:
        # Handle user interruption
        print(dmessages['stop'])
        quit()
  return lives

display_intro()
lives = NB_OF_INITIAL_LIVES
for question_index, _ in enumerate(lquestions):
  lives = ask_question(lives, question_index)

# Display end game message based on remaining lives
if lives > 0:
  print(dmessages['congratulate'])
else:
  print(dmessages['loose'])