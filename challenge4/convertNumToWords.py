one_twenty = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
              "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ", "decillion "]


def convert_num_to_words(num):
    if num < 20:
        if num == 0:
            return "zero"
        return one_twenty[num]
    else:
        # break the numbers into groupings of 3 digits xxx,yyy,zzz
        # Maybe convert the number to a string then slice the string
        # and make a list of the slices
        num_string = str(num)
        digits = list(num_string)


    stNumber = str(num)
    return stNumber
