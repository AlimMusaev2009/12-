def solve_coins():
    fake = int(input("Введите номер фальшивой монеты (1-12): "))
    weight_type = input("Фальшивая монета тяжелее или легче? (тяжелее/легче): ").strip().lower()
    
    if fake < 1 or fake > 12 or weight_type not in ['тяжелее', 'легче']:
        print("Ошибка ввода")
        return
    
    def weigh(left, right):
        def w(c):
            if c == fake:
                return 2 if weight_type == 'тяжелее' else 0
            return 1
        l = sum(w(c) for c in left)
        r = sum(w(c) for c in right)
        return (l > r) - (l < r)
    
    r1 = weigh([1,2,3,4], [5,6,7,8])
    
    if r1 == 0:
        r2 = weigh([9,10,11], [1,2,3])
        if r2 == 0:
            fake_coin = 12
        elif r2 == 1:
            r3 = weigh([9], [10])
            fake_coin = 9 if r3 == 1 else 10 if r3 == -1 else 11
        else:
            r3 = weigh([9], [10])
            fake_coin = 9 if r3 == -1 else 10 if r3 == 1 else 11
    else:
        r2 = weigh([1,2,5], [3,6,9])
        if r1 == 1:
            if r2 == 0:
                r3 = weigh([7], [8])
                fake_coin = 8 if r3 == -1 else 7 if r3 == 1 else 4
            elif r2 == 1:
                r3 = weigh([1], [2])
                fake_coin = 1 if r3 == 1 else 2 if r3 == -1 else 6
            else:
                r3 = weigh([3], [9])
                fake_coin = 3 if r3 == 1 else 5
        else:
            if r2 == 0:
                r3 = weigh([7], [8])
                fake_coin = 8 if r3 == 1 else 7 if r3 == -1 else 4
            elif r2 == 1:
                r3 = weigh([3], [9])
                fake_coin = 3 if r3 == -1 else 5
            else:
                r3 = weigh([1], [2])
                fake_coin = 1 if r3 == -1 else 2 if r3 == 1 else 6
    
    print(f"Фальшивая монета: {fake_coin} ({weight_type})")
    print("Верно!" if fake_coin == fake else f"Ошибка! Правильно: {fake}")

solve_coins()
