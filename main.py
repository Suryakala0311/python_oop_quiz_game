from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    q_question = items["text"]
    q_answer = items["answer"]
    quiz_question = Question(q_question, q_answer)
    question_bank.append(quiz_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You final score was: {quiz.score}/{quiz.question_number}")