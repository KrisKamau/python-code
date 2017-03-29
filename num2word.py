#Author: Kris Kamau

#num2word: int -> string
#Purpose: takes in an integer number and returns it's word format
#Example: 22 -> twenty-two

#Constraints: 0 <= number <= 1,000,000,000
def num2word(num):

    values = { 1 :"one", 2 :"two", 3 :"three", 4 :"four", 5 :"five",
               6 :"six", 7 :"seven", 8 :"eight", 9 :"nine", 10:"ten",
               11 :"eleven", 12 :"twelve", 13 :"thirteen", 14 :"fourteen",
               15 :"fifteen", 16 :"sixteen", 17 :"seventeen", 18 :"eighteen",
               19 :"nineteen", 20 :"twenty", 30 :"thirty", 40 :"forty",
               50 :"fifty", 60 :"sixty", 70 :"seventy", 80 :"eighty",
               90 :"ninety", 0 :"zero" }

    if(num < 100):
        if((num < 20) or ((num % 10) == 0)):
            return(values[num])
        else:
            return(values[num - (num % 10)] + "-" + num2word(num % 10))
    elif(num < 1000):
        return(values[num // 100] + " hundred and " + num2word(num % 100))
    elif(num < 1e6):
        return(num2word(num // 1000) + " thousand, " + num2word(num % 1000))
    elif(num < 1e9):
        return(num2word(num // 1e6) + " million, " + num2word(num % 1e6))
    elif(num == 1e9):
        return("One billion")
    else:
        return("Number too large")
    
 
