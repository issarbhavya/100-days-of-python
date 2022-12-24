from data import question_data as qd
question=[]
real_answer=[]
for i in qd:
    question.append(i["text"])
    real_answer.append(i["answer"])
