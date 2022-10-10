import sys

def birthdayCakeCandles(ar):
    candles = 0

    max_arr = max(ar)
    #i is the index in ar
    for i in range(len(ar)):
        if ar[i] == max_arr:
            candles+=1

    print(candles)

if __name__ == '__main__':
    list = [2, 5, 5, 4]
    birthdayCakeCandles(list)
