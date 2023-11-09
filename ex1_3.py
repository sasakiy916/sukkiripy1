weight = float(input("体重(kg)は >> "))
height = float(input("身長(cm)は >>")) / 100

bmi = weight / height / height
print(f"BMIは{bmi}です")