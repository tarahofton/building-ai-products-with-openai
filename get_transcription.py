def get_transcribe_podcast(rss_url, local_path):
    print ("Starting Podcast Transcription Function")
    print ("Feed URL: ", rss_url)
    print ("Local Path:", local_path)

    # Read from the RSS Feed URL
    import feedparser
    intelligence_feed = feedparser.parse(rss_url)
    for item in intelligence_feed.entries[0].links:
        if (item['type'] == 'audio/mpeg'):
            episode_url = item.href
    episode_name = "podcast_episode.mp3"
    print ("RSS URL read and episode URL: ", episode_url)

    # Download the podcast episode by parsing the RSS feed
    from pathlib import Path
    p = Path(local_path)
    p.mkdir(exist_ok=True)

    print ("Downloading the podcast episode")
    import requests
    with requests.get(episode_url, stream=True) as r:
        r.raise_for_status()
        episode_path = p.joinpath(episode_name)
        with open(episode_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print ("Podcast Episode downloaded")

    # Load the Whisper model
    import os
    import whisper
    print ("Download and Load the Whisper model")
    model = whisper.load_model("medium")
    print (model.device)

    # Perform the transcription
    print ("Starting podcast transcription")
    result = model.transcribe(local_path + episode_name)

    # Return the transcribed text
    print ("Podcast transcription completed, returning results...")
    return result