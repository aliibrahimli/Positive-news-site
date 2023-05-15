import requests

from send_email import send_email

topic = "windows"

api = "4de8df5017304a59b879d6986258c027"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-04-15&" \
      "sortBy=publishedAt&" \
      "apiKey=4de8df5017304a59b879d6986258c027&" \
      "language=en"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description

body = ""
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n"\
               + body +article["title"] + "\n" \
               + article["description"] + "\n"\
               + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)