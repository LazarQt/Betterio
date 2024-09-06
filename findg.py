import requests

# Define the URL
url = "https://raider.io/api/search-advanced?type=guild&mplus.season-df-1.top20[0][gte]=&recruitment.guild_raids.languages[0][eq]=&recruitment.guild_raids.tags[0][eq]=&recruitment.guild_raids.schedule[0][eq][endTime]=&recruitment.guild_raids.schedule[0][eq][day]=&recruitment.guild_raids.profile.published_at[0][gte]=&region[0][eq]=eu-english&sort[recruitment.guild_raids.profile.published_at]=desc&limit=99&offset=20"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response as JSON
    json_data = response.json()
    # Print or work with the JSON data
    print(json_data)
else:
    print(f"Error: Unable to fetch data (Status code: {response.status_code})")
