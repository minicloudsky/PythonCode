#coding: utf-8
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
language = 'python'
url = 'https://api.github.com/search/repositories?q=language:'+language+'&sort=stars'
r = requests.get(url)
print("code: ",r.status_code)
response_dict = r.json()
print("Total Repository: ",response_dict['total_count'])
repo_dicts = response_dict['items']

names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_szie = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(style=my_style,x_label_rotation = 45,show_legend = True)
chart.title = 'Most-Starred '+language+' Projects on Github'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file("new"+language+'_repos.svg')
