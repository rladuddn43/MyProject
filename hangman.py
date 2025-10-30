#행맨 만들기
import random as r




def print_hangman(tryNumber):

    print("     _______")
    print("     |     |")
    print("           |")
    print("           |")
    print("           |")
    print("         -----\n")

    if tryNumber == 5:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("           |")
        print("           |")
        print("         -----\n")
    elif tryNumber == 4:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("     |     |")
        print("           |")
        print("         -----\n")
    elif tryNumber == 3:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("    /|     |")
        print("           |")
        print("         -----\n")
    elif tryNumber == 2:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("    /|\\    |")
        print("           |")
        print("         -----\n")
    elif tryNumber == 1:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("    /|\\    |")
        print("    /      |")
        print("         -----\n") 
    elif tryNumber == 0 :
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("    /|\\    |")
        print("    / \\    |")
        print("         -----\n")
        print("실패!")
        

def print_list(list):
    for i in list:
        print(i,end="")






def main():

    wordList = ["apple","banana","seventeenfour","canada","football","fantastic",
            "jacket","amazing","university","kookmin","insect","worldcup","movie",
            "hangman","notebook"]
    computerPickWord = wordList[r.randint(0,len(wordList)-1)]


    tryNumber = 6

    binkan = [ "_" for i in range(len(computerPickWord))]


    while (tryNumber >0):
        print_hangman(tryNumber)
        print_list(binkan)
        guessOfPlayer = input("\n알파벳을 추측해보세요!\n")

        for i in range(len(computerPickWord)):
            if guessOfPlayer == computerPickWord[i]:
                binkan[i] = computerPickWord[i]
            
            ##원래 여기 있엇음
        if guessOfPlayer not in binkan:
            tryNumber -=1

        if binkan == list(computerPickWord):
            print("성공!")
            print("정답: ",end="")
            print_list(binkan)
            break
        elif tryNumber == 0:
            print_hangman(tryNumber)






            
          
if __name__ =="__main__":
    main()

