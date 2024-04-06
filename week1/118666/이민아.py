def solution(survey, choices):
    #1.
    c_dic = {'R':0, 'T':0, 'C':0, 'F':0,'J':0, 'M':0, 'A':0, 'N':0}
    a_lst = [] #answer_lst
    #2.
    for i in range(len(choices)):
        if choices[i] == 1:
            c_dic[survey[i][0]] += 3
        elif choices[i] == 2:
            c_dic[survey[i][0]] += 2
        elif choices[i] == 3:
            c_dic[survey[i][0]] += 1
        elif choices[i] == 5:
            c_dic[survey[i][1]] += 1
        elif choices[i] == 6:
            c_dic[survey[i][1]] += 2
        elif choices[i] == 7:
            c_dic[survey[i][1]] += 3
        else:
            pass
    #3.
    if c_dic['R'] < c_dic['T']:
        a_lst.append('T')
    elif c_dic['R'] >= c_dic['T']:
        a_lst.append('R')
    
    if c_dic['C'] < c_dic['F']:
        a_lst.append('F')
    elif c_dic['C'] >= c_dic['F']:
        a_lst.append('C')
    
    if c_dic['J'] < c_dic['M']:
        a_lst.append('M')
    elif c_dic['J'] >= c_dic['M']:
        a_lst.append('J')
    
    if c_dic['A'] < c_dic['N']:
        a_lst.append('N')  
    elif c_dic['A'] >= c_dic['N']:
        a_lst.append('A')
        
    
    return ''.join(a_lst)
