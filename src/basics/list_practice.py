import sys
sys.stdout.reconfigure(encoding='utf-8')
num = [3, 1, 4, 1, 5, 9, 2, 6]
num.append(5)
num.remove(1)
num.sort()
print(f"排序后列表: {num}")
print(f"倒数第三个元素: {num[-3]}")
print(f"前三个元素的切片: {num[:3]}")

scores = {"Alice": 85, "Bob": 90, "Charlie": 78}
scores["Charlie"] = 92
scores["David"] = 88
del scores["Alice"]
print(f"所有键: {list(scores.keys())}")
print(f"Bob 的分数: {scores.get('Bob', '不存在')}")
print(f"Eve 的分数: {scores.get('Eve', '不存在')}")

squared = {k: v ** 2 for k, v in scores.items() if v > 80}
print(f"分数大于80的平方: {squared}")