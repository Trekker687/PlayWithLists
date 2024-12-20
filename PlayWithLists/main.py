L = input("Enter the list values separated by spaces")
X = L.split()
X = [float(i) for i in X]

total = sum(X)
avg = total/len(X)

print("Sum = ", total)
print("Average =", avg)

X.sort()
print("Smallest element: ", X[0])
print("Largest element: ", X[-1])
