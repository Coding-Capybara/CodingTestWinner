def solution(survey, choices):
    indicator = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i, s in enumerate(survey):
        l, r = s[0], s[1]
        choice = choices[i]
                
        if choice == 1:
            indicator[l] += 3
        elif choice == 2:
            indicator[l] += 2
        elif choice == 3:
            indicator[l] += 1
        elif choice == 5:
            indicator[r] += 1
        elif choice == 6:
            indicator[r] += 2
        elif choice == 7:
            indicator[r] += 3
        else:
            continue
    
    first = 'R' if indicator['R'] >= indicator['T'] else 'T'
    second = 'C' if indicator['C'] >= indicator['F'] else 'F'
    third = 'J' if indicator['J'] >= indicator['M'] else 'M'
    fourth = 'A' if indicator['A'] >= indicator['N'] else 'N'
        
    return ''.join([first, second, third, fourth])