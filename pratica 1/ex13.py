
eps=5e-4


def proxA(k):
    return(-1)**k*(k/((5**k)+10))

def resA(eps):
    i=1
    termo=proxA(i)
    soma=0
    while(abs(termo)>=eps):
        soma+=termo
        i+=1
        termo=proxA(i)
    print("13 a)")
    print(f"Soma: {soma}\nTermos: {i-1}")


def proxB(k):
    return 1/(k*3**k)

def resB(eps):
    L=1/3
    i=1
    soma=0
    termo=proxB(i)
    while(abs(termo/(1-L))>=eps):
        soma+=termo
        i+=1
        termo=proxB(i)
    print("13 b)")
    print(f"Soma: {soma}\nTermos: {i-1}")


def proxC(k):
    deno=1
    j=1
    while(j<=k):
        deno*=(k+j)
        j+=1
    return 1/deno

def resC(eps):
    i=1
    soma=proxC(i)
    i+=1
    while not (abs(proxC(i+1)-proxC(i))<eps):
        soma+=proxC(i)
        i+=1
   
    print("13 c)")
    print(f"Soma: {soma}\nTermos: {i-1}")




#resA(eps)
#resB(eps)
resC(eps)