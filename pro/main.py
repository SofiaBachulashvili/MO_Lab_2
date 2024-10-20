"""
Точка входа программы, инициирует параметры и запускает симплекс-метод.
"""

from sim.simplex import to_dual_task, simplexsus # from sim.simplex import * # all


def main():
    """
    Точка входа программы - инициализация значений и вызов симплекс-метода.
    """
    minimize = False                            # Необходимость минимизации
    c = [3, 1, 4]  # Коэффициенты целевой функции
    A = [[2, 1, 1], [1, 4, 0], [0, 0.5, 1]]  # Ограничения
    b = [6, 4, 1]  # Правая часть ограничений
    f = 0

    c, A, b, minimize = to_dual_task(c, A, b, minimize)
    print("[ + ] Ans:", simplexsus(c, A, b, f, minimize))

    return 0


if __name__ == "__main__":
    main()