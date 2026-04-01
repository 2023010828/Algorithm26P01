def solve1(numbers):

    answer = 0
    
    for num in numbers:

        if num % 3 == 0 and num % 2 != 0:
            answer += num
            

    return answer
