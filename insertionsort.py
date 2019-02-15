def insertion_sort (a, compare):
    for k in range(1,len(a)):
        current = a[k]
        j = k

        while j > 0 and compare(a[j-1], current) > 0:
            a[j] = a[j-1]
            j = j - 1

        a[j] = current
        print(k, a)

def compare_int(a, b):
    return a-b

def compare_cars(a, b): 
    return a.potencia - b.potencia


if __name__ == '__main__' :
    a = [2,4,13,1,5,8,2]
    insertion_sort(a, compare_int)