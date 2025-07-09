def digit_root(num):
    if 0 < num < 10000000:
        num1 = []
        for i in str(num):
            num1.append(i)
        new_num = 0
        for i in num1:
            new_num += int(i)
        if new_num > 9:
            new_num1 = 0
            for i in str(new_num):
                new_num1 += int(i)
            if new_num1 > 9:
                new_num2 = 0
                for i in str(new_num1):
                    new_num2 += int(i)
                return new_num2
            else:
                return new_num1
        else:
            return new_num    
    else:
        print('Значение внедопустимого диапазона')