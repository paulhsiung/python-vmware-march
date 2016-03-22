import urllib2


def scrape(url):
    print "Scraping %s..." % url
    response = urllib2.urlopen(url)
    return response.read()