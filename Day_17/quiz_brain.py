class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):        
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        #I'll add 1 here because it shows +1 question number
        self.question_number += 1
        uanswer = input(f"Q.{self.question_number}:{current_question.text} (True/False)").lower()
        self.check_answer(uanswer,current_question.answer)

    def check_answer(self,uanswer,canswer):
        if uanswer == canswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
    
        print(f"Your score: {self.score}/{self.question_number}\n")



