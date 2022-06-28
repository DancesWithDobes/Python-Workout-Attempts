#reinvent the sumfunction

from ast import alias
from textwrap import dedent


def mySumFunction(*numbers):

    numSum = 0

    for number in numbers:
        numSum = numSum + number


    return numSum


print(mySumFunction(10,20,30,40,50))


#taking it a step farther

def secondMySumFunction(aList, number):

    numsum = 0

    for num in aList:
        numsum += num


    numsum = numsum + number

    return numsum





print(secondMySumFunction([1,2,3,4,5],10))


print(secondMySumFunction([10,20,30,40,50], 0))


print(secondMySumFunction([0,1,2,3,4,5,6,7,8,9,10], 10))