
numbers = [1,2,3,4,5]
sum = 0
for number in numbers:
    sum += number

print(sum)


words = ["peter","Agatha","Marv"]
new_list = []
for word in words:
    new_list.append(len(word))

print(new_list)


integers = [1,2,3,4,5,6,7,8,9,10]

for index in range(len(integers)):
    if index % 2 == 1:
        print(integers[index])
