def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0


        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j] 
            j += 1  
            k += 1

        

if __name__ == '__main__':
    array = [54,12,3,56,7,145]
    print(array)    
    merge_sort(array)     
    print(array)        