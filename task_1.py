# 1 Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = []
        if len(self.input) == len(other.input):
            for line1, line2 in zip(self.input, other.input):
                if len(line1) != len(line2):
                    raise ValueError

                line_sum = [i + j for i, j in zip(line1, line2)]
                answer.append(line_sum)
        else:
            raise ValueError
        return Matrix(answer)

m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[2, 2, 2], [3, 3, 3]])
print(m1)
print('*'*2)
print(m2)
print('*'*2)
print(m1 + m2)