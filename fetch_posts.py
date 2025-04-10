import instaloader
import time

def get_news_posts():
    L = instaloader.Instaloader()

    try:
        # Load profile and fetch recent posts
        profile = instaloader.Profile.from_username(L.context, "wallstreetbets")
        posts = []
        
        for post in profile.get_posts():
            if len(post.caption.split()) > 10:  # Filter posts with more than 10 words
                posts.append({
                    'image': post.url,
                    'caption': post.caption
                })
            
            # Limit the number of posts to display (e.g., 5 recent posts)
            if len(posts) >= 4:
                break
            
            # Delay to avoid hitting Instagram rate limits
            time.sleep(10)  # Sleep for 5 seconds between requests to avoid rate-limiting

        return posts

    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection Error: {e}")
        return []  # Return an empty list if there is a connection issue

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
