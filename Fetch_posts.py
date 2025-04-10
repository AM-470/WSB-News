import instaloader

def get_news_posts(username='wallstreetbets', limit=10, min_words=10):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    posts = profile.get_posts()

    news_posts = []
    for post in posts:
        if post.caption:
            if len(post.caption.split()) >= min_words:
                news_posts.append({
                    'url': post.url,
                    'caption': post.caption,
                    'thumbnail_url': post.url
                })
        if len(news_posts) >= limit:
            break
    return news_posts
