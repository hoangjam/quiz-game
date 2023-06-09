class Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.question} (True/False)?: ")
        self.check_answer(user_answer, curr_question.answer)

    def still_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
            return True
        else:
            print("Wrong!")

        print(f"The correct answer was {correct_answer}\n")
        print(f"Current score: {self.score}/{self.question_number}\n")