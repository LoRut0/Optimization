import pandas
import matplotlib.pyplot as pyplot

df = pandas.read_csv("function.csv")
df.plot(kind = "scatter", x = "x", y = "y")
minimum = df.idxmin()
y_min_index = minimum.iloc[1]
minimum_coords = df.iloc[y_min_index]
x_min = minimum_coords.iloc[0]
y_min = minimum_coords.iloc[1]
print(f"x точки минимума: {x_min}")
print(f"y точки минимума {y_min}")
pyplot.scatter(x_min, y_min, c='r', label='minimum')
pyplot.legend()
pyplot.show()