"""
Usa programación dinámica para resolver el problema de cortar la cuerda de la siguiente tabla.
Encuentra para la cuerda de largo 11 cual sería el precio máximo para venderla, así como la descomposición óptima.

largo	1	2	3	4	5	6	7	8	9	10	11
precio	1	4	10	12	15	20	21	32	31	41	51
"""


def cutRod(price:list[int], n:int):
    """
    price list[int]
    n int
    """
    val = [0 for x in range(n+1)]
    rod_lengths = [0 for x in range(n+1)]

    for i in range(1, n+1):
        max_value = float('-inf')
        for j in range(1, i+1):
            if max_value < (price[j-1] + val[i-j]):
                max_value = price[j-1] + val[i-j]
                rod_lengths[i] = j
        val[i] = max_value
    return val, rod_lengths


def decompose(n, val, rod_lengths):
    while n > 0:
        print('Length included in sol',rod_lengths[n])
        n = n - rod_lengths[n]

if __name__ == "__main__":
    price_list = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]
    #price_list = [1, 5, 8, 9, 10, 17, 17, 20]
    #n = 8
    n = 11
    value_list, rod_lengths = cutRod(price_list, n)
    max_price = value_list[n]
    decompose(n, value_list, rod_lengths)
    print('Maximum price', max_price)