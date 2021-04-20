## 패키지 import
import random


## 함수들
# 1-1) 10 x 10의 말판을 list를 이용해 만들기
def make_grid(h, w):
    grid = [[" . " for _ in range(w)] for _ in range(h)]
    return grid


grid_ls = make_grid(10, 10)
print('\n'.join(''.join(row) for row in make_grid(10, 10)))


def is_end(stone):
    # 다섯개가 연이어 있는지 확인
    # 모든 가로줄 check
    for j in range(10):
        for i in range(6):
            if grid_ls[j][i + 0] == stone and grid_ls[j][i + 1] == stone and grid_ls[j][i + 2] == stone and grid_ls[j][
                i + 3] == stone and grid_ls[j][i + 4] == stone:
                return True
    # 세로줄 check
    for j in range(6):
        for i in range(10):
            if grid_ls[j + 0][i] == stone and grid_ls[j + 1][i] == stone and grid_ls[j + 2][i] == stone and \
                    grid_ls[j + 3][i] == stone and grid_ls[j + 4][i] == stone:
                return True
    # 대각선 check
    for j in range(6):
        for i in range(6):
            if grid_ls[j + 0][i + 0] == stone and grid_ls[j + 1][i + 1] == stone and grid_ls[j + 2][i + 2] == stone and \
                    grid_ls[j + 3][i + 3] == stone and grid_ls[j + 4][i + 4] == stone:
                return True
    for j in range(4, 10):
        for i in range(6):
            if grid_ls[j + 0][i + 0] == stone and grid_ls[j - 1][i + 1] == stone and grid_ls[j - 2][i + 2] == stone and \
                    grid_ls[j - 3][i + 3] == stone and grid_ls[j - 4][i + 4] == stone:
                return True
    # 위에 if 에서 안걸렸다 == 안끝난다.
    return False

# 다음부턴 while문 사용하기
def omuk_input():
    # 1-2) 말판에 사람이 두 숫자를 좌표로 받으면 말판에 x 말이 나오도록 구현
    xinput = input().split()
    xinput = [int(num) for num in xinput]
    y = xinput[1]
    x = xinput[0]
    if grid_ls[y - 1][x - 1] == ' . ':
        grid_ls[y - 1][x - 1] = ' X '
    # 1-3) 사람이 좌표 입력시, 비어있는 칸이 아닌, 다른 말이 놓여있는 상태였다면, ‘다른 좌표를 입력해야 합니다' 라는 경고문구가 뜬뒤, 다시 입력을 받는 로직을 추가합니다.
    else:
        print("다른 좌표를 입력해야 합니다")
    if is_end(' X '):  # 사람이 게임을 끝내요
        print('\n'.join(''.join(row) for row in grid_ls))
        return True

    # 1-4) 사람이 말(X)을 성공적으로 놓은 뒤, 컴퓨터(상대)가 random 하게 말판에 말(O)을 놓는 로직을 추가합니다. [이 때, 위의 문제 2-3) 과 같이 빈 칸이 아니면 다시 놓는 로직을 추가합니다.
    while grid_ls[y - 1][x - 1] == ' X ':
        y2 = random.randint(1, 10)
        x2 = random.randint(1, 10)
        if grid_ls[y2 - 1][x2 - 1] != ' . ':
            continue
        else:
            grid_ls[y2 - 1][x2 - 1] = ' O '
            print('\n'.join(''.join(row) for row in grid_ls))
            break
    if is_end(' O '):  # 게임이 끝나요
        print('\n'.join(''.join(row) for row in grid_ls))
        return False

### main ###
# 1-5) 문제 2) 에서 문제 4) 의 과정이 무한 반복되도록 만듭니다.
while True:
    result = omuk_input()
    if result == True:
        print("사람이 이김")
        break
    elif result == False:
        print("컴터가 이김")
        break