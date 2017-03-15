import sys
from urllib import request, urlopen, HTTPError, URLError

srcURL = 'https://www.underground.com/history/airport/KNUQ/2007/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2007&req_city=NA&req_state=NA&req_statename=NA&format=1'

page = None

try:
	page =  urlopen(srcURL)
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
except URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
else:
	print(('Total of {} bytes of content on {}'.format(page.headers['content-length'], page.geturl())))
