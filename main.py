import matplotlib.pyplot as plt

v = [i * 0.00001 for i in range(4, 100)]


def dav(t):
    p = [(8.314 * t / (j - (3.19 * 10 ** -5))) - 0.1382 / j ** 2 for j in v]
    return p

fig = plt.figure(figsize = (15,5))
t0 = -140

for i in range(5):
    plt.subplot(1,5,i +1)
    if i == 2:
        plt.plot(v, dav(t0 + 273.15), color='red')
    else:
        plt.plot(v, dav(t0 + 273.15))
    plt.xlabel('V')
    plt.ylabel('P')
    t0 += 10

plt.show()

def dav2(j):
    p = (8.314 * (-130 + 273.15) / (j - (3.19 * 10 ** -5))) - 0.1382 / j ** 2
    return p

a = 0
b = 10 ** -4
while abs(a - b) > 0.00002:
        c = a + (b - a) / 3
        d = b - (b - a) / 3
        if dav2(c) > dav2(d):
            a = c
        else:
            b = d

mi = (a + b) / 2
print('Минимум:', mi)

a = 10 ** -4
b = 5 * 10 ** 4
while abs(a - b) > 0.00002:
        c = a + (b - a) / 3
        d = b - (b - a) / 3
        if dav2(c) < dav2(d):
            a = c
        else:
            b = d

ma = (a + b) / 2
print('Максимум:', ma)

s = 0
for i in range(round(mi * 10 ** 7), round(ma * 10 ** 7)):
    d = ((dav2(i * 0.0000001 + 0.0000001) - dav2(i * 0.0000001)) ** 2 + 10 ** -14) ** 0.5
    s += abs(d)

print("Длина кривой в запрещённой зоне", s)


pn = 3664186.998
a = 3.20 * 10 ** -5
b = mi
for i in range(3):

    while abs(dav2(a) - dav2(b)) > 0.0000002:
            c = (a + b) / 2
            if (dav2(a) - pn) * (dav2(c) - pn) < 0:
                b = c
                continue
            elif (dav2(b) - pn) * (dav2(c) - pn) < 0:
                a = c
                continue
            else:
                print(round(c, 7))
                break
    else:
        print(round((a + b) / 2, 7))

    if i == 0:
        a = mi
        b = ma
    else:
        b = ma
        a = ma + 0.001


su = 0
for i in range(round(6.15 * 10 ** 2), round(0.0001948 * 10 ** 7)):
    i *= 10 ** -7
    d = dav2(i + 10 ** -7) + dav2(i) * 5 * (10 ** -8)
    su += d

print("Интеграл 1:", su * 10 ** -7)

print("Интеграл 2:", (0.0001948 - 6.15e-05) * 3664186.998)