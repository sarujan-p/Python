x = input()
try :
    p = int(x)

    if p == 1 :
        a1 = input()
        n1 = int(a1)
        prize = n1 * (2**0)

    elif p == 2 :
        a1, a2 = input().split()
        n1 = int(a1)
        n2 = int(a2)

        lists = [n1,n2]
        lists.sort()
        prize = lists[0] * (2**1) + lists[1] * (2**0)

    elif p == 3 :
        a1, a2, a3 = input().split()
        n1 = int(a1)
        n2 = int(a2)
        n3 = int(a3)

        lists = [n1,n2,n3]
        lists.sort()
        prize = lists[0] * (2**2) + lists[1] * (2**1) + lists[2] * (2**0)

    elif p == 4 :
        a1, a2, a3, a4 = input().split()
        n1 = int(a1)
        n2 = int(a2)
        n3 = int(a3)
        n4 = int(a4)

        lists = [n1,n2,n3,n4]
        lists.sort()
        prize = lists[0] * (2**3) + lists[1] * (2**2) + lists[2] * (2**1) + lists[3] * (2**0)

    elif p == 5 :
        a1, a2, a3, a4, a5 = input().split()
        n1 = int(a1)
        n2 = int(a2)
        n3 = int(a3)
        n4 = int(a4)
        n5 = int(a5)

        lists = [n1,n2,n3,n4,n5]
        lists.sort()
        prize = lists[0] * (2**4) + lists[1] * (2**3) + lists[2] * (2**2) + lists[3] * (2**1) +lists[4] * (2**0)

    else : print("Error!")

    print(str(prize) + "$")
    
except Exception as e :
    print(e)
