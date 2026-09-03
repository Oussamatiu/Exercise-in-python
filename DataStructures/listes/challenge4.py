temperatures = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]

temperatures_sup_25 = [x for x in temperatures if x > 25]

print(temperatures_sup_25)

temperatures_infu_25 = [ x for x in temperatures if x <= 25 ]

temperatures_between_20_30 = [ x for x in temperatures if 20 <= x <= 30 ]

print(temperatures_between_20_30)

temperatures_sup_30 = [x for x in temperatures if x > 30]

print(temperatures_sup_30)