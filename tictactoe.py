import random

space = ['0', '0', '0', '0', '0', '0', '0', '0', '0']

def print_board():
    for i in range(3):
        print(f"{space[i*3]} | {space[i*3+1]} | {space[i*3+2]}")
        if i < 2:
            print("--|---|--")

def check_winners():
    for i in range(3):
        if space[i*3] == space[i*3+1] == space[i*3+2] != '0':
            return True
        if space[i] == space[i+3] == space[i+6] != '0':
            return True
    if space[0] == space[4] == space[8] or space[2] == space[4] == space[6] != '0':
        return True
    return False

while True:
    player = int(input("어느 칸에 둘지 입력해주세요 (1~9): "))
    if space[player - 1] == '0':
        space[player - 1] = 'X'
        print_board()

        if check_winners():
            print("게임이 종료되었습니다. 플레이어가 이겼습니다.")
            break

        # 컴퓨터 턴
        while True:
            computer = random.randint(1, 9)
            if space[computer - 1] == '0':
                space[computer - 1] = 'O'
                print(f"컴퓨터가 {computer}에 수를 두었습니다")
                print_board()

                if check_winners():
                    print("게임이 종료되었습니다. 컴퓨터가 이겼습니다.")
                    break
                break
                
    else:
        print("이미 사용된 칸입니다. 다시 선택해주세요.")