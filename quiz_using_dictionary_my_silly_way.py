#task 4: create quiz question answer dictionary using dictionary and 2 list and zip
#question=['Nepal capital city:','national animal:','number of bones in human body'] 
q1=0
q2=0
q3=0
question=[input('q1'),input('q2'),input('q3')]
a1=0
a2=0
a3=0
answer=[input('a1'),input('a2'),input('a3')]
quiz=dict(zip(question,answer))
print(quiz)
