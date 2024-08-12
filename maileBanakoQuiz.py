#create a kbc/quiz game where 5 questions are asked and 5 answer need to be provided after each correct answer 

print('welcome to the quiz')
score=0
a1=input('What is the capital city of France?')
if(a1=='paris'):
    score+=1
else:
    a2=input('What is the chemical symbol for the element Gold?')
    if (a2=='Au'): # Fixed indentation here
        score+=1
    else:
        a3=input('Who was the first President of the United States?')
        if (a3=='George Washington'):
            score+=1
        else:
            a4=input('Who wrote the play "Romeo and Juliet"?')
            if (a4=='shakespeare'):
                score+=1
            else:
                a5=input('What is the value of π (pi) up to two decimal places?')
                if (a5=='3.14'): # Note: Comparing strings, not numbers
                    score+=1
print('congratulations you scored',score)
