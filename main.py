## 假设初始地球体重为55公斤
initial_weight = 55
moon_ratio = 0.165
earth_weight = initial_weight
print("年份\t地球体重(公斤)\t月球体重(公斤)")
for year in range(1, 11):
  moon_weight = earth_weight * moon_ratio
  print("第{}年\t{:.2f}\t\t{:.2f}".format(year, earth_weight, moon_weight))
  earth_weight += 0.5 在这个文件里编写代码
