def calculate_third_edge(first_edge, second_edge, include_long_edge = False):
    #只能算直角三角形
    possible_answer = list()
    #不含長邊
    if include_long_edge == False: #if !include_long_edge
        #get long edge
        answer = (first_edge**2 + second_edge**2) **0.5
        possible_answer.append(answer)
    #有含長邊
    elif first_edge != second_edge:
        #get another short edge
        longer_one = max(first_edge, second_edge)
        shorter_one = min(first_edge, second_edge)
        answer_2 = (longer_one**2 - shorter_one**2) **0.5
        possible_answer.append(answer_2)
    return possible_answer

if __name__ == '__main__':
    print(calculate_third_edge(3, 4)) #預設為false
    print(calculate_third_edge(5, 12))
    print(calculate_third_edge(13, 12, True))