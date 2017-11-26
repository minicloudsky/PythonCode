#coding: utf-8
from random import randint
import pygal
class Die():
    def __init__(self,numsides = 6):
        self.num_sides = numsides

    def roll(self):
        return randint(1,self.num_sides)

if __name__ == '__main__':
    die_1 = Die()
    die_2 = Die(10)
    results = []
    for roll_num in range(50000):
        result = die_1.roll() + die_2.roll()
        results.append(result)
    frequencies = []
    max_result = die_1.num_sides +die_2.num_sides
    for value in range(1,max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    hist = pygal.Bar()
    hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    hist._x_title = "Result"
    hist._y_title = "Frequency of Result"
    hist.add("D6 + D10",frequencies)
    hist.render_to_file("dice_visual.svg")