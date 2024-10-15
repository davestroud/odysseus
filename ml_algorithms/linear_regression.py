x = [1,2, 3, 4, 5]
y = [2, 4, 5, 8, 10]

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
denominator = sum((xi - mean_x) ** 2 for xi in x)

beta_1 = numerator / denominator
beta_0 = mean_y - beta_1 * mean_x

print(f"C")