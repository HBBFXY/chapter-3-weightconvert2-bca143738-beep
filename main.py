while True:
    try:
        current_weight = float(input("请输入你当前在地球上的体重(kg): "))
        if current_weight > 0:
            break
        else:
            print("体重必须是正数，请重新输入。")
    except ValueError:
        print("输入无效，请输入一个数字。")

# 打印表头
print("\n未来10年地球和月球上的体重变化:")
print("年份 | 地球上的体重(kg) | 月球上的体重(kg)")
print("-" * 45)

# 计算并输出未来10年的体重变化
for year in range(10):
    earth_weight = current_weight + year * 0.5
    moon_weight = earth_weight * 0.165
    print(f"{year+1:4d} | {earth_weight:16.2f} | {moon_weight:16.2f}")
