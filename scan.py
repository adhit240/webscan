#!/usr/bin/env python
# WebPwn3r is a Web Applications Security Scanner
# By Ebrahim Hegazy - twitter.com/zigoo0
# First demo conducted 12Apr-2014 @OWASP Chapter Egypt
# https://www.owasp.org/index.php/Cairo
import re
import urllib
from headers import *
from vulnz import *

print ga.green + ga.bold +'''
 ____                        _
/ ___| _ __   __ _ _ __   __| |
\___ \| '_ \ / _` | '_ \ / _` |
 ___) | |_) | (_| | | | | (_| |
|____/| .__/ \__,_|_| |_|\__,_|
      |_|'''+ga.end
print ga.blue + ga.bold +'''
  ____      _
 / ___|   _| |__   ___ _ __
| |  | | | | '_ \ / _ \ '__|
| |__| |_| | |_) |  __/ |
 \____\__, |_.__/ \___|_|
      |___/'''+ga.end

def urls_or_list():
	url_or_list = raw_input(" [!] Scan URL Atau Daftar URL? [1/2]: ")
	if url_or_list == "1":
	 	 url = raw_input(" [!] Masukan Url: ")
		 #if not url.startswith("http://"):
		     #Thanks to Nu11 for the HTTP checker
                     #print ga.red+'''\n Invalid URL, Please Make Sure That The URL Starts With \"http://\" \n'''+ga.end
                     #exit()
		 if "?" in url:
		 	rce_func(url)
		 	xss_func(url)
		 	error_based_sqli_func(url)
		 else:
			print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" URL Tidak Valid"+ga.end			
			print ga.red +" [Warning] Anda Harus Menulis URL Dengan Legkap .e.g http://URL.com/page.php?id=value \n"+ ga.end
			exit()
	if url_or_list =="2":
		 urls_list = raw_input( ga.green+" [!] Masukan Nama Daftar List .e.g [list.txt]: "+ga.end)
		 open_list = open(urls_list).readlines()
		 for line in open_list:
			 if "?" in line:
			 	links = line.strip()
		  	 	url = links
		  	 	print ga.green+" \n [!] Memulai Scanning %s"%url +ga.end
		  	 	rce_func(url)
			 	xss_func(url)
			 	error_based_sqli_func(url)
			 else:
			 	links = line.strip()
		  	 	url = links
				print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" URL Tidak Valid"+ga.end				
				print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
		 exit()				

urls_or_list()





