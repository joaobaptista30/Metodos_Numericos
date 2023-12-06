from sigfig import round


def media(x1,x2,d_sig):
    x1=round(x1,sigfigs=d_sig)
    x2=round(x2,sigfigs=d_sig)

    t=round(x1+x2,sigfigs=d_sig)

    return round(t/2,sigfigs=d_sig)



print(media(5.74,5.72,3))