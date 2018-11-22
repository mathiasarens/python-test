import sys


def minimumPasses(m, w, p, n):
    candy = 0
    steps = 0
    while candy < n:
        if candy < p and n >= p:
            add_steps=((p-candy)//(m*w))-1
            if add_steps > 0:
                steps += add_steps
                candy += add_steps * m * w
        candy+=m*w

        # buy new machines or workers if possible
        old_candy,old_m,old_w = candy,m,w
        old_eta = (n-candy)/(m*w)
        # make count of workers and machines equal
        if m < w:
            new_m = min(candy//p, w-m)
            m+= new_m
            candy -= new_m*p
        if w < m:
            new_w = min(candy//p, m-w)
            w+=new_w
            candy-=new_w*p
        # candy for new workers and machines
        new_m_w = candy//(2*p)
        m+=new_m_w
        w+=new_m_w
        candy-=new_m_w*2*p
        # candy for new machine
        new_machine = candy//p
        m+=new_machine
        candy-=new_machine*p

        # throw recently machines/workers away if it is better not to invest
        eta = (n-candy) / (m*w)
        if old_eta < eta:
            candy = old_candy
            w = old_w
            m = old_m
            add_steps=((n-candy)//(m*w))-1
            if add_steps > 0:
                steps += add_steps
                candy += add_steps * m * w
        steps +=1
    return steps

print(minimumPasses(3,1,2,12)==3)
print(minimumPasses(1,1,6,45)==16)
print(minimumPasses(1,100,10000000000,250)==3)
print(minimumPasses(5184889632,5184889632,20,10000)==1)
print(minimumPasses(1,1,1000000000000,1000000000000)==1000000000000)
print(minimumPasses(1,100,1000,10000)== 39)
print(minimumPasses(1,100,10000,100000) == 384)
print(minimumPasses(1,100,10000000000,1000000000000)==617737754)


def minimumPassesCorrectButTooSlow(m, w, p, n):
    candy = 0
    steps = 0
    investing = True
    while candy < n:
        if candy < p and n >= p:
            add_steps=((p-candy)//(m*w))-1
            if add_steps > 0:
                steps += add_steps
                candy += add_steps * m * w
        candy+=m*w
        if investing:
            old_candy = candy
            old_m = m
            old_w = w
            old_eta = (n-candy)/(m*w)
            if m < w:
                new_m = min(candy//p, w-m)
                if new_m > 0:
                    m+= new_m
                    candy -= new_m*p
            if w < m:
                new_w = min(candy//p, m-w)
                if new_w >0:
                    w+=new_w
                    candy-=new_w*p
            # candy for new workers and machines
            new_m_w = candy//(2*p)
            if new_m_w > 0:
                m+=new_m_w
                w+=new_m_w
                candy-=new_m_w*2*p
            # candy for new machine
            new_machine = candy//p
            if new_machine >0:
                m+=new_machine
                candy-=new_machine*p

            eta = (n-candy) / (m*w)
            if old_eta < eta:
                investing = False
                candy = old_candy
                w = old_w
                m = old_m
        steps +=1
    return steps

# print(minimumPassesCorrectButTooSlow(1,100,10000000000,1000000000000))

# Wrong

# def minimumPasses(m, w, p, n):
#     return makeCandy(m,w,p,n,0,0)

# def makeCandy(m,w,p,n,c,s):
#     if c>=n:
#         return s
#     result = sys.maxsize
#     candy = c + m*w
#     result = min(result, makeCandy(m, w, p, n, candy, s+1))
#     if m<w:
#         new_m = min(candy//p, w-m)
#         result = min(result, makeCandy(m+new_m, w, p, n, candy-(new_m*p), s+1))
#     if m>w:
#         new_w = min(candy//p, m-w)
#         result = min(result, makeCandy(m, w+new_w, p, n, candy-(new_w*p), s+1))
    
#     return result

# Probably ok but far too slow

# def minimumPasses(m, w, p, n):
#     return makeCandy(m,w,p,n,0,0)

# def makeCandy(m,w,p,n,c,s):
#     if c>=n:
#         return s-1
#     result = sys.maxsize
#     candy = c + m*w
#     result = min(result, makeCandy(m, w, p, n, candy, s+1))
#     for i in range(candy//p):
#         for j in range(i):
#             if m+i <= n or w+i <=n:
#                 result = min(result, makeCandy(m+j, w+i-j, p, n, candy-(i*p), s+1))
#     return result
