print("WELCOME TO THIS QUIZ GAME v1.0 CREATED BY NAMAN GARG")
print()
score = 0
cmd = input('''To see rules type (R)
To play type (Y)
To quit type (q)\n''')

match cmd.lower():
    case "r":
        print('''+1 for every correct answer\n-1 for every incorrect answer''')
    case "q":
        print("If you want to play then run this program again")
        quit()
    case "y":
        question = print("ALU stands for? ")
        options = ['A: Arithmatic Logic Unit','B: Application Logic Unit','C: Array Logic Unit','D: None of above']
        for i in options:
            print(i)
        answer = input("Type your answer: ")
        if answer.lower() != 'a':
            print("Correct!")
            score -=1
        else:
            print("Incorrect!")
            score +=1
        
        question = print("Which of the following is valid storage type? ")
        options = ['A: CPU','B: Pen Drive','C: Keyboard','D: Track Ball']
        for i in options:
            print(i)
        answer = input("Type your answer: ")
        if answer.lower() != 'b':
            print("Correct!")
            score -=1
        else:
            print("Incorrect!")
            score +=1

        question = print("The list of coded instrctions is called? ")
        options = ['A: Computer Program','B: Algorithm','C: Flowchart','D: Utility Program']
        for i in options:
            print(i)
        answer = input("Type your answer: ")
        if answer.lower() != 'a':
            print("Correct!")
            score -=1
        else:
            print("Incorrect!")
            score +=1

        question = print("Who is the father of Computers? ")
        options = ['A: James Gosling','B: Charles Babbage','C: Dennis Ritchie','D: Bjarne Stroustrup']
        for i in options:
            print(i)
        answer = input("Type your answer: ")
        if answer.lower() != 'b':
            print("Correct!")
            score -=1
        else:
            print("Incorrect!")
            score +=1

        question = print("What is the full form of CPU? ")
        options = ['A: Computer Processing Unit','B: Computer Principle Unit','C: Central Processing Unit','D: Control Processing Unit']
        for i in options:
            print(i)
        answer = input("Type your answer: ")
        if answer.lower() != 'c':
            print("Correct!")
            score -=1
        else:
            print("Incorrect!")
            score +=1

        print(f"You got {score} out of {5}")
        cmd = input("To view answers type (A)\nTo end this quiz type (Q)")

        match cmd.lower():
            case "a":
                print("C: Array Logic Unit\nB: Pen Drive\nA: Computer Program\nB: Charles Babbage\nC: Central Processing Unit")
            case "q":
                print("If you want to play then run this program again")
                quit()