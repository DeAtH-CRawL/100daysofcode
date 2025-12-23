"""
main.py
The entry point for the Quiz Game application.

This script orchestrates the quiz by:
1. Loading questions from the data module.
2. Creating a list of Question objects.
3. Initializing the QuizBrain with the list of questions.
4. Running the quiz loop until all questions are answered.
5. Displaying the final score to the user.
"""

# Import necessary classes and data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# --- Create the Question Bank ---
# Initialize an empty list to hold the Question objects.
question_bank = []

# Iterate through each question dictionary in the question_data list.
for question in question_data:
    # Extract the question text and answer from the dictionary.
    question_text = question["text"]
    question_answer = question["answer"]
    
    # Create a new Question object using the extracted text and answer.
    new_question = Question(question_text, question_answer)
    
    # Add the newly created Question object to the question_bank list.
    question_bank.append(new_question)


# --- Initialize and Run the Quiz ---
# Create an instance of the QuizBrain class, passing the question_bank to it.
# The QuizBrain will manage the quiz logic, such as asking questions and checking answers.
quiz = QuizBrain(question_bank)

# Start the quiz loop. The loop continues as long as there are questions left.
while quiz.still_has_questions():
    # The next_question() method handles displaying the question,
    # prompting the user for an answer, and checking if it's correct.
    quiz.next_question()

# --- Quiz Completion ---
# This code runs after the while loop finishes (i.e., all questions have been answered).
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")