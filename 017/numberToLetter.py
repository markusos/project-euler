#!/usr/bin/python

numbers = ["",
    "one",	 
    "two",
    "three",	
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty"]

tens = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"]

def numberToLetters(number):
    i = number
    number = "000" + str(number)
    singular = int(number[len(number) - 1])
    ten = int(number[len(number) - 2])
    hundred = int(number[len(number) - 3])
    tenAndSingular = int(str(ten) + str(singular))
    
    if i < 20:
        return numbers[tenAndSingular]
    elif i < 100:
        return tens[ten] + numbers[singular]
    elif i < 1000:
        if int(ten) == 0 and int(singular) == 0:
            return numbers[hundred] + " hundred"
        elif int(tenAndSingular) < 20:
            return numbers[hundred] + " hundred and " + numbers[tenAndSingular]
        elif int(singular) == 0:
            return numbers[hundred] + " hundred and " + tens[ten]
        else:
            return numbers[hundred] + " hundred and " + tens[ten] + "-" + numbers[singular]
    elif i == 1000:
        return "one thousand"
    else:
        return "N/A"

def countLetters(numberRange):
    nrOfLetters = 0
    for i in numberRange:
        nrOfLetters += len(numberToLetters(i).replace(" ", "").replace("-", ""))
    return nrOfLetters
