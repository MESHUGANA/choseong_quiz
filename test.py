from jaum import *
from random import *


# 퀴즈 주제 선택
quiz_subject, quiz_file = select_subject(get_txt_names())

# 퀴즈 데이터 가공하여 초성 데이터 생성
jaum_set = get_jaum_set(get_data(quiz_file))
data_num = len(jaum_set) # 데이터 길이

correct_cnt = 0 # 맞춘 횟수
hint_cnt = 0

# 퀴즈 개수 입력
print(f'\n{quiz_subject} 초성 퀴즈를 시작합니다.')
print(f'플레이하실 퀴즈 개수를 입력하세요.(최대 {data_num}개)')
n = constraint(int(input()), 0, data_num)
print()

game_data = sample(jaum_set, n)  # 데이터에서 랜덤뽑기

for i, (ans, quiz) in enumerate(game_data):
    hint_pos_list = [i for i in range(len(quiz))]
    shuffle(hint_pos_list)
    print(f'{i + 1}. ', end='')
    while(True):
        # 문제 출력
        print(f'[{quiz_subject}] {quiz}')
    
        reply = input()
        
        if reply == ans:
            print('정답입니다!\n')
            correct_cnt += 1
            break
        elif reply == '답공개':
            print(f'정답은 {ans}입니다!\n')
            break
        elif reply == '힌트':
            if len(hint_pos_list) > 1:
                hint_pos = hint_pos_list.pop()
                temp = list(quiz)
                temp[hint_pos] = ans[hint_pos]
                quiz = ''.join(temp)
                hint_cnt += 1
                print()
            else:
                print('힌트를 더 이상 사용할 수 없습니다. 답공개를 사용해주세요.\n')
        elif reply == '패스':
            print()
            break
        else:
            print('틀렸습니다!\n')

print(f'맞춘 개수: {correct_cnt}')
print(f'힌트 사용: {hint_cnt}')