def animals(chickens, cows, pigs):
        chickens  =     chickens * 2
        cows      =     cows * 4
        pigs      =     pigs * 4
        total_number_of_legs = chickens + cows + pigs
        return total_number_of_legs
if __name__ == '__main__':
    print(animals(3,5,2))