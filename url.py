import pyshorteners

def shortenurl(url):
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        return short_url
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    url = input("Enter your URL: ")
    shortened_url = shortenurl(url)
    print(f"Shortened URL: {shortened_url}")

if __name__ == "__main__":
    main()
