import base64
import json
import codecs
from urllib import request

import requests

file_path1 = "E:/Projects/midwares/midwares/TestFile.txt"
file_path2 = "E:/Projects/midwares/midwares/temp.txt"
repo_file_url = 'https://api.github.com/repos/honwaii/midwares/contents/TestFile.txt'

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
headers = {"User-agent": user_agent}


def writefile():
	file1 = codecs.open(file_path1, "w", encoding="utf-8")
	file2 = codecs.open(file_path2, "rb", encoding="utf-8")
	line = file2.readline()
	print(line)
	while line:
		file1.writelines(line)
		line = file2.readline()
	file1.close()
	file2.close()


def get_file_info(file_url):  # 获取文件的sha值
	with request.urlopen(file_url) as f:
		data = f.read()
	sha = json.loads(data)['sha']
	return sha


def convert_contents(content_path):  # 编码转换
	temp = codecs.open(content_path, "r", encoding="utf-8").read()
	content = str(base64.b64encode(temp.encode('utf-8')), "utf-8")  # 将打开的文件转换为base64编码
	return content


def update_file():
	writefile()
	content = convert_contents(file_path1)
	sha = get_file_info(repo_file_url)
	data = {"message": "update this file by python", "content": content, "sha": sha}
	print("data:", data)
	response = requests.put(repo_file_url, headers=headers, data=json.dumps(data), auth=('honwaii', '11113003148a..'))
	print(response.headers)
	print(response.content)


# get_file_info(path)
# openfile()

# print(convert_contents(file_path1))
update_file()
