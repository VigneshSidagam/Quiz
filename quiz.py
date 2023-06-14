#QUIZ GAME
def fun():
    user = input("Enter your name:")
    print(f"Welcome to the quiz game {user}")
    score = 0
    print("1) Which one is a text editor for Microsoft Windows?")
    print(" A)MS Word\n B)MS Excel\n C)WordPad\n D)Notepad")
    q1 = input("choose the correct option:").lower()
    if q1=="d":
        print("HURRAY!!!, Correct answer... You got 1 mark\n")
        score+=1
    else:
        print("Sorry, Wrong answer")
        print("The correct answer is Notepad, option D")
    print(" 2) Total number of function keys in a keyboard?")
    print(" A)10\n B)12\n C)14\n D)8")
    q2 = input("choose the correct option:").lower()
    if q2=="b":
        print("HURRAY!!!, Correct answer... You got 1 mark\n")
        score+=1
    else:
        print("Sorry, Wrong answer")
        print("The correct answer is 12, option B")
    print("3) Linux is an example of?")
    print(" A)Software\n B)Application\n C)Operating System\n D)Browser")
    q3 = input("choose the correct option:").lower()
    if q3=="a":
        print("HURRAY!!!, Correct answer... You got 1 mark\n")
        score+=1
    else:
        print("Sorry, Wrong answer")
        print("The correct answer is Software, option A")
    print("4) Who developed 'PYTHON' programming language?")
    print(" A)Wick Van Rossum\n B)Rasmus Lerdorf\n C)Guido Van Rossum\n D)Niene Stom")
    q4 = input("choose the correct option:").lower()
    if q4=="c":
        print("HURRAY!!!, Correct answer... You got 1 mark\n")
        score+=1
    else:
        print("Sorry, Wrong answer")
        print("The correct answer is Guido Van Rosssum, option C")
    print("5) Which type of Programming does Python support?")
    print(" A)Object-Oriented Programming\n B)Structured Programming\n C)Functional Programming\n D)All of the mentioned")
    q5 = input("choose the correct option:").lower()
    if q5=="d":
        print("HURRAY!!!, Correct answer... You got 1 mark\n")
        score+=1
    else:
        print("Sorry, Wrong answer")
        print("The correct answer is option D")
    print("\nTHE QUIZ IS COMPLETED\n")
    if score==5:
        print("CONGRATULATIONS,WELLDONE YOU GOT 5/5 POINTS")
    else:
        print(f"Your total score is {score}/5")
fun()
repeat = input("Do you wanna repeat the quiz again,(yes/no)").lower()
while repeat=="yes":
    fun()
    repeat = input("Do you wanna repeat the quiz again,(yes/no):").lower()
else:
    print("THANKYOU")
    
