one_twenty = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
              "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ", "decillion "]


def breakItUp(num):
    pass


def convertNumToWords(num):
    if num < 20:
        if num == 0:
            return "zero"
        return one_twenty[num]
    elif num >= 1000:
        # break the numbers into groupings of 3 digits xxx,yyy,zzz
        breakItUp(num)
    else:
        pass

    stNumber = str(num)
    return stNumber
