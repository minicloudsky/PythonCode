#coding: utf-8
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation = 45,show_legend = False)
chart.title = 'Python projects'
chart.x_labels = ['httpie','django','flask']

plot_dicts = [
    {'httpie':16101,'label':'Description of httpie.'},
    {'django': 15028,'label':'Description of django.'},
    {'flask': 14798,'label':'Description of flask'}
]
chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')
