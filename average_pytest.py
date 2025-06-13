# Только положительные числа
def test_only_pos_1():
    res = calculate_average([10, 3, 2])
    assert res == 5


def test_only_pos_2():
    res = calculate_average([1, 3, 4])
    assert res == 2.67


# Только отрицательные числа
def test_only_neg_1():
    res = calculate_average([-1, -2, -3])
    assert res == -2


def test_only_neg_2():
    res = calculate_average([-7, -2, -1, -2])
    assert res == -3


# Пустой список
def test_none():
    res = calculate_average([])
    assert res is None


def calculate_average(numbers: list[float]):
    sum = 0
    for num in numbers:
        sum += num
    if not numbers:
        return None
    else:
        return float(format(sum / len(numbers), '.2f'))


def show_result(data):
    if data is None:
        print(f'Список пуст')
    else:
        print(f"Среднее арифметическое - {data}\n")
    print('by Kirsanov Platon')


def main():
    input_list_1 = input('Пожалуйста, введите числа через пробел:\n').split()
    input_list_2 = []
    for x in input_list_1:
        input_list_2.append(float(x))
    result = calculate_average(input_list_2)
    show_result(result)


if __name__ == '__main__':
    main()
