import random
import sys
def generate(n):
    return [[random.randint(0, 1) for __ in range(n)]for _ in range(n)]

if __name__ == "__main__":
    mtx = generate(int(sys.argv[1]))
    n = len(mtx)
    print(f"{n} {n}")
    print("\n".join([" ".join(map(str,row)) for row in mtx]))
    print("0 0")