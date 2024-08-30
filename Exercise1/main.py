

wiiprice = 100

money = float(input("How much money do you have? "))


wiis_affordable = int(money // wiiprice)


more_money_needed = wiiprice - (money % wiiprice)



if money < 100:
    print("You can't afford Nintendo Wiis.")
    print("You need", more_money_needed,"more to afford a Wii.")

elif wiis_affordable >0:
    print("You can", wiis_affordable, "afford  Nintendo Wiis.")
    print("You need",more_money_needed, "more to afford another Wii.")

factorial = 1
x = int (input("Enter a number: "))
for a in range(1, x+1):
    factorial = factorial * a
print("The Factorial of ",x, "is", factorial)


factors = 1
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i,"is a factor of ",num)

factorList = []
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        factorList.append(i)
print("The factors of", x,"are: ",factorList)
