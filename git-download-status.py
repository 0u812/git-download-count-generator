#!/usr/local/bin/python
import xlsxwriter
import json

from urllib2 import Request, urlopen, URLError, HTTPError

user = raw_input("Enter User name: ")
project = raw_input("Enter Project name: ")
request = Request('https://api.github.com/repos/'+user+'/'+project+'/releases')
workbook = xlsxwriter.Workbook('exports/'+user+'-'+project+'.xlsx')
worksheet = workbook.add_worksheet(project)
worksheet_graph = workbook.add_worksheet('Status Chart')
bold = workbook.add_format({'bold': True})
chart = workbook.add_chart({'type': 'column'})
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
	chart.add_series({
		'categories': '='+project+'!$A$2:$A$'+str(row),
		'values':     '='+project+'!$B$2:$B$'+str(row),
		'line':       {'color': 'blue'},
	})
	chart.set_title ({'name': project+' Download Status'})
	chart.set_x_axis({'name': 'Release version'})
	chart.set_y_axis({'name': 'Download Count'})
	chart.set_size({'x_scale': 2.5, 'y_scale': 3})
	worksheet_graph.insert_chart('A1', chart)
	print "Exported result saved in exports folder"

finally:
	workbook.close()
