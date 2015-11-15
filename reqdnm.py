import requests
r = requests.get('https://api.github.com/events')
print
print "status code: ",r.status_code
print
print "Headers:     ",r.headers['Date']
print "Headers:     ",r.headers.get('content-type')
print
print "Encoding:    ",r.encoding
print
#print "Text:        ", r.text
print
#print "Json:        ",r.json()

url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print r.cookies['example_cookie_name']
