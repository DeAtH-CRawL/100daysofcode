"""
quiz_brain.py

This module defines the QuizBrain class, which contains the core logic for running the quiz,
including tracking the current question, checking answers, and keeping score.
"""

class QuizBrain:
    """
    Manages the quiz logic, state, and user interaction.

    Attributes:
        question_number (int): The index of the current question in the list.
        score (int): The user's current score.
        question_list (list): A list of Question objects for the quiz.
    """
    def __init__(self, q_list):
        """
        Initializes a new QuizBrain object.
        
        Args:
            q_list (list): A list of Question objects.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """
        Checks if there are more questions remaining in the quiz.
        
        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        """
        Retrieves the next question, prompts the user, and checks their answer.
        """
        # Get the current question object from the list.
        current_question = self.question_list[self.question_number]
        # Increment the question number for the next round.
        self.question_number += 1
        # Prompt the user for their answer.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Check if the user's answer is correct.
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        """
        Validates the user's answer, updates the score, and provides feedback.
        
        Args:
            user_answer (str): The answer provided by the user.
            correct_answer (str): The correct answer from the Question object.
        """
        # Compare the user's answer with the correct answer (case-insensitive).
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            # Increment the score if the answer is correct.
            self.score += 1
        else:
            print("That's wrong.")
        
        # Provide feedback to the user.
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        # Add a newline for better readability in the console.
        print("\n")
