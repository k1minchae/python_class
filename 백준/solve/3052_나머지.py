arr = [int(input()) for _ in range(10)]
result = []
for i in arr:
    if i % 42 == 0:
        result.append('0')
    else:
        result.append(i % 42)

result = set(result)
print(len(result))