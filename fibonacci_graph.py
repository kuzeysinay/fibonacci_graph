from matplotlib import pyplot as plt

a = 1
b = 1

fibonacci = [a, b]

for i in range(40):
    a, b = b, a+b
    fibonacci.append(b)

x = list(range(1, len(fibonacci)+1))

y = fibonacci

plt.plot(x, y)
plt.title("Fibonacci Dizisi")
plt.ylabel("Fibonacci Sayısı")
plt.xlabel("X Ekseni")

plt.show()