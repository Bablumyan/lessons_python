"""Python Logical Operators"""
x = 10
z = x < 5 and x < 10    #returns true if both statements are true
print(z)

a = 55
result = a < 5 or a < 100 #returns true if one of statements is true
print(result)

""" Python identity operators """
#is - returns true if both variables are the same object
#is not - returns true if bothe variables are not the same object

""" Python membership operators"""
#in - returns true if sequence with specified value is prsent in the object
#not in - returns true if a sequence with the specified value is not present in the object

""" Python Bitwise """
#&(AND) - Sets each bit to one both bits are one
#|(OR) - Sets each bit to one if one of two bits is 1
#^(XOR) - 7^10: 1^1 = 3 --Need to review
print(1^5)

#~(NOT) - Inverts all the bits
#<<  Zero fill left shift  Shift left by pushing zeros in from the right and let the leftmost bits fall off
#>>  Signed right shift  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off