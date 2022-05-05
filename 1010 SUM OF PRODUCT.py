a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = float(c)

d, e, f = input().split(" ")
d = int(d)
e = int(e)
f = float(f)

pr_1 = b*c
pr_2 = e*f

valor_total = pr_1+pr_2

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')