import urllib.request
import json
import pdfkit
import os
import datetime


def tagpdf(pathac="",num=1,urll=''):
	request = urllib.request.Request("http://www.codeforces.com/api/problemset.problems?tags="+urll)
	response = urllib.request.urlopen(request)
	encoding = response.info().get_content_charset('utf8')
	data = json.loads(response.read().decode(encoding))
	if data['status'] != 'OK':
		print(' ERROR\n')
		return

	ss = str(datetime.datetime.now().now())
	path = pathac
	if not pathac:
		os.chdir(os.path.dirname(__file__))
		path = os.getcwd()
		
	path = path + '/' +  ss
	
	os.makedirs(path,exist_ok=True)
	
	path = path + '/'
	
	'''
	print(path)
	'''
	for i in range(0,num):
		if not data['result']['problems'][i]:
			break;
		a = "http://www.codeforces.com/problemset/problem/"
		a = a + str(data['result']['problems'][i]['contestId'])
		a = a + "/"
		a = a + str(data['result']['problems'][i]['index'])
		pdfkit.from_url(a,path + str(data['result']['problems'][i]['contestId'])+ str(data['result']['problems'][i]['index']))



		
def gettags():
	
	tags = ["implementation","binary search","math","data structures","dfs and similar","graphs","combinatorics","constructive algorithms","dp","greedy","strings","hashing","two pointers",
	"bitmasks","sortings","string suffix structures","geometry","dsu","divide and conquer","trees","games","probabilities"]
	print("\n")
	print("	*********************** \n ")
	print("	press q to quit\n")

	print("	tags list\n")
	print("    tag id  : tag\n")
	print("	1  implementation\n")
	print("	2  binary search\n")
	print("	3  math\n")
	print("	4  data structures\n")
	print("	5  dfs and similar\n")
	print("	6  graphs\n")
	print("	7  combinatorics\n")
	print("	8  constructive algorithms\n")
	print("	9  dp\n")
	print("	10 greedy\n")
	print("	11 strings\n")
	print("	12 hashing\n")
	print("	13 two pointers\n")
	print("	14 bitmasks\n")
	print("	15 sortings\n")
	print("	16 string suffix structures\n")
	print("	17 geometry\n")
	print("	18 dsu\n")
	print("	19 divide and conquer\n")
	print("	20 trees\n")
	print("	21 games\n")
	print("	22 probabilities\n")
	print("\n")
	print("	press f to select tag id: \n")
	print("	press q to quit\n")
	s = input()
	while s!='q' and s!='f':
		print(" press either q or f (not in caps)")
		s= input()
	
	if s=='q':
		return
	
	rTag = []

	while s!='s':
		print('	enter the tagid : ')
		print('')
		s = input()
		if s=='s':
			break
		while (int(s) > 22 or int(s) <=0) or (not s.isdigit()) :
			print(" invalid tag id , give a valid tag, press s to stop")
			s=input()
			if s=='s':
				break
		if s=='s':
			break
		rTag.append(int(s))
		print('	press s to stop , f to continue')
		s = input()
		while s!='s' and s!='f':
			print('	press s to stop , f to continue')
			s=input()
		if s=='s':
			break

	urll = ""
	for i in range(0,len(rTag)):
		urll = urll + tags[rTag[i]-1]
		if i != (len(rTag)-1):
			urll = urll + ';'
	path=""
	print('	Enter the directory path where the problems are to be downloaded or leave blank, by default it is the working directory of script\n')
	path = input()
	print('	Enter the number of problems to be downloaded or leave blank, by default it is 1')
	num = int(input())

	tagpdf(path,num,urll)

	

def contestpdf(pathac="",contestId='1'):
	if not contestId.isdigit():
		print('	TYPE ERROR\n')
		return 
	request = urllib.request.Request('http://www.codeforces.com/api/problemset.problems?tags=')
	response = urllib.request.urlopen(request)
	encoding = response.info().get_content_charset('utf8')
	data = json.loads(response.read().decode(encoding))
	if data['status'] != 'OK':
		print(' ERROR\n')
		return

	ss = str(datetime.datetime.now().now())
	path = pathac
	if not pathac:
		os.chdir(os.path.dirname(__file__))
		path = os.getcwd()
		
	path = path + '/' +  ss
	
	os.makedirs(path,exist_ok=True)
	
	path = path + '/'
	
	

	

	for i in range(0,len(data['result']['problems'])):
		
		if str(data['result']['problems'][i]['contestId']) == contestId:
			a = "http://www.codeforces.com/problemset/problem/"
			a = a + str(data['result']['problems'][i]['contestId'])
			a = a + "/"
			a = a + str(data['result']['problems'][i]['index'])
			pdfkit.from_url(a,path + str(data['result']['problems'][i]['contestId'])+ str(data['result']['problems'][i]['index']))
		
		

