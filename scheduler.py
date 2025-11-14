from pulp import *


class Scheduler:
    """
        Class that contains the core functionality of the scheduling model.
    """

    def __init__(self, n, m, a: int, b: list[list[int]], c: list[int], d: list[int], p: list[int]):
        """
        Constructs the problem model and variables.

        :param n: Number of tasks.
        :param m: Number of slots.
        :param a: Maximum number of slots without break.
        :param b: Slot block constraints for each task. Can be used to set start and end time for task.
        :param c: Global slot block constraints.
        :param d: Duration of each task. (slots)
        :param p: Priority of each task.
        """
        self.f = LpVariable.dicts('f', range(n), cat='Binary')
        self.x = LpVariable.dicts('x', (range(n), range(m)), cat='Binary')
        self.model = LpProblem('Schedule', LpMaximize)

        # Add global slot block constraints
        for j in range(m):
            self.model += lpSum(self.x[i][j] for i in range(n)) <= c[j]

        # Add local slot block constraints
        for i in range(n):
            for j in range(m):
                self.model += self.x[i][j] <= b[i][j]

        # Add finish task constraints
        for i in range(n):
            self.model += lpSum(self.x[i][j] for j in range(m)) == d[i] * self.f[i]

        # Add break constraint
        for j in range(max(0, m - a - 1)):
            self.model += lpSum(self.x[i][k] for i in range(n) for k in range(j, j + a + 1)) <= a

        # Add objective function
        self.model += lpSum(self.f[i] * p[i] for i in range(n))

    def get_model(self):
        return self.model

    def get_x(self):
        return self.x

    def get_f(self):
        return self.f


# Example usage
# n = 3
# m = 3
# a = 1
# b = [[0, 1, 1], [1, 0, 1], [1, 1, 1]]
# c = [1, 1, 1]
# d = [1, 1, 1]
# p = [3, 1, 1]
# sc = Schedule(n, m, a, b, c, d, p)
#
# sc_model = sc.get_model()
# print(sc_model)
# sc_model.solve()
# print(LpStatus[sc_model.status])
# f = sc.get_f()
# x = sc.get_x()
# for i in range(n):
#     print(f[i].value())
#
# for i in range(n):
#     for j in range(m):
#         print(x[i][j].value(), end=' ')
#     print()
