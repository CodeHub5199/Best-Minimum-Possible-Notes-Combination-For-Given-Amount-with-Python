print('\t\t\tWelcome to note counter')
import math
amount = int(input('Enter amount: '))
if amount >=2000:
    a1 = amount/2000 
    b1 = amount%2000 
    if b1 >= 500:
        c1 = b1/500 
        d1 = b1%500
        if d1 >= 200:
            e1 = d1/200
            f1 = d1%200
            if f1 >= 100:
                g1 = f1/100
                h1 = f1%100
                if h1 >= 50:
                    i1 = h1/50
                    j1 = h1%50
                    if j1 >= 20:
                        k1 = j1/20
                        l1 = j1%20
                        if l1 >= 10:
                            m1 = l1/10
                            n1 = l1%10
    print('2000: ',math.floor(a1))
    print('500: ',math.floor(c1))
    print('200: ',math.floor(e1))
    print('100: ',math.floor(g1))
    print('50: ',math.floor(i1))
    print('20: ',math.floor(k1))
    print('10: ',math.floor(m1))

elif 500 <= amount < 2000:
    if amount >= 500:                           #790
        c1 = amount/500                         #500=1
        d1 = amount%500 #290
        if d1 >= 200:                           #290
            e1 = d1/200                         #90 200=1
            f1 = d1%200
            if f1 >= 100:
                g1 = f1/100
                h1 = f1%100
                if h1 >= 50:                    #90
                    i1 = h1/50                  #40 50=1
                    j1 = h1%50                  
                    if j1 >= 20:
                        k1 = j1/20              #20=2
                        l1 = j1%20
                        if l1 >= 10:
                            m1 = l1/10
                            n1 = l1%10
    print('500: ',math.floor(c1))
    print('200: ',math.floor(e1))
    print('100: ',math.floor(g1))
    print('50: ',math.floor(i1))
    print('20: ',math.floor(k1))
    print('10: ',math.floor(m1))

elif 200 <= amount < 500:
    if amount >= 200:
        e1 = amount/200
        f1 = amount%200
        if f1 >= 100:
            g1 = f1/100
            h1 = f1%100
            if h1 >= 50:
                i1 = h1/50
                j1 = h1%50
                if j1 >= 20:
                    k1 = j1/20
                    l1 = j1%20
                    if l1 >= 10:
                        m1 = l1/10
                        n1 = l1%10
    print('200: ',math.floor(e1))
    print('100: ',math.floor(g1))
    print('50: ',math.floor(i1))
    print('20: ',math.floor(k1))
    print('10: ',math.floor(m1))
elif 100 <= amount < 200 :
    if amount >= 100:
        g1 = amount/100
        h1 = amount%100
        if h1 >= 50:
            i1 = h1/50
            j1 = h1%50
            if j1 >= 20:
                k1 = j1/20
                l1 = j1%20
                if l1 >= 10:
                    m1 = l1/10
                    n1 = l1%10
    print('100: ',math.floor(g1))
    print('50: ',math.floor(i1))
    print('20: ',math.floor(k1))
    print('10: ',math.floor(m1))

elif 50 <= amount < 100 :
    if amount >= 50:
            i1 = amount/50
            j1 = amount%50
            if j1 >= 20:
                k1 = j1/20
                l1 = j1%20
                if l1 >= 10:
                    m1 = l1/10
                    n1 = l1%10
    print('50: ',math.floor(i1))
    print('20: ',math.floor(k1))
    print('10: ',math.floor(m1))

elif 20 <= amount < 50 :
    if amount >= 20:
        k1 = amount/20
        l1 = amount%20
        if l1 >= 10:
            m1 = l1/10
            n1 = l1%10
    print('20: ',math.floor(k1))
    print('10: ',math.floor(m1))

elif 10 <= amount < 20 :
    if amount >= 10:
        m1 = amount/10
        n1 = amount%10
    print('10: ',math.floor(m1))
    

    


