import random

def addition():   
    x = random.randint(0,10)
    y = random.randint(0,10) 
    r_answer = x + y
    return x, y, r_answer


def deduction():
    x = random.randint(0,10)
    y = random.randint(0,10)
    
    while x<y :
        x = random.randint(0,10)
        y = random.randint(0,10) 

    r_answer = x - y
    return x, y, r_answer

def multiplication():
    x = random.randint(0,10)
    y = random.randint(0,10) 

    r_answer = x * y
    return x, y, r_answer

def division():
    x = random.randint(1,10)
    y = random.randint(1,10)
    
    while x<y :
        x = random.randint(1,10)
        y = random.randint(1,10)

    while x%y !=0 :
        x = random.randint(1,10)
        y = random.randint(1,10)
    
        while x<y :
            x = random.randint(1,10)
            y = random.randint(1,10)

    r_answer = x / y
    return x, y, r_answer

def u_answerf(q_x, q_type, q_y):
    while True:
        try:
            u_answer = int(input(f"{q_x} {q_type} {q_y} = "))
            
        except ValueError:
            continue
            
        else:
            return u_answer
        

def main():

    score = 0

    while True:
        
        q_type = random.choice(["+","-","*","/"])
        
        if q_type == "+":
            question = addition()
            q_x = question[0]
            q_y = question[1]
            r_answer = question[2]
        
        elif q_type == "-":
            question = deduction()
            q_x = question[0]
            q_y = question[1]
            r_answer = question[2]
        
        elif q_type == "*":
            question = multiplication()
            q_x = question[0]
            q_y = question[1]
            r_answer = question[2]

        else:
            question = division()
            q_x = question[0]
            q_y = question[1]
            r_answer = question[2]

        u_answer = u_answerf(q_x, q_type, q_y)
            

        if u_answer == r_answer:
            print ("Congratulation, you're right!!")
            score = score+1
        else :
            print("Sorry, you're wrong.")
            break
        
        
    print(f"Your score is {score}")


main()