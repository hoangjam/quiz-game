from question_model import Question
from data import question_data
from quiz_brain import Brain

question_bank = []

for i in question_data:
    question_bank.append(Question(i['question'], i['correct_answer']))

quiz = Brain(question_bank)

while quiz.still_questions():
    quiz.next_question()

print("Completed quiz!")
print(f"Your final score is: {quiz.score}")