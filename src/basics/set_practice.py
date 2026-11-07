set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"交集: {set_a & set_b}")
print(f"并集: {set_a | set_b}")
print(f"差集 (A-B): {set_a - set_b}")

point = (10, 20)
try:
    point[0] = 15
except TypeError as e:
    print(f"元组不可变： {e}")