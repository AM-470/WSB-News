import instaloader
import time
import random  # Import random module

def get_news_posts():
    L = instaloader.Instaloader()

    try:
        # Load profile and fetch recent posts
        profile = instaloader.Profile.from_username(L.context, "wallstreetbets")
        posts = []
        
        for post in profile.get_posts():
            if len(post.caption.split()) > 3:  # Filter posts with more than 10 words
                posts.append({
                    'image': post.url,
                    'caption': post.caption
                })
            
            # Limit the number of posts to 4
            if len(posts) >= 4:  # Fetch top 4 posts
                break
            
            # Random delay between 13 and 55 seconds
            delay = random.randint(13, 55)  # Generate a random delay
            print(f"Waiting for {delay} seconds...")  # Optional: Print the delay time
            time.sleep(delay)  # Sleep for the random delay

        return posts

    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection Error: {e}")
        return []  # Return an empty list if there is a connection issue

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
