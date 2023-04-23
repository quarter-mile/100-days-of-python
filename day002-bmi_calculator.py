height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

fl_h = float(height)
fl_w = float(weight)

bmi =  fl_w/ fl_h ** 2

print(int(bmi))
