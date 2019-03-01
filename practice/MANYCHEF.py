t=int(input())
for _ in range(t):
    s= input()
    s=list(s)
    for i in range(len(s)-4,-1,-1):
        if((s[i]=='?' or s[i]=='C') and (s[i+1]=='?' or s[i+1]=='H') and (s[i+2]=='?' or s[i+2]=='E') and (s[i+3]=='?' or s[i+3]=='F')):
            s[i:i+4]=list('CHEF')
    for i in range(len(s)):
        if(s[i]=='?'):
            s[i]='A'
    s=''.join(s)
    print(s)
