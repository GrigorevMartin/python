score = 0
print("привет!Поиграем в города?Ты должен назвать город название которого начинается с последней буквы моего города!"
      " например Брянск!")
city = input("введите город:")
if city[0].lower == "к":
    score += 1
    print("отлично")
print("теперь твой город - Калининград")
city = input("введите город:")
if city[0].lower == "д":
    score += 1
    print("отлично")