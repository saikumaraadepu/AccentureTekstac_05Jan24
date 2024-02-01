def funny_string(string):
    if len(string)<2 or len(string)>50:
        return 'Invalid string'
    STR1=string
    STR2=string[::-1]
    for i in range(len(string)):
        if abs(ord(STR1[i])-ord(STR1[i-1]))!=abs(ord(STR2[i])-ord(STR2[i-1])):
            return 'Not funny'
    return 'Funny'
    
string=input('Enter the string:\n')
print(funny_string(string))
