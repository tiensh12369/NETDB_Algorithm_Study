def solution(new_id):
    answer_1 = new_id.lower()
    answer_2 = ''
    answer_3 = ''
    answer_4 = ''

    for i in answer_1:
        if i.islower() or i.isdigit() or i in "-" or i in "_" or i in ".":
            answer_2 += i

    for i in range(0, len(answer_2)):
        if answer_2[i] == "." and answer_2[i] == answer_2[i-1]:
            continue
        else:
            answer_3 += answer_2[i]

    answer_3 = answer_3.strip(".")

    for i in range(0, len(answer_3)):
        if i <= 14:
            answer_4 += answer_3[i]

    answer_4 = answer_4.strip(".")

    if not len(answer_4):
        answer_4 = "a"
        
    while len(answer_4) < 3: 
        answer_4 += answer_4[-1]
    answer = answer_4

    return answer
'''
#정규식 풀이
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''