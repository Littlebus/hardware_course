import random

data = []

if __name__ == '__main__':
    for i in range(0,10):
        data.append(random.randint(0,99))
    print(data)

    count = len(data)

    for i in range(count-1,0,-1):
        for j in range(0, i):
            if data[j] < data[j+1]:
                data[j] ^= data[j+1]
                data[j+1] ^= data[j]
                data[j] ^= data[j+1]
    print(data) 