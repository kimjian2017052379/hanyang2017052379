from colorama import Fore
class Tic_tac_toe:
    #이긴 케이스의 경우를 나열
    Win_case = ((0, 1, 2), (3, 4, 5),
                (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

    def __init__(self): #초기화(init) 단계
        self.turn = 1       #게임 턴
        self.winner = 0     #우승한 사람, O가 이길 경우 1을, X가 이길 경우 2를 리턴한다.
        self.board = list(range(1, 10))  #tictactoe의 게임 보드는 1부터 9까지의 수로 되어있다
        self.remainder = list(range(1, 10)) #선택할 수 있는 보드의 남은 자리

    def __str__(self):
        Game_board = '' # String 초기화,

        #보드판을 콘솔창에 출력하기 위한 과정
        for i in range(3):
            row = self.board[i * 3:i * 3 + 3]
            Game_board +=  '{0[0]}\t{0[1]}\t{0[2]}\n'.format(row)  #3행3열 게임판 생성
        return Game_board

    def move(self, x): #배열 번호 x를 받아 turn 번호가 1일때, 'O'로 교체하고, 그렇지 않으면 X로 교체
        self.board[x-1] = Fore.RED + '○' + Fore.WHITE  \
            if self.turn == 1 \
            else Fore.GREEN + '×' + Fore.WHITE
        self.remainder.remove(x) #remainder에서 선택된 x를 제거함
        self.winner = self.winner_exam() #탐색된 우승자를 winner에 집어넣음

        # 두번째 턴으로 넘어간다, 턴이 2일땐 1로 넘어간다.
        self.turn = 2 \
            if self.turn == 1 \
            else 1

    def winner_exam(self):  #우승 체크, O or X 둘중 하나가 3개면 우승자로 지정
        for case in self.Win_case:
            count_list = [self.board[x] for x in case]
            if count_list.count(Fore.RED + '○' + Fore.WHITE) == 3:
                return 1
            elif count_list.count(Fore.GREEN + '×' + Fore.WHITE) == 3:
                return 2
            else:
                continue
        return 0
