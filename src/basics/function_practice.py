scale=1
def calculate_area(width, height=10, **kwargs):
    area = width * height
    unit = kwargs.get("unit", "平方单位")
    return f"{area} {unit}"
def update_scale(new_factor):
    global scale
    scale = new_factor
print(calculate_area(5))
print(calculate_area(5, height=8, unit="平方厘米"))
update_scale(10)
print(f"全局变量scale 已修改为: {scale}")
