


# def get_variance(data):
#     n = len(data)
#     if n == 0:
#         return None
#     sample_mean = sum(data) / n
#     sum_of_squares = 0
#     for i in data:
#         sum_of_squares += (i - sample_mean) ** 2
#     variance = sum_of_squares / (n - 1)
#     return variance


# test1 = [1, 2, 3, 5, 5, 4]
# test2 = [1, 1, 1, 2, 3, 4, 5, 5, 5]
# print(get_variance(test1)) # 2.67
# # print(get_mean(test1)) # 3.33
# print(get_variance(test2)) # 3.25


# from math import sqrt

# def get_standard_deviation(data):
#     variance = get_variance(data)
#     stddev = sqrt(variance)
#     return round(stddev, 2)

# test = [120,112,131,211,312,90]
# print(get_standard_deviation(test))


def get_variance(data):
    n = len(data)
    if n == 0:
        return None
    sample_mean = sum(data) / n
    sum_of_squares = 0
    for i in data:
        sum_of_squares += (i - sample_mean) ** 2
    variance = sum_of_squares / (n - 1)
    return variance

test1 = [1, 2, 3, 5, 5, 4]
test2 = [1, 1, 1, 2, 3, 4, 5, 5, 5]
print(get_variance(test1)) # 2.67
# print(get_mean(test1)) # 3.33
print(get_variance(test2)) # 3.25