# coding: utf8
#!usr/bin/python2
#------ Mengimpor Modules Yang Diperlukan
import sys,requests,time,json
#------ Warna
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
LC = '\033[1;96m'
#Global
global pesan
global token
#------ Fungsi Untuk Komentar
def komen(posts):  
	hitung = 0 
	for post in posts:
		print "%s[%s!%s]%s Koment Status => %s"%(Y,G,Y,W,post["id"])
		url = "https://graph.facebook.com/%s/comments"%(post["id"])
		params = {'access_token' : token, 'message' : pesan}
		s = requests.post(url, data=params )
		hitung += 1
#------ Fungsi Untuk Mendapatkan Post
def dapat():
	payload = {'access_token' : token}
	r = requests.get('https://graph.facebook.com/me/feed', params=payload)
	hasil = json.loads(r.text) 
	return hasil['data']
#------ Inisialisasi
try:
	pesan = sys.argv[1]
	token = sys.argv[2]
except:
	print "%s%s[%serr%s] %sPenggunaan %s [pesan] [token]\nNote: CTRL+Z Untuk Menghentikan Program%s"%(I,Y,R,Y,W,sys.argv[0],N)
	sys.exit()
#;
dpt=dapat()
komen(dpt)