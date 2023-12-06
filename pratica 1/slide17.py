
import math
#ex12
from sigfig import round

x1=5.74
x2=5.72
num_digitos_significativos=2


def media(x1,x2,num_digitos_significativos):
    t1=round(x1, sigfigs= num_digitos_significativos)
    t2=round(x2, sigfigs= num_digitos_significativos)
    tsoma=round(t1+t2, sigfigs= num_digitos_significativos)
    print(tsoma)
    tmedia=round(tsoma/2, sigfigs= num_digitos_significativos)

    return tmedia


print(media(x1,x2,num_digitos_significativos))