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
    frequencies = []
    for value in range(1,die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    hist = pygal.Bar()
    hist.x_labels = ['1','2','3','4','5','6']
    hist._x_title = "Result"
    hist._y_title = "Frequency of Result"
    hist.add("D6",frequencies)
    hist.render_to_file("die_visual.svg")