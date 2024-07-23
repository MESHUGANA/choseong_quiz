from jamo import h2j, j2hcj
import os

PATH_RES = './res/'
def get_txt_names():
    file_list = os.listdir(PATH_RES)
    return [file.replace('.txt', '') for file in file_list if file.endswith('.txt')]

def get_data(file_name):
    file = open(PATH_RES + file_name, 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    return data

def get_jaum_set(data):
    jaum_set = []
    for i in data:
        han = i.strip()  # 앞뒤 공백 제거
        jaum_set.append([''.join(han), han2jaum(han)])
    return jaum_set

def han2jaum(han):
    jaum = []
    for i in han:
        temp = h2j(i)  # 완성형 -> 조합형
        imf = j2hcj(temp)  # 자모 분리
        jaum.append(imf[0])  # 초성만 사용
    return ''.join(jaum)

def constraint(num, min_num, max_num):
    if min_num > max_num:
        min_num, max_num = max_num, min_num
    num = max(num, min_num)
    num = min(num, max_num)
    return num

def select_subject(subjects):
    print('플레이하실 주제 또는 번호를 선택하여 입력하세요.')

    for i, subject in enumerate(subjects):
        print(f'{i + 1}. {subject}')

    while(True):
        response = input()

        if response.isdecimal() and 0 < int(response) <= len(subjects):
            subject = subjects[int(response) - 1]
            break
        elif response in subjects:
            subject = response
            break
        else:
            print('잘못된 입력입니다. 다시 입력해주세요.')
    return subject, subject + '.txt'

# def game():
#     correct = 0

#     print('초성 퀴즈를 시작합니다.')
#     print('데이터: ', fileName)
#     print(f'플레이하실 퀴즈 개수를 입력하세요.(최대 {dataNum}개)')
#     n = constraint(int(input()), 0, dataNum)
    
#     gameData = sample(jaumSet, n)  # 데이터에서 랜덤뽑기
#     for ans, quiz in gameData:
#         while(True):
#             print(quiz)
#             reply = input()
#             if reply == ans:
#                 print('정답입니다!')
#                 correct += 1
#                 break
#             elif reply == '답공개':
#                 print('정답은', ans)
#                 break
#             print('틀렸습니다!')
#     print(f'맞춘 개수: {correct}')

# fileName = './res/pokemon.txt'

# data = getData(fileName)
# jaumSet = getJaumSet(data)

# dataNum = len(jaumSet)

# game()