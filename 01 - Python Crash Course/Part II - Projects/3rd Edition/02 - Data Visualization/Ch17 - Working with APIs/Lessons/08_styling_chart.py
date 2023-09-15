import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
query_string = "?q=language:python+sort:stars+stars:>10000"
request_url = url + query_string
headers = {"Accept": "application/vnd.github.v3+json"}

response = requests.get(request_url, headers=headers)
response_dict = response.json()

if response.status_code != 200:
    print("Error:", response_dict["message"])
else:
    repo_dicts = response_dict['items']

    # Process the repo information
    names, stars = [], []
    for repo in repo_dicts:
        names.append(repo["name"])
        stars.append(repo["stargazers_count"])

    # Visualize
    title = "Most-Starred Python Projects on GitHub"
    labels = {"x": "Repository", "y": "Stars"}
    fig = px.bar(x=names, y=stars, title=title, labels=labels)
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

    fig.show()
