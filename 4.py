a = [str(num) for num in range(20, 101) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
print(','.join(a))