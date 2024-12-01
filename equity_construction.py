"""
Долевое строительство

n - кол-во долей

1. Сложность:
    - по памяти: O(n).
    - по времени: O(n).
2. Задал как 1 млн, операции займут миллисекунды.
3. 2/10, 12 минут.
"""

MAX_SHARES = 1_000_000


def calc_percentage(shares: list) -> list:
    shares_overall = sum(shares)
    perc = [(f"{i / shares_overall:.3f}") for i in shares]
    return perc


if __name__ == '__main__':

    n = int(input('Введите число долей: '))
    if n > MAX_SHARES:
        raise ValueError(f'Введите число не больше {MAX_SHARES}.')

    shares = []

    for i in range(n):
        share = float(input(f'Введите долю {i + 1}: '))
        shares.append(share)

    result = calc_percentage(shares)

    for val in result:
        print(val)
