def solve2(format_str):

    answer = 0


    for i in range(len(format_str)):
        if i == 0:   
            if format_str[i] == 'C':
                answer = 26
            else:
                answer = 10
        else:
            if format_str[i] == 'C':
                if format_str[i-1] == 'C':
                    answer = answer * 25
                else:
                    answer = answer * 26
            else:
                if format_str[i-1] == 'N':
                    answer = answer * 9
                else:
                    answer = answer * 10

    return answer
