import queue
def Balan(input):
    S = queue.LifoQueue()
    out = ""
    for c in input():
        if '0'<=c<='9': out += c
        elif c=='(':S.put(c)
        elif c==')':
            while S.queue[-1] != '(': out += S.get()
            S.get() # lay dau ra khoi stack
        else:   #Cac phep toan
            while S.qsize() and  UT[S.queue[-1]]>=UT[c]: out += S.get()
            S.put(c)
    while S.qsize(): out += S.get()
    print(out)
        
def tinh(out):
    S= queue.LifoQueue()
    for c in out:
        if '0'<=c<='9': S.put(int(c))
        elif c=='+': S.put(S.get()+S.get())
        elif c=='*':S.put(S.get()*S.get())
        elif c=='-':
            b = S.get()
            a = S.get()
            S.put(a-b)
        elif c=='/':
            b = S.get()
            a = S.get()
            S.put(int(a/b))
    return S.get()
if __name__ == "__main__":
    out = Balan(input())
    print(tinh(out))