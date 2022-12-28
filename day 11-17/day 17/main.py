from question_model import *
import random

score =0
while len(question)>0:
    
    question_asked=random.choice(question)
    index_=question.index(question_asked)
    answer=real_answer[index_]
    print("\n\n")
    print(question_asked)
    answer_by_user=input("enter True or False : ")
    answer_=""
    c=0
    for i in answer_by_user:
        if c==0:
            i=i.upper()
        answer_=answer_+i
        c=c+1

    if (answer_==answer):
       score=score+1
       print("\nCorrect !!!")
    else:
       print("\nwrong !!!")
    print(f"your current score is : {score}")    

    del question[index_]
    del real_answer[index_]



