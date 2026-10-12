import time
import sys


def print_slow(text, delay=0.5):
    """Печатает текст с задержкой для эффекта"""
    print(text)
    time.sleep(delay)


def print_typing(text, delay=0.02):
    """Печатает текст по буквам"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def solve_coins():
    print("=" * 60)
    print_typing("ЗАГАДКА О 12 МОНЕТАХ")
    print("=" * 60)
    time.sleep(0.5)

    # Ввод данных
    print("\nВведите номер фальшивой монеты (1-12):")
    fake = int(input())
    print("Фальшивая монета тяжелее или легче? (введите 'тяжелее' или 'легче'):")
    weight_type = input().strip().lower()

    if fake < 1 or fake > 12:
        print("Ошибка: номер монеты должен быть от 1 до 12")
        return
    if weight_type not in ['тяжелее', 'легче']:
        print("Ошибка: введите 'тяжелее' или 'легче'")
        return

    print("\n" + "=" * 60)
    print_typing("Условие задачи:")
    print("=" * 60)
    print_slow("У нас есть 12 монет, пронумерованных от 1 до 12.")
    print_slow("Одна из них фальшивая — она либо тяжелее, либо легче настоящих.")
    print_slow("У нас есть чашечные весы. За 3 взвешивания нужно найти фальшивку.")
    print_slow("Начинаем расследование...\n")

    # Функция для имитации взвешивания
    def weigh(left, right):
        def get_weight(coin):
            if coin == fake:
                return 2 if weight_type == 'тяжелее' else 0
            return 1

        left_weight = sum(get_weight(c) for c in left)
        right_weight = sum(get_weight(c) for c in right)

        if left_weight < right_weight:
            return -1
        elif left_weight > right_weight:
            return 1
        else:
            return 0

    def describe_weigh(left, right, result, coin_num):
        """Красиво описывает взвешивание"""
        left_str = ",".join(map(str, left))
        right_str = ",".join(map(str, right))
        print_slow(f"\nВзвешивание #{coin_num}: [{left_str}] vs [{right_str}]")
        time.sleep(0.8)

        if result == 0:
            print_typing("   Весы в равновесии - обе чаши одинакового веса")
        elif result == 1:
            print_typing("   Левая чаша перевесила")
        else:
            print_typing("   Правая чаша перевесила")
        time.sleep(0.7)

    # ============ ВЗВЕШИВАНИЕ 1 ============
    print("=" * 60)
    print_typing("РАССУЖДЕНИЕ:")
    print("=" * 60)
    print_slow("Разделим монеты на три группы по 4:")
    print_slow("   Группа A: 1, 2, 3, 4")
    print_slow("   Группа B: 5, 6, 7, 8")
    print_slow("   Группа C: 9, 10, 11, 12")
    print_slow("Сначала сравним группы A и B. Если они равны -")
    print_slow("фальшивка точно в группе C. Если нет - она в A или B.")

    result1 = weigh([1, 2, 3, 4], [5, 6, 7, 8])
    describe_weigh([1, 2, 3, 4], [5, 6, 7, 8], result1, 1)

    if result1 == 0:
        # ===== Фальшивка среди 9,10,11,12 =====
        print_slow("Вывод: монеты 1-8 настоящие.")
        print_slow("   Фальшивка среди 9, 10, 11, 12.\n")
        time.sleep(0.7)

        print_typing("РАССУЖДЕНИЕ:")
        print_slow("Возьмём монеты 9, 10, 11 и сравним с тремя настоящими (1, 2, 3).")
        print_slow("Если равновесие - фальшивка 12.")
        print_slow("Если левая тяжелее - одна из 9,10,11 тяжелее.")
        print_slow("Если левая легче - одна из 9,10,11 легче.\n")

        result2 = weigh([9, 10, 11], [1, 2, 3])
        describe_weigh([9, 10, 11], [1, 2, 3], result2, 2)

        if result2 == 0:
            print_slow("Вывод: 9, 10, 11 - настоящие.")
            print_slow(f"   Значит, фальшивая монета - 12!")
            fake_coin = 12
        elif result2 == 1:
            print_slow("Вывод: среди 9, 10, 11 есть ТЯЖЁЛАЯ монета.\n")
            time.sleep(0.7)
            print_typing("РАССУЖДЕНИЕ:")
            print_slow("Сравним 9 и 10. Если равны - фальшивка 11 (тяжёлая).")
            print_slow("Если 9 тяжелее - фальшивка 9. Если 10 тяжелее - фальшивка 10.\n")

            result3 = weigh([9], [10])
            describe_weigh([9], [10], result3, 3)

            if result3 == 1:
                fake_coin = 9
                print_slow("9 тяжелее 10 - фальшивая монета 9!")
            elif result3 == -1:
                fake_coin = 10
                print_slow("10 тяжелее 9 - фальшивая монета 10!")
            else:
                fake_coin = 11
                print_slow("9 и 10 равны - фальшивая монета 11!")
        else:  # result2 == -1
            print_slow("Вывод: среди 9, 10, 11 есть ЛЁГКАЯ монета.\n")
            time.sleep(0.7)
            print_typing("РАССУЖДЕНИЕ:")
            print_slow("Сравним 9 и 10. Если равны - фальшивка 11 (лёгкая).")
            print_slow("Если 9 легче - фальшивка 9. Если 10 легче - фальшивка 10.\n")

            result3 = weigh([9], [10])
            describe_weigh([9], [10], result3, 3)

            if result3 == -1:
                fake_coin = 9
                print_slow("9 легче 10 - фальшивая монета 9!")
            elif result3 == 1:
                fake_coin = 10
                print_slow("10 легче 9 - фальшивая монета 10!")
            else:
                fake_coin = 11
                print_slow("9 и 10 равны - фальшивая монета 11!")

    else:
        # ===== Фальшивка среди 1-8 =====
        if result1 == 1:
            print_slow("Вывод: группа A (1,2,3,4) тяжелее группы B (5,6,7,8).")
            print_slow("   Значит, либо одна из 1,2,3,4 ТЯЖЁЛАЯ,")
            print_slow("   либо одна из 5,6,7,8 ЛЁГКАЯ.")
            print_slow("   Монеты 9-12 точно настоящие.\n")
        else:
            print_slow("Вывод: группа A (1,2,3,4) легче группы B (5,6,7,8).")
            print_slow("   Значит, либо одна из 1,2,3,4 ЛЁГКАЯ,")
            print_slow("   либо одна из 5,6,7,8 ТЯЖЁЛАЯ.")
            print_slow("   Монеты 9-12 точно настоящие.\n")

        time.sleep(0.8)
        print_typing("РАССУЖДЕНИЕ:")
        print_slow("Теперь нужна хитрая комбинация. Поменяем монеты местами")
        print_slow("и добавим настоящие. Сравним: [1, 2, 5] vs [3, 6, 9]")
        print_slow("Здесь 9 - заведомо настоящая монета.\n")

        result2 = weigh([1, 2, 5], [3, 6, 9])
        describe_weigh([1, 2, 5], [3, 6, 9], result2, 2)

        if result1 == 1:  # Первое: левая была тяжелее
            if result2 == 0:
                print_slow("Равновесие! Значит, подозреваемые 1,2,3,5,6 - чистые.")
                print_slow("   Остаются: 4 (может быть тяжёлой), 7 (лёгкой), 8 (лёгкой).\n")
                time.sleep(0.7)
                print_typing("РАССУЖДЕНИЕ:")
                print_slow("Сравним 7 и 8. Если равны - 4 тяжелее.")
                print_slow("Если 7 легче - фальшивка 7. Если 8 легче - фальшивка 8.\n")

                result3 = weigh([7], [8])
                describe_weigh([7], [8], result3, 3)

                if result3 == -1:
                    fake_coin = 8
                    print_slow("8 легче 7 - фальшивая монета 8 (лёгкая)!")
                elif result3 == 1:
                    fake_coin = 7
                    print_slow("7 легче 8 - фальшивая монета 7 (лёгкая)!")
                else:
                    fake_coin = 4
                    print_slow("7 и 8 равны - фальшивая монета 4 (тяжёлая)!")
            elif result2 == 1:
                print_slow("Левая тяжелее. Значит, 1 или 2 тяжёлые, либо 6 лёгкая.")
                print_slow("   (5 и 3 исключаются - их перестановка не объясняет результат)\n")
                time.sleep(0.7)
                print_typing("РАССУЖДЕНИЕ:")
                print_slow("Сравним 1 и 2. Если равны - фальшивка 6 (лёгкая).")
                print_slow("Если 1 тяжелее - фальшивка 1. Если 2 тяжелее - фальшивка 2.\n")

                result3 = weigh([1], [2])
                describe_weigh([1], [2], result3, 3)

                if result3 == 1:
                    fake_coin = 1
                    print_slow("1 тяжелее 2 - фальшивая монета 1 (тяжёлая)!")
                elif result3 == -1:
                    fake_coin = 2
                    print_slow("2 тяжелее 1 - фальшивая монета 2 (тяжёлая)!")
                else:
                    fake_coin = 6
                    print_slow("1 и 2 равны - фальшивая монета 6 (лёгкая)!")
            else:  # result2 == -1
                print_slow("Правая тяжелее. Значит, 3 тяжёлая или 5 лёгкая.")
                print_slow("   (1, 2, 6 исключаются)\n")
                time.sleep(0.7)
                print_typing("РАССУЖДЕНИЕ:")
                print_slow("Сравним 3 с настоящей монетой 9.")
                print_slow("Если 3 тяжелее - фальшивка 3. Иначе - фальшивка 5.\n")

                result3 = weigh([3], [9])
                describe_weigh([3], [9], result3, 3)

                if result3 == 1:
                    fake_coin = 3
                    print_slow("3 тяжелее 9 - фальшивая монета 3 (тяжёлая)!")
                else:
                    fake_coin = 5
                    print_slow("3 не тяжелее 9 - фальшивая монета 5 (лёгкая)!")

        else:  # result1 == -1, левая была легче
            if result2 == 0:
                print_slow("Равновесие! Значит, 1,2,3,5,6 - чистые.")
                print_slow("   Остаются: 4 (может быть лёгкой), 7 (тяжёлой), 8 (тяжёлой).\n")
                time.sleep(0.7)
                print_typing("РАССУЖДЕНИЕ:")
                print_slow("Сравним 7 и 8. Если равны - 4 легче.")
                print_slow("Если 7 тяжелее - фальшивка 7. Если 8 тяжелее - фальшивка 8.\n")

                result3 = weigh([7], [8])
                describe_weigh([7], [8], result3, 3)

                if result3 == 1:
                    fake_coin = 8
                    print_slow("8 тяжелее 7 - фальшивая монета 8 (тяжёлая)!")
                elif result3 == -1:
                    fake_coin = 7
                    print_slow("7 тяжелее 8 - фальшивая монета 7 (тяжёлая)!")
                else:
                    fake_coin = 4
                    print_slow("7 и 8 равны - фальшивая монета 4 (лёгкая)!")
            elif result2 == 1:
                print_slow("Левая тяжелее. Значит, 5 тяжёлая или 3 лёгкая.\n")
                time.sleep(0.7)
                print_typing("РАССУЖДЕНИЕ:")
                print_slow("Сравним 3 с настоящей монетой 9.")
                print_slow("Если 3 легче - фальшивка 3. Иначе - фальшивка 5.\n")

                result3 = weigh([3], [9])
                describe_weigh([3], [9], result3, 3)

                if result3 == -1:
                    fake_coin = 3
                    print_slow("3 легче 9 - фальшивая монета 3 (лёгкая)!")
                else:
                    fake_coin = 5
                    print_slow("3 не легче 9 - фальшивая монета 5 (тяжёлая)!")
            else:  # result2 == -1
                print_slow("Правая тяжелее. Значит, 1 или 2 лёгкие, либо 6 тяжёлая.\n")
                time.sleep(0.7)
                print_typing("РАССУЖДЕНИЕ:")
                print_slow("Сравним 1 и 2. Если равны - фальшивка 6 (тяжёлая).")
                print_slow("Если 1 легче - фальшивка 1. Если 2 легче - фальшивка 2.\n")

                result3 = weigh([1], [2])
                describe_weigh([1], [2], result3, 3)

                if result3 == -1:
                    fake_coin = 1
                    print_slow("1 легче 2 - фальшивая монета 1 (лёгкая)!")
                elif result3 == 1:
                    fake_coin = 2
                    print_slow("2 легче 1 - фальшивая монета 2 (лёгкая)!")
                else:
                    fake_coin = 6
                    print_slow("1 и 2 равны - фальшивая монета 6 (тяжёлая)!")

    # Итог
    print("\n" + "=" * 60)
    print_typing("ИТОГОВЫЙ РЕЗУЛЬТАТ:")
    print("=" * 60)
    time.sleep(0.5)
    print_slow(f"   Фальшивая монета: N{fake_coin}")
    print_slow(f"   Она {weight_type} настоящих монет")
    time.sleep(0.5)

    if fake_coin == fake:
        print_typing("\n   Ответ правильный! Задача решена за 3 взвешивания!")
    else:
        print_typing(f"\n   Ошибка! Правильный ответ был: {fake}")

    print("=" * 60)


if __name__ == "__main__":
    solve_coins()
