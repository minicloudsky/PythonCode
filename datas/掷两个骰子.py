#coding: utf-8
from random import randint
import pygal
class Die():
    def __init__(self,numsides = 6):
        self.num_sides = numsides

    def roll(self):
        return randint(1,self.num_sides)

if __name__ == '__main__':
    die1 = Die()
    die2 = Die()
    results = []
    for roll_num in range(1000):
        result = die1.roll() + die2.roll()
        results.append(result)
    frequencies = []
    max_result = die1.num_sides +die2.num_sides
    for value in range(1,max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    hist = pygal.Bar()
    hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
    hist._x_title = "Result"
    hist._y_title = "Frequency of Result"
    hist.add("D6 + D6",frequencies)
    hist.render_to_file("dice_visual.svg")