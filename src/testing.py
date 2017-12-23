
f = open('../data/data.txt', 'r')
g = open('../data/categories.txt', 'w')

n = int(f.readline())
for i in range(n):
    f.readline()
    g.write(f.readline())

g.close()