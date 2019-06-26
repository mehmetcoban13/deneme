def ebob():
    ebob = 1 #result
    list = [] #list that we will store the entered numbers
    counter = 0 #the number of valid positive integers that we will store in "list"
    i = int(input("Lütfen ebob'unu bulmak istediğiniz pozitif sayıları girin\
    \n(çıkmak için 0(sıfır) giriniz) \
    \nSayı giriniz : ")) # first input
    smallest = i #the variable that stores the smallest number which is entered by user
    while i != 0:
        list.append(i) #add the entered number to the list if it is not zero(0)
        if smallest > list[counter]: # if the value of "smallest" is greater than the last entered value
            smallest = i #then assign "smallest" to the new value
        counter += 1 #increment counter by one if the entered value is not zero
        i = int(input("Sayı giriniz : ")) #ask to user for a new value
        if i == 0 : #if new value equals to zero
            print("Hesaplanıyor...") #then deliver this message

    print() #leave a blank line
    if counter == 0: #if no valid value exists then return this message
        return "Lütfen geçerli pozitif sayılar giriniz !"
    else:
        for j in range(smallest, 1, -1): #from smallest number to 2
            ok=True
            for k in list: #check every number in list
                if k%j != 0: #whether they are divisible without reminder or not
                    ok=False
                    break
            if ok == True:
                ebob = j
                break
        return ebob
#end of ebob() function

print("ebob = ", ebob())
#comment line
#print("\nOrtalama =", ortalamaHesaplama())


