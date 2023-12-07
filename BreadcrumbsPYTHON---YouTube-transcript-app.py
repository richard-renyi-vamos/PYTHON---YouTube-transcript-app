from youtube_transcript_api import YouTubeTranscriptApi

def get_captions(video_id):
    try:
        captions = YouTubeTranscriptApi.get_transcript(video_id)
        return captions
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_captions_to_file(video_id, file_name):
    captions = get_captions(video_id)
    if captions:
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                for caption in captions:
                    text = caption['text']
                    file.write(text + '\n')
            print(f"Captions saved to {file_name}")
        except Exception as e:
            print(f"Failed to save captions: {e}")

# Replace 'VIDEO_ID' with the actual ID of the YouTube video
video_id = 'VIDEO_ID'

# Replace 'captions.txt' with the desired file name
save_captions_to_file(video_id, 'captions.txt')
