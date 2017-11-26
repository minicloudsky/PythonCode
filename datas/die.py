#coding: utf-8
from random import randint
import pygal
class Die():
    def __init__(self,numsides = 6):
        self.num_sides = numsides

    def roll(self):
        return randint(1,self.num_sides)

if __name__ == '__main__':
    die = Die()
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)
    # print(results)
    frequencies = []
    for value in range(1,die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    print(frequencies)