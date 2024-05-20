if __name__ == '__main__':
    lst=[]
    min_score = float('inf')
    second_min_score = float('inf')
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])
        if score < min_score:
            second_min_score =min_score
            min_score=score
        elif score < second_min_score and score != min_score:
            second_min_score =score
    sec_lst =[]
    for item in lst:
        if item[1] == second_min_score:
            sec_lst.append(item[0])
    sec_lst.sort()
    print(*sec_lst, sep="\n")