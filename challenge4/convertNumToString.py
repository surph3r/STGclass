def convertNumToString(num):

    one_twenty = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
            "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion "]

    if num < 20:
        return one_twenty[num]

    words = str(num)
    return words
