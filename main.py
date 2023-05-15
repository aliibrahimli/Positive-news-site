import requests

from send_email import send_email

api = "4de8df5017304a59b879d6986258c027"
url = "https://newsapi.org/v2/everything?q=apple&from=2023-05-14&to=2023-05-14&sortBy=popularity&apiKey=4de8df5017304a59b879d6986258c027"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body +article["title"] + "\n" + article["description"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)