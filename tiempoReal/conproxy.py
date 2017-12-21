import urllib2
import urllib
import random

CAproxies = [{"http":"199.201.122.175:3128", "https":"199.201.122.175:3128"},{"http":"192.99.3.129:3128", "https":"192.99.3.129:3128"},{"http":"192.99.246.101:8118", "https":"192.99.246.101:8118"},{"http":"205.205.129.130:443", "https":"205.205.129.130:443"} ]

# http://www.proxy-listen.de/Proxy/Proxyliste.html
# https://stackoverflow.com/questions/30292361/request-from-different-country-ip

proxies = urllib2.ProxyHandler(random.choice(CAproxies))

urls =[{"www.facebook.com","www.twitter.com","www.wikipedia.com"}]
url = urls[1];
# hacer un for con url para comprobar uno a uno

request = urllib2.Request(url)
request.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0")
request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")

opener = urllib2.build_opener(proxies)
urllib2.install_opener(opener)
r = urllib2.urlopen(request, timeout=15)
html = r.read()
