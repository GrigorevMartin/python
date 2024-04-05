import  random
fruits = ['apple', 'banana','grape', 'qiwi', 'orange', 'watermelon']
tools = ['saw', 'screwdriver','hammer', 'ladder', 'paintbrush', 'drill']
vedgetables = ['tomato', 'cucumber', 'cabbage', 'carrot', 'pumpkin', 'potato']
materials = ['paper', 'leather','concrete', 'wood', 'plastic', 'copper']
gadgets = ['PC', 'microfone','smartphone', 'TV', 'game console', 'monitor']
clothes = ['scarf', 'cap','t shirt', 'shirt', 'skirt', 'dress']
array_of_arrays = [fruits,tools,vedgetables,materials,gadgets,clothes]
print('Hello! Please choose extra word!')
print('--------------------------------')
current_array = random.randrange(0, len(array_of_arrays))
for i in range(1,len(fruits)):
    print(i,'.', fruits[i])
print(array_of_arrays[current_array])


