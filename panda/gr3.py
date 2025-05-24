import matplotlib.pyplot as plt
import numpy as np

# 1. Line Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.figure()
plt.plot(x, y, marker='o', linestyle='--', color='blue')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2. Bar Chart
x = ['A', 'B', 'C', 'D']
y = [5, 7, 3, 8]
plt.figure()
plt.bar(x, y, color='green')
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# 3. Horizontal Bar Chart
plt.figure()
plt.barh(x, y, color='orange')
plt.title("Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Category")
plt.show()

# 4. Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.figure()
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.figure()
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 6. Pie Chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [20, 30, 25, 25]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.figure()
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.axis('equal')
plt.show()

# 7. Box Plot
data = [7, 15, 13, 19, 21, 22, 20, 18, 15, 17]
plt.figure()
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

# 8. Stacked Area Plot
days = [1, 2, 3, 4, 5]
eating = [1, 2, 3, 4, 3]
sleeping = [7, 8, 6, 7, 8]
working = [8, 7, 8, 9, 8]
playing = [2, 2, 2, 1, 2]
plt.figure()
plt.stackplot(days, eating, sleeping, working, playing,
              labels=['Eating', 'Sleeping', 'Working', 'Playing'],
              colors=['m', 'c', 'r', 'y'])
plt.legend(loc='upper left')
plt.title("Stacked Area Plot")
plt.show()

# 9. Heatmap
data = np.random.rand(5, 5)
plt.figure()
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap")
plt.show()

# 10. Error Bar Plot
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
error = [1.5, 2.0, 1.0, 2.5]
plt.figure()
plt.errorbar(x, y, yerr=error, fmt='o', capsize=5, color='navy')
plt.title("Error Bar Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()