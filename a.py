def solution(heights):
    new_arr = []
    for index in range(len(heights)):
        if index == 0:
            new_arr.append(0)
        else:
            for a in range(index, -1, -1):
                if heights[a] > heights[index]:
                    new_arr.append(a+1)
                    break
            if len(new_arr) == index+1:
                continue
            new_arr.append(0)
    print(new_arr)
                
solution([6,9,5,7,4])