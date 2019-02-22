def find_max(a, begin, end):
    index = begin
    max = a[index]

    for i in range(begin,end):
        n = a[i]

        if n > max:
            max = n 
            index = i

    return index


def selection_sort(a):
    for i in range(len(a) - 1, 0, -1):
        index = find_max(a, 0, i+1)
        
        if index != i:
            a[index], a[i] = a[i], a[index]

def insertion_sort (a):
    for k in range(1,len(a)):
        current = a[k]
        j = k

        while j > 0 and a[j-1] > current:
            a[j] = a[j-1]
            j -= 1

        a[j] = current


def worst_case(n):
    r = range(n)
    array = list(r)
    return array[::-1]

from time import time
def performance(sort, scenario):
    rates = {}
    n = 10

    while n < 50000:
        numbers = scenario(n)
        now = time()
        sort(numbers)
        done = time()
        diff = (done - now) * 1000
        rates[n] = diff
        print(n, '\t', diff)
        n *=2

    print("Done.")

if __name__ == '__main__':
    """
    array = [56,2,5,12,6]
    m = find_max(array,0,len(array))
    print('O maior está na posição: {}'.format(m))

    selection_sort(array)
    print(array)"""

    performance(selection_sort, worst_case)    