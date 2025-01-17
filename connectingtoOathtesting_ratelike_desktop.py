from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Specify the scopes your app needs (read and write permissions)
SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl"
]

def authenticate():
    # Load the OAuth 2.0 credentials
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret_from20250115_desktop.json", SCOPES
    )

    # Perform authentication
    credentials = flow.run_local_server(port=0)
    print("Authentication successful!")
    return credentials

def search_youtube(credentials, query):
    # Build the YouTube service
    youtube = build("youtube", "v3", credentials=credentials)

    try:
        # Search for the query
        request = youtube.search().list(
            part="snippet",
            q=query,  # Search query
            maxResults=5  # Limit to 5 results
        )
        response = request.execute()

        # Print the search results and return the first video ID
        first_video_id = None
        for idx, item in enumerate(response.get("items", [])):
            print(f"Result {idx + 1}:")
            print("Video Title:", item["snippet"]["title"])
            print("Channel Title:", item["snippet"]["channelTitle"])
            video_id = item["id"].get("videoId", "N/A")
            print("Video ID:", video_id)
            print("-" * 40)
            if idx == 0:  # Save the first video ID
                first_video_id = video_id
        
        return first_video_id

    except HttpError as e:
        print(f"An error occurred: {e}")
        return None

def like_video(credentials, video_id):
    # Build the YouTube service
    youtube = build("youtube", "v3", credentials=credentials)

    try:
        # Like the video using the `videos.rate` method
        youtube.videos().rate(
            id=video_id,
            rating="like"
        ).execute()
        print(f"Liked video with ID: {video_id}")
    except HttpError as e:
        print(f"An error occurred while liking the video: {e}")

# Authenticate with your Google account
if __name__ == "__main__":
    creds = authenticate()
    query = "hello"  # Replace with your desired search query
    first_video_id = search_youtube(creds, query)
    if first_video_id:
        like_video(creds, first_video_id)
