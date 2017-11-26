#coding: utf-8
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
language = 'c#'
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
chart = pygal.Bar(style=my_style,x_label_rotation = 45,show_legend = True)
chart.title = 'Most-Starred '+language+' Projects on Github'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file(language+'_repos.svg')
