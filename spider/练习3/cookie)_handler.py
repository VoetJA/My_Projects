import urllib2
import urllib
import cookielib

cookie = cookielib.CookieJar()

cookie_handler = urllib2.HTTPCookieProcessor(cookie)

opener_cookie = urllib2.bulid_opener(cookie_handler)

opener_cookie.addheaders = [("User-Agente","Mozilla...")]

url = 'http://...'

data = {'name':name,'password':password}

data = urllib.urlencode(data)

request = urllib2.Request(url,data)

rep = opener_cookie.open(request)

print rep.read()