if __name__ == '__main__':
    rank_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        rank_list.append([name, score]) 
    scores = [ (score) for _,score in rank_list]
    max = max (scores[0],scores[1])
    min = min (scores[0],scores[1])
    rank_list.sort ()
    for score in scores:
        if score < min:
            max = min
            min = score 
        elif score > min and score < max: 
            max = score 
        elif min == max and score > max: 
            max = score  
    for name, score in rank_list:
        if score == max:
             print (name)
