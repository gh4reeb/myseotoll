from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace with your YouTube API Key
API_KEY = 'ADD_YOUR_YOUTUBE_API'

def fetch_video_data(query, max_results=10):
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results
        )
        response = request.execute()

        video_data = []
        for item in response['items']:
            video_data.append({
                'video_id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'tags': item.get('tags', []),
            })

        return video_data, None  # No error

    except HttpError as e:
        error_message = f"API Error: {e.reason}. Please try again later."
        return None, error_message  # Return the error message