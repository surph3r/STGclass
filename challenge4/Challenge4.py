import unittest
from fibonacci import fibonacci as fib
from convertNumToWords import convert_num_to_words as num_words

# I found this built-in lib before writing my own (redundant) function, so I'm also using it, but for other things
from num2words import num2words


class Challenge4(unittest.TestCase):

    def setUp(self):
        # code to start webdriver
        # self.driver = webdriver.Chrome("../chromedriver.exe")
        pass

    def tearDown(self):
        # code to close webdriver
        # self.driver.close()
        pass

    def test_challenge4(self):
        # code for our test steps
        my_nums = [9, 13, 144, 7408, 98765]
        my_num_ords = []
        for i in range(len(my_nums)):
            item_ord = num2words(my_nums[i], ordinal=True)
            item_ord = item_ord.replace('-', ' ')
            item_ord = item_ord.replace('and ','')
            my_num_ords.append(item_ord)

        for i in range(len(my_nums)):
            print('The ' + my_num_ords[i] + ' Fibonacci number is ' + str(fib(my_nums[i])) + ' - words')
        # fib_num = fibonacci(my_num)
        # fib_num_words = fibonacci(fib_num)
        # word_salad = num2words(fib_num)
        # word_salad = word_salad.replace('-', ' ')
        #
        # print('The ' + my_num_ord + ' Fibonacci number is: ' + str(fib_num) + ' - ' + word_salad)


if __name__ == '__main__':
    unittest.main()
