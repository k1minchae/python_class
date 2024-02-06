P = str(input())

cal = 0
for i in range(len(P)):
    for j in range(i+1, len(P)):
        if P[i] == '[' and P[j] == ']':
            cal += int(P[i+1:j])
            break
        if P[i] == '{' and P[j] == '}':
            cal *= int(P[i+1:j])
            break
print(cal)