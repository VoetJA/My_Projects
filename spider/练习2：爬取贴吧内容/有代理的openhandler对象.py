import urllib2

proxyswith = True

httpproxy_handler = urllib2.ProxyHandler({'http':"124.88.67.54:80"})
# httpproxy_handler = urllib2.ProxyHandler({'http':"yangjian:123456789@124.88.67.54:80"})

opener = urllib2.build_opener(httpproxy_handler)

urllib2.install_opener(opener)
request = urllib2.Request('http://www.baidu.com')

# rep = opener.open(request)
rep = urllib2.urlopen(request)

print rep.read()