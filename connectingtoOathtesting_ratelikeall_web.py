from flask import Flask, render_template, request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl"
]

@app.route('/')
def index():
    return render_template('submit.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form data
    query = request.form['query']
    num_videos = int(request.form['num_videos'])
    
    creds = authenticate()
    video_ids = search_youtube(creds, query, num_videos)
    
    if video_ids:
        for video_id in video_ids:
            like_video(creds, video_id)
    
    return f"Search for '{query}' with {num_videos} videos completed, and all found videos have been liked!"


def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret_from20250115_desktop.json", SCOPES
    )
    credentials = flow.run_local_server(port=0)
    print("Authentication successful!")
    return credentials

def search_youtube(credentials, query, num_videos):
    youtube = build("youtube", "v3", credentials=credentials)
    request = youtube.search().list(part="snippet", q=query, maxResults=num_videos)
    response = request.execute()

    video_ids = []
    for idx, item in enumerate(response.get("items", [])):
        video_title = item["snippet"]["title"]
        video_id = item["id"].get("videoId", "N/A")

        # Print the title of each video
        print(f"Video {idx + 1}: {video_title}")

        if video_id != "N/A":
            video_ids.append(video_id)

    return video_ids

def like_video(credentials, video_id):
    youtube = build("youtube", "v3", credentials=credentials)
    youtube.videos().rate(id=video_id, rating="like").execute()

if __name__ == "__main__":
    app.run(debug=True)


