# test = [1, 2, 3, 4, 5,]

# def mean_normalize(var):
#     normalized_var = []
#     mean_var = sum(var) / len(var)

#     for i in var:
#         normalized_var.append(i - mean_var)
#     return normalized_var

# mean_normalize([1, 2, 3, 4, 5]), mean_normalize([11, 22, 33, 44, 55])


def dot_product(x, y):
    total = 0
    for i in range(len(x)):
        total += x[i] * y[i]
    return total

a = [1, 2, 3]
b = [4, 5, 6]

dot_product(a,b)

