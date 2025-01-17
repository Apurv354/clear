from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Specify the scopes your app needs
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def authenticate():
    # Load the OAuth 2.0 credentials
    flow = InstalledAppFlow.from_client_secrets_file(
        # I am using the one applied for the desktop servise
        "client_secret.json", SCOPES
    )

    # Perform authentication
    credentials = flow.run_local_server(port=0)
    print("Authentication successful!")
    return credentials

def search_youtube(credentials, query):
    # Build the YouTube service
    youtube = build("youtube", "v3", credentials=credentials)

    # Search for the query "hello"
    request = youtube.search().list(
        part="snippet",
        q=query,  # Search query
        maxResults=5  # Limit to 5 results
    )
    response = request.execute()

    # Print the search results
    for item in response.get("items", []):
        print("Video Title:", item["snippet"]["title"])
        print("Channel Title:", item["snippet"]["channelTitle"])
        print("Video ID:", item["id"].get("videoId", "N/A"))
        print("-" * 40)

# Authenticate with your Google account
if __name__ == "__main__":
    creds = authenticate()
    search_youtube(creds, "hello")


