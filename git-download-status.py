#!/usr/local/bin/python
import xlsxwriter
import json

from urllib2 import Request, urlopen, URLError, HTTPError

user = raw_input("Enter User name: ")
project = raw_input("Enter project name: ")
request = Request('https://api.github.com/repos/'+user+'/'+project+'/releases')
workbook = xlsxwriter.Workbook('exports/'+user+'-'+project+'.xlsx')
worksheet = workbook.add_worksheet(project)
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Releases', bold)
worksheet.write('B1', 'Download Count', bold)
row = 1
col = 0

try:
	response = urlopen(request)
except HTTPError as e:
	if e.code == 404:
		print "No repository available"
		worksheet.write(row, col, "No repository available")
	else:
		raise
else:
	# 200
	download_counts = json.loads(response.read())
	for item in download_counts:
		if 'tag_name' in item:
			worksheet.write(row, col, item['tag_name'])
			if item['assets']:
				worksheet.write(row, col + 1, item['assets'][0]['download_count'])
			row += 1
			continue
	print "Exported result saved in exports folder"
finally:
	workbook.close()
