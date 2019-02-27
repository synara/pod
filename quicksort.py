"""dividir pra conquistar"""
""" http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html """

def quick_sort(a): 
        quickSortHelper(a, 0, len(a)-1)

def quickSortHelper(a, first, last):
     if first < last:
         splitpoint = partition(a, first, last)

         print(a)
         quickSortHelper(a, first, splitpoint-1)
         quickSortHelper(a, splitpoint + 1, last)

def partition(a, first, last):
    pivot = a[first]

    leftmark = first + 1
    rightmark = last

    done = False
    
    while not done:

        while leftmark <= rightmark and a[leftmark] <= pivot:
            leftmark = leftmark + 1

        while a[rightmark] >= pivot and rightmark >= leftmark:
           rightmark = rightmark -1

        if rightmark < leftmark:
           done = True
        else:
           temp = a[leftmark]
           a[leftmark] = a[rightmark]
           a[rightmark] = temp

    temp = a[first]
    a[first] = a[rightmark]
    a[rightmark] = temp

    return rightmark

if __name__ == '__main__':
    array = [1,26,93,17,77,31,44,55,20]
    quick_sort(array)
    print(array)
