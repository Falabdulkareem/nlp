# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$6-Jan-2014 01:46:45 PM$"


def second_largest(numbers):
    first, second = None, None
    for n in numbers:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return second


def third_largest(numbers):
    first, second, third = None, None, None
    for n in numbers:
        if n > first:
            first, second, third = n, first, second
        elif first > n > second:
            second = n
        elif second > n > third:
            third = n
    return third