# Fluthfi
for f in range(0, 10):
    print()
    print(f, end="\t")
    for a in range(1, 10):
        print(f + a, end="\t")

# 6xatz
for f in range(10):
    row = [f + a for a in range(1, 10)]
    print(f, *row, sep="\t")
