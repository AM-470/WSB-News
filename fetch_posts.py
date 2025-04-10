import instaloader

def check_for_news():
    L = instaloader.Instaloader()

    # Login if necessary (optional)
    # L.login("your_username", "your_password")  # Uncomment if login is needed

    try:
        # Fetch the profile and get the most recent post
        profile = instaloader.Profile.from_username(L.context, "wallstreetbets")
        recent_post = next(profile.get_posts())  # This gets the most recent post

        # Check if the post's caption contains more than 10 words (assuming news posts are longer)
        if len(recent_post.caption.split()) > 10:
            return "There is news!"
        else:
            return "No news."

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred."

# Test the function
result = check_for_news()
print(result)
