#!/usr/local/bin/python
# Tool to convert CSV files (with configurable delimiter and text wrap
# character) to Excel spreadsheets.
import xlsxwriter
import json

from urllib2 import Request, urlopen, URLError

project = raw_input("Enter project name: ")
request = Request('https://api.github.com/repos/wso2/'+project+'/releases')
workbook = xlsxwriter.Workbook('exports/'+project+'.xlsx')
worksheet = workbook.add_worksheet(project)
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Releases', bold)
worksheet.write('B1', 'Download Count', bold)
row = 1
col = 0

try:
	response = urlopen(request)
	download_counts = json.loads(response.read())
finally:
	for item in download_counts:
		if 'tag_name' in item:
			worksheet.write(row, col, item['tag_name'])
			if item['assets']:
				worksheet.write(row, col + 1, item['assets'][0]['download_count'])
			row += 1
			continue

workbook.close()
