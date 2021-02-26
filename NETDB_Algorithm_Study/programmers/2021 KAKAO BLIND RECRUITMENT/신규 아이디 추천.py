def solution(new_id):
    answer = ''
    new_id.lower()
    for i in new_id:
        if i.islower() or i in "-" or i in "_" or i in ".":
            answer += i

    answer = answer.strip(".")
    if answer in ".":
        print(answer)
    return answer