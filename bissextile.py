def leapyear(X):
    if X%400==0 or (X%4==0 and X%100!=0) :
        return  True
    else:
        return False
    
year=int(input("enter a year: "))
B=leapyear(year)
if B==  True:
    print("this year is a leep year")
else:
    print("this year is not a leep year")


