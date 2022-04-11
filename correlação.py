x = list(map(float, input('Digite os valores para X: ').split()))  # obtem os valores para X e os coloca em uma lista
y = list(map(float, input('Digite os valores para Y: ').split()))  # obtem os valores para Y e os coloca em uma lista
xy = []  # cria uma lista para armazenar os produtos da multiplicação entre X e Y
x2 = []  # cria uma lista para armazenar os valores resultantes de cada valor em X ao quadrado
y2 = []  # cria uma lista para armazenar os valores resultantes de cada valor em Y ao quadrado

# adiciona às listas criadas seus devidos valores
for i in range(len(x)):
    xy.append(x[i] * y[i])
    x2.append(x[i] ** 2)
    y2.append(y[i] ** 2)

# calcula o r de Pearson
r1 = (len(x) * sum(xy) - sum(x) * sum(y))
r2 = (len(x) * sum(x2) - sum(x) ** 2) ** 0.5 * (len(x) * sum(y2) - sum(y) ** 2) ** 0.5
r = r1 / r2

# faz uma tabela com os valores armazenados na lista
print(f"{'x':^10}|{'y':^10}|{'xy':^10}|{'x2':^10}|{'y2':^10}")
for i in range(len(x)):
    print(f"{x[i]:^10}|{y[i]:^10}|{xy[i]:^10}|{x2[i]:^10}|{y2[i]:^10}")

print("_"*50)
print(f"{sum(x):^10}|{sum(y):^10}|{sum(xy):^10}|{sum(x2):^10}|{sum(y2):^10}")
# imprime o r de Pearson
print(f"\nr de Pearson: {r:.4f}")
