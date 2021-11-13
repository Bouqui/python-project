# import RegEx packages
import re

class sortPage():

    def sortString(string):
        # extract digits from the string using RegEx
        # treat two numeric characters that follow each other as a single value
        x = re.findall(r'\d+', string)

        # extract letters from the string using RegEx
        y = re.findall(r'[a-zA-Z]', string)

        # extract special charactees from the string using RegEx
        z = re.findall(r'[@_!#$%^&*()<>?/\|}{~:]', string)

        # sort the numbers in ascending order
        x.sort(reverse=True)

        # sort the letter in a way that the uppercase comes first
        y.sort(reverse=True)

        # concatenate the list
        b = x + y + z

        # convert the list to string
        sortedString = ''.join(b)

        return sortedString


    #print(sortString("kOJkdsmdb%$8jj10"))