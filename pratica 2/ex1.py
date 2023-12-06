import math

#a

def cal_n_iter(a,b,error):
    return math.ceil(math.log2((b-a/error)))

def F(k):
    ...

#b
def successive_bisections(f,a,b,error):
    n = 0
    delta= (b-a)/(2**n)
    n_iter= cal_n_iter(a,b,error)
    while(n<n_iter):
        m=(a+b)/2
        if f(m)==0:
            delta=0
            return m        
        
        elif(f(m)*f(a)<0):
            b=m
        elif(f(m)*f(a)>0):
            a=m

        delta/=2
        n+=1
        
    return m,delta



#2.a
def F(k):
    return 0.123**k - k

result,delta = successive_bisections(F,0,1,1e-5)
print("2.a)")
print(f"Solution = {result:.3f} +/- {delta:.2e}")