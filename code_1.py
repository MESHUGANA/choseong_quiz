from jaum import *
from random import sample

# 퀴즈 주제 선택
quiz_subject, quiz_file = select_subject(get_txt_names())

# 퀴즈 데이터 가공하여 초성 데이터 생성
jaum_set = get_jaum_set(get_data(quiz_file))
data_num = len(jaum_set) # 데이터 길이

correct = 0 # 맞춘 횟수

# 퀴즈 개수 입력
print(f'\n{quiz_subject} 초성 퀴즈를 시작합니다.')
print(f'플레이하실 퀴즈 개수를 입력하세요.(최대 {data_num}개)')
n = constraint(int(input()), 0, data_num)
print()

def read_input(reply):
    if reply == '답공개':
        pass
    elif reply == '힌트':
        pass
    elif reply == '패스':
        pass
    else:
        pass

game_data = sample(jaum_set, n)  # 데이터에서 랜덤뽑기
for i, (ans, quiz) in enumerate(game_data):
    while(True):
        print(f'{i + 1}. [{quiz_subject}] {quiz}')
        reply = input()
        if reply == ans:
            print('정답입니다!\n')
            correct += 1
            break
        elif reply == '답공개':
            print(f'정답은 {ans}입니다!\n')
            break
        print('틀렸습니다!')
print(f'맞춘 개수: {correct}') # 데이터 길이