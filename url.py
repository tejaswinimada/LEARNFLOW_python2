import string
import random

class URLShortener:
    def __init__(self):
        self.url_mappings = {}

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))  # Adjust the length as needed
        return short_url

    def shorten_url(self, long_url):
        short_url = self.generate_short_url()
        self.url_mappings[short_url] = long_url
        return short_url

    def redirect(self, short_url):
        return self.url_mappings.get(short_url, None)

# Example usage:
url_shortener = URLShortener()

while True:
    long_url = input("Enter the long URL to shorten (or 'exit' to quit): ")
    
    if long_url.lower() == 'exit':
        break

    short_url = url_shortener.shorten_url(long_url)
    print(f"Short URL: http://example.com/{short_url}")

# Simulate redirection
while True:
    short_url = input("Enter the short URL for redirection (or 'exit' to quit): ")
    
    if short_url.lower() == 'exit':
        break

    long_url = url_shortener.redirect(short_url)
    
    if long_url:
        print(f"Redirecting to: {long_url}")
    else:
        print("Short URL not found.")
