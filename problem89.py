import time

tStart = time.time()

def ConvertRomanNumeralToNumber(roman_numeral):
    number_result = 0
    roman_numerals = {
        1:"I", 4:"IV", 5:"V", 9:"IX",
        10:"X", 40:"XL", 50:"L",
        90:"XC", 100:"C", 400:"CD",
        500:"D", 900:"CM", 1000:"M"}
    # Iterate through the roman numerals.  But you see here that I sort them to 
    # get the largest string size first: "CD" comes before "I" 
    for numeral_value in sorted(roman_numerals,
                                key=lambda roman: len(roman_numerals[roman]),
                                reverse=True):
        keep_converting = True
        while keep_converting:            
            if roman_numeral.find(roman_numerals[numeral_value]) != -1:
                number_result += numeral_value
                roman_numeral = roman_numeral.replace(roman_numerals[numeral_value], "", 1)
            else:
                keep_converting = False
    return number_result


def int2roman(number):
    numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL",
                50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
    result = ""
    for value, numeral in sorted(numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result

filename = "roman.txt"
f = open(filename,"r")
text = f.readline() 
data = []
while len(text) != 0:
    data.append(text)
    text = f.readline() 
for x in range(len(data)):
    data[x] = str(data[x]).rstrip()
#print (data)

saved = 0
isChanged = True

for x in data:
    number = 0
    #convert x to integer
    number = ConvertRomanNumeralToNumber(x)

    #convert number to roman numeral
    simplified = ""
    simplified = int2roman(number)
    print (x,"  >  ", number, "  >  ",simplified, " saved: ", len(x) - len(simplified) )
    saved = saved + (len(x) - len(simplified))

print (saved)


# if isChanged = false, then the string is already in reduced form



print ("Run Time = " , str(time.time() - tStart))