# Names scores

## Problem Statement

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score. For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714. What is the total of all the name scores in the file?

## Solution
When I saw this problem, I immediately thought of ASCII - the original american standard for encoding text in computers. I checked if python supports extracting this, and it does through the function ord(), which I've used in other languages before. I used this knowledge to write a simple function that returns a value of the sume of the characters of a string (with an offsset value - as the capital letters start at 65, I need to subtract 64 to start counting forward from 1).

After this it was a simple matter of opening the file, reading it, removing quotation marks, splitting on commas, sorting, and then summing over the multiples of name values by their indices.