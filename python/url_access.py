# Python 3
import sys
from urllib import request, error

srcURL = 'https://www.wunderground.com/history/airport/KNUQ/2007/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2007&req_city=NA&req_state=NA&req_statename=NA&format=1'

page = None

try:
	page =  request.urlopen(srcURL)
except error.HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
except error.URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
except Exception:
	print('Failed to open URL "{}"'.format(srcURL))
else:
	print(('Total of {} bytes of content available on {}'.format(page.headers['content-length'], page.geturl())))

if(not page):
	print(page)
