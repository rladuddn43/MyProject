## 컴퓨터가 생각한 숫자 맞추기!
import random as r

Level = input("난이도를 선택해주세요! \n 하 : 기회 7번 \n 중 : 기회 5번 \n 상 : 기회 3번\n")

if (Level == "하"):
    TryCount = 7
elif (Level == "중"):
    TryCount = 5
elif (Level == "상"):
    TryCount = 3


rangeOfNumber =list( map(int,input("숫자의 범위를 공백을 기준으로 정해주세요!").split()))
numberOfComputer = r.randint(rangeOfNumber[0],rangeOfNumber[1]) # 컴퓨터의 번호 선택
print("컴퓨터는 번호를 선택했습니다!")

while True:

    if TryCount == 0:
        print("기회를 모두 소진했어요! 실패 ㅠㅠ")
        break


    playerGuess = int(input("추측할 숫자를 입력해주세요! (남은 기회 : {}번) ".format(TryCount)))
    if playerGuess == numberOfComputer :
        print("정답입니다! 대단해요! 컴퓨터가 선택한 숫자는 {} 이었습니다!".format(numberOfComputer))
        break
    elif playerGuess > numberOfComputer:
        print("다운!")
        TryCount -=1
    elif playerGuess < numberOfComputer:
        print("업!")
        TryCount -=1


