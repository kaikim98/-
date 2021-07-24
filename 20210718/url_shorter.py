import pyshorteners
def shorter(url):
    
    short_url= pyshorteners.Shortener().tinyurl.short(url)
    return short_url