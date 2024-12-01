# """
# Мегатрейдер
#
# n - кол-во лотов
#
# 1. Сложность:
#     - по памяти: O(n).
#     - по времени: O(n*logn). Парсинг, покупка - O(n), но сортировка по доходности поднимет сложность до O(n*logn).
# 2. Задал горизонт на 5 лет и кол-во лотов в 1 млн.
# 3. 7, 45 минут.
# """

MAX_DAYS = 365 * 5
MAX_LOTS = 1_000_000

def calculate_profit(lot: list) -> int:
    day, name, price, quantity = lot
    nominal_value = 1000
    coupon_income = 30 * quantity  # Купонный доход за 30 дней
    redemption_income = quantity * (nominal_value - price * 10)  # Погашение (разовое)
    return coupon_income + redemption_income

if __name__ == '__main__':

    data = """2 2 8000
    1 alfa-05 100.2 2
    2 alfa-05 101.5 5
    2 gazprom-07 100.0 2
    """

    lines = data.strip().split('\n')
    N, M, S = map(int, lines[0].split())
    lots = []

    if N > MAX_DAYS:
        raise ValueError('Максимальный горизонт планирования 5 лет.')
    if M > MAX_LOTS:
        raise ValueError(f'Максимальное кол-во лотов {MAX_LOTS}.')

    for line in lines[1:]:
        day, name, price, quantity = line.split()
        lots.append((int(day), name, float(price), int(quantity)))

    # Вычисляем и сортируем по доходности
    profit_table = [(calculate_profit(lot), lot) for lot in lots]
    profit_table.sort(reverse=True, key=lambda x: x[0])

    total_income = 0
    purchased_lots = []
    for profit, lot in profit_table:
        day, name, price, quantity = lot
        total_cost = price * 10 * quantity
        if S >= total_cost:
            S -= total_cost
            total_income += profit
            purchased_lots.append(lot)

    print(total_income)
    for lot in purchased_lots:
        print(f"{lot[0]} {lot[1]} {lot[2]} {lot[3]}")
    print()
