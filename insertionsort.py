def insertion_sort (a, compare):
    for k in range(1,len(a)):
        current = a[k]
        j = k

        while j > 0 and a[j-1] > current:
            a[j] = a[j-1]
            j -= 1

        a[j] = current
        print(a)

def compare_int(a, b):
    return a-b

def compare_cars(a, b): 
    return a.potencia - b.potencia

class Veiculo(object):
    def __init__(self, modelo, potencia):
        self.modelo = modelo
        self.potencia = potencia

if __name__ == '__main__' :
    a = [25,1,4,3,3,12,2]
    insertion_sort(a, compare_int)
