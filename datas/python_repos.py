#coding: utf-8
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r  = requests.get(url)
print("status_code: ",r.status_code)

response_dict = r.json()
repo_dicts = response_dict['items']
print(response_dict.keys())
print("Repositories returned:",len(repo_dicts))
print("total Repository:" ,response_dict['total_count'])
print("Selected information about each repository:")
for repo_dict in repo_dicts:
    print("Name: ",repo_dict['name'])
    print("Owner: ",repo_dict['owner']['login'])
    print("Stars: ",repo_dict['stargazers_count'])
    print("Repository: ",repo_dict['html_url'])
    print('Description: ',repo_dict['description'])
