import random

word_list=["wakabahashi","aragaki","kasuga"]

x=random.randint(0,2)
#print(x)
word_list[x]
#print (word_list[x])


def hangman(word):
    wrong=0
    stages=["",
            "___________",
            "|      |   ",
            "|      |   ",
            "|      0   ",
            "|     /|\  ",
            "|     / \  ",
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("hangman!")
    
    while wrong < len(stages)-1:
        print("\n")
        msg="予想してね"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong +=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("lose.answer is {}.".format(word))
        
        
hangman(word_list[x])
