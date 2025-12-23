"""
question_model.py

This module defines the Question class, which serves as a blueprint for creating
individual question objects in the quiz.
"""

class Question:
    """
    Models a single question with its text and answer.
    
    Attributes:
        text (str): The text of the question.
        answer (str): The correct answer to the question (e.g., "True" or "False").
    """
    def __init__(self, q_text, q_answer):
        """
        Initializes a new Question object.
        
        Args:
            q_text (str): The text for the question.
            q_answer (str): The correct answer for the question.
        """
        self.text = q_text
        self.answer = q_answer
