from colorama import Fore #텍스트에 color를 지정할 수 있는 모듈 가져오기
from my_mod import Tic_tac_toe

if __name__ == '__main__':
    #두명의 사용자 이름 받아오기
    play1 = input("유저(1)의 이름을 입력해주세요 : ")
    print(play1 + " " + "유저의 Mark '○'")
    play2 = input("유저(2)의 이름을 입력해주세요 : ")
    print(play2 + " " + "유저의 Mark '×'")

    start = Tic_tac_toe()

    #게임에서 우승자가 생기거나, 판에서 남은 숫자가 없을 때까지 진행한다
    while start.winner == 0 and len(start.remainder) != 0:
        move = 0

        #배열판 프린트
        print('\n' + str(start))
        if start.turn == 1: #turn이 홀수면 user1, turn이 짝수면 user2
            name = play1
        else :
            name = play2

        # 입력할 수 있는 배열판을 현재 user와 같이 출력해준다
        string = "'{0}'님의 차례입니다 - 원하는 포지션을 입력해주세요. \n남은 자릿수: *  {1}  * : " .format(name, ', '.join([str(x) for x in start.remainder]))

        while move not in start.remainder: #remainder안에 있는 숫자 안에서 입력받는다
            try:
                move = int(input(string))

                if move not in start.remainder: raise TypeError
            except: #예외처리
                print('다시 입력해주세요.')
        start.move(move)

    else: #마지막 차레
        print(start) #마지막 결과 출력해주기
        if start.winner != 0: # 무승부가 아닐 때
            if start.winner == 1: #Winner가 1이면 play1 우승, 2면 play2 우승
                winner = play1
                Lose = play2
            else:
                winner = play2
                Lose = play1

            print(Fore.BLUE + '이겼다 !!: '+ Fore.WHITE + str(winner)) #이긴 사람 출력
            print(Fore.YELLOW +'졌다  !!: '+ Fore.WHITE + str(Lose))  #진사람 출력
        else: #무승부 일때
            print('!!비겼습니다!!')
