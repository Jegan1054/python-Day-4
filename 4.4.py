string = input("Enter any string : ")
i=input("charactr to be deleted")

# Solution

new_string = ""

for j in string:
    if j == i or j == i:
        continue
    else:
        new_string += j

print(new_string)