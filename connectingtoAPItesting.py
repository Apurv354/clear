from googleapiclient.discovery import build

# API key
api_key = 'AIzaSyAodSc3UlB8nf3YpxnGCk2aKk8e95gjF2c'

# Build the YouTube API service
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()

print(response)