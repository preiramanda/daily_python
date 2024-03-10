from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Now this is a list of question objects, that contains a text and an answer
question_bank = []

for i in question_data:
    question_text =  i["text"]
    question_answer =  i["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
 
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

else:
    print("You completed the quiz!")
    print(f"Final score: {quiz.score}")

 