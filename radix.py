import math

def create_buckets(base):
    buckets = []
    for i in range(base):
        buckets.append([])
    return buckets

def sort(items, base):
    tmp = -1
    j = 0
    m = int(math.log(items[0], base)) + 1

    while j < m:
        buckets = create_buckets(base)
        for number in items:
            tmp = number / math.pow(base, j)
            digit = int(tmp % base)
            buckets[digit].append(number)
        a = 0
        for bucket in buckets:
            for n in bucket:
                items[a] = n
                a += 1    
        print(items)
        j += 1

if __name__ == '__main__':
    items = [ 1012, 2053, 1443, 5152, 9008 ]
    sort(items, 10)