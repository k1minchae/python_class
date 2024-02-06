P = str(input())

var = []
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

i = 1
while len(P) >= 1:
    if '+' not in P[1:] and '-' not in P[1:]:
        var.append(P)
        break
    if P[i] not in numbers:
        var.append(P[:i])
        P = P[i:]
        i = 1
    else:
        i += 1

sum_var = 0
for i in var:
    sum_var += int(i)
print(sum_var)