while True:
    try:
        current_weight = float(input("请输入您当前在地球上的体重(kg)："))
        if current_weight > 0:
            break
        else:
            print("体重必须为正数，请重新输入！")
    except ValueError:
        print("输入格式错误，请输入数字！")

# 打印标题和表头
print("\n" + "=" * 50)
print("{:^50}".format("未来10年地球与月球体重变化表"))
print("=" * 50)
print("{:^6} | {:^18} | {:^18}".format("年份", "地球上的体重(kg)", "月球上的体重(kg)"))
print("-" * 50)

# 计算并输出未来10年的体重情况
for year in range(1, 11):
    earth_weight = current_weight + (year - 1) * 0.5
    moon_weight = earth_weight * 0.165
    print("{:^6d} | {:^18.2f} | {:^18.2f}".format(
        year, earth_weight, moon_weight
    ))

print("=" * 50)
