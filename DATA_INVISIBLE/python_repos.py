import requests  #导入了requests模块

#   调用api 并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
respon_dict = req.json()
print("status_code is :", req.status_code)
print("Total repositories: ", respon_dict["total_count"])

repo_dicts = respon_dict["items"]
print("Repositories returned: ", len(repo_dicts))

repo_dict = repo_dicts[0]
print("total of keys is :", len(repo_dict))
for key in sorted(repo_dict.keys()):  #sorted按照字母顺序排序
    print(key)

s = 1
for re_dict in repo_dicts:
    print("\nSelect information about the {}th repository".format(s))
    print("name :", re_dict["name"])
    print("owner :", re_dict['owner']['login'])
    print("description :", re_dict["description"])
    print("created_at :", re_dict["created_at"])
    print("updated_at :", re_dict["updated_at"])
    print("repository :", re_dict["html_url"])
    print("Stars :", re_dict["stargazers_count"])
    s = s+1
"""
status_code is : 200
Total repositories:  3409234
Repositories returned:  30
total of keys is : 73

Select information about the 1th repository
name : awesome-python
owner : vinta
description : A curated list of awesome Python frameworks, libraries, software and resources
created_at : 2014-06-27T21:00:06Z
updated_at : 2019-01-20T17:13:01Z
repository : https://github.com/vinta/awesome-python
Stars : 60345

Select information about the 2th repository
name : system-design-primer
owner : donnemartin
description : Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.
created_at : 2017-02-26T16:15:28Z
updated_at : 2019-01-20T17:10:41Z
repository : https://github.com/donnemartin/system-design-primer
Stars : 55139
Select information about the 3th repository
name : models
owner : tensorflow
description : Models and examples built with TensorFlow
created_at : 2016-02-05T01:15:20Z
updated_at : 2019-01-20T17:28:48Z
repository : https://github.com/tensorflow/models
Stars : 47430
Select information about the 4th repository
name : public-apis
owner : toddmotto
description : A collective list of free APIs for use in software and web development.
created_at : 2016-03-20T23:49:42Z
updated_at : 2019-01-20T17:19:20Z
repository : https://github.com/toddmotto/public-apis
Stars : 46551
Select information about the 5th repository
name : youtube-dl
owner : rg3
description : Command-line program to download videos from YouTube.com and other video sites
created_at : 2010-10-31T14:35:07Z
updated_at : 2019-01-20T17:28:16Z
repository : https://github.com/rg3/youtube-dl
Stars : 46280
Select information about the 6th repository
name : flask
owner : pallets
description : The Python micro framework for building web applications.
created_at : 2010-04-06T11:11:59Z
updated_at : 2019-01-20T17:24:38Z
repository : https://github.com/pallets/flask
Stars : 41376
Select information about the 7th repository
name : thefuck
owner : nvbn
description : Magnificent app which corrects your previous console command.
created_at : 2015-04-08T15:08:04Z
updated_at : 2019-01-20T14:39:29Z
repository : https://github.com/nvbn/thefuck
Stars : 40051
Select information about the 8th repository
name : httpie
owner : jakubroztocil
description : As easy as httpie /aitch-tee-tee-pie/ 🥧 Modern command line HTTP client – user-friendly curl alternative with intuitive UI, JSON support, syntax highlighting, wget-like downloads, extensions, etc.  https://twitter.com/clihttp
created_at : 2012-02-25T12:39:13Z
updated_at : 2019-01-20T17:10:33Z
repository : https://github.com/jakubroztocil/httpie
Stars : 39389
Select information about the 9th repository
name : django
owner : django
description : The Web framework for perfectionists with deadlines.
created_at : 2012-04-28T02:47:18Z
updated_at : 2019-01-20T15:47:40Z
repository : https://github.com/django/django
Stars : 38976
Select information about the 10th repository
name : awesome-machine-learning
owner : josephmisiti
description : A curated list of awesome Machine Learning frameworks, libraries and software.
created_at : 2014-07-15T19:11:19Z
updated_at : 2019-01-20T16:59:01Z
repository : https://github.com/josephmisiti/awesome-machine-learning
Stars : 37690
Select information about the 11th repository
name : keras
owner : keras-team
description : Deep Learning for humans
created_at : 2015-03-28T00:35:42Z
updated_at : 2019-01-20T17:18:27Z
repository : https://github.com/keras-team/keras
Stars : 37543
Select information about the 12th repository
name : requests
owner : requests
description : Python HTTP Requests for Humans™ ✨🍰✨
created_at : 2011-02-13T18:38:17Z
updated_at : 2019-01-20T16:39:18Z
repository : https://github.com/requests/requests
Stars : 36777
Select information about the 13th repository
name : ansible
owner : ansible
description : Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy. Avoid writing scripts or custom code to deploy and update your applications — automate in a language that approaches plain English, using SSH, with no agents to install on remote systems. https://docs.ansible.com/ansible/
created_at : 2012-03-06T14:58:02Z
updated_at : 2019-01-20T17:04:08Z
repository : https://github.com/ansible/ansible
Stars : 34917
Select information about the 14th repository
name : scikit-learn
owner : scikit-learn
description : scikit-learn: machine learning in Python
created_at : 2010-08-17T09:43:38Z
updated_at : 2019-01-20T15:20:51Z
repository : https://github.com/scikit-learn/scikit-learn
Stars : 32912
Select information about the 15th repository
name : big-list-of-naughty-strings
owner : minimaxir
description : The Big List of Naughty Strings is a list of strings which have a high probability of causing issues when used as user-input data.
created_at : 2015-08-08T20:57:20Z
updated_at : 2019-01-20T17:28:21Z
repository : https://github.com/minimaxir/big-list-of-naughty-strings
Stars : 31184
Select information about the 16th repository
name : scrapy
owner : scrapy
description : Scrapy, a fast high-level web crawling & scraping framework for Python.
created_at : 2010-02-22T02:01:14Z
updated_at : 2019-01-20T17:38:45Z
repository : https://github.com/scrapy/scrapy
Stars : 31067
Select information about the 17th repository
name : shadowsocks
owner : shadowsocks
description : None
created_at : 2012-04-20T13:10:49Z
updated_at : 2019-01-20T16:32:13Z
repository : https://github.com/shadowsocks/shadowsocks
Stars : 28306
Select information about the 18th repository
name : XX-Net
owner : XX-net
description : a web proxy tool
created_at : 2015-01-15T09:35:51Z
updated_at : 2019-01-20T14:29:56Z
repository : https://github.com/XX-net/XX-Net
Stars : 26250
Select information about the 19th repository
name : certbot
owner : certbot
description : Certbot is EFF's tool to obtain certs from Let's Encrypt and (optionally) auto-enable HTTPS on your server.  It can also act as a client for any other CA that uses the ACME protocol.
created_at : 2014-11-12T02:52:20Z
updated_at : 2019-01-20T15:58:54Z
repository : https://github.com/certbot/certbot
Stars : 24097
Select information about the 20th repository
name : cpython
owner : python
description : The Python programming language
created_at : 2017-02-10T19:23:51Z
updated_at : 2019-01-20T17:31:50Z
repository : https://github.com/python/cpython
Stars : 21960
Select information about the 21th repository
name : you-get
owner : soimort
description : :arrow_double_down: Dumb downloader that scrapes the web
created_at : 2012-08-20T15:53:36Z
updated_at : 2019-01-20T13:27:57Z
repository : https://github.com/soimort/you-get
Stars : 21768
Select information about the 22th repository
name : Deep-Learning-Papers-Reading-Roadmap
owner : floodsung
description : Deep Learning papers reading roadmap for anyone who are eager to learn this amazing tech!
created_at : 2016-10-14T11:49:48Z
updated_at : 2019-01-20T17:41:51Z
repository : https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap
Stars : 21421
Select information about the 23th repository
name : CppCoreGuidelines
owner : isocpp
description : The C++ Core Guidelines are a set of tried-and-true guidelines, rules, and best practices about coding in C++
created_at : 2015-08-19T20:22:52Z
updated_at : 2019-01-20T17:11:50Z
repository : https://github.com/isocpp/CppCoreGuidelines
Stars : 21067
Select information about the 24th repository
name : home-assistant
owner : home-assistant
description : :house_with_garden: Open source home automation that puts local control and privacy first
created_at : 2013-09-17T07:29:48Z
updated_at : 2019-01-20T17:27:07Z
repository : https://github.com/home-assistant/home-assistant
Stars : 20736
Select information about the 25th repository
name : Python
owner : TheAlgorithms
description : All Algorithms implemented in Python
created_at : 2016-07-16T09:44:01Z
updated_at : 2019-01-20T16:47:41Z
repository : https://github.com/TheAlgorithms/Python
Stars : 20732
Select information about the 26th repository
name : face_recognition
owner : ageitgey
description : The world's simplest facial recognition api for Python and the command line
created_at : 2017-03-03T21:52:39Z
updated_at : 2019-01-20T17:32:30Z
repository : https://github.com/ageitgey/face_recognition
Stars : 20251
Select information about the 27th repository
name : tldr
owner : tldr-pages
description : :books: Simplified and community-driven man pages
created_at : 2013-12-08T07:34:43Z
updated_at : 2019-01-20T17:26:11Z
repository : https://github.com/tldr-pages/tldr
Stars : 20230
Select information about the 28th repository
name : sentry
owner : getsentry
description : Sentry is cross-platform application monitoring, with a focus on error reporting.
created_at : 2010-08-30T22:06:41Z
updated_at : 2019-01-20T06:51:23Z
repository : https://github.com/getsentry/sentry
Stars : 19487
Select information about the 29th repository
name : linux-insides
owner : 0xAX
description : A little bit about a linux kernel
created_at : 2015-01-03T18:44:57Z
updated_at : 2019-01-20T17:05:20Z
repository : https://github.com/0xAX/linux-insides
Stars : 18854
Select information about the 30th repository
name : Detectron
owner : facebookresearch
description : FAIR's research platform for object detection research, implementing popular algorithms like Mask R-CNN and RetinaNet.
created_at : 2017-10-05T17:32:00Z
updated_at : 2019-01-20T16:16:21Z
repository : https://github.com/facebookresearch/Detectron
Stars : 18744
PyDev console: starting.
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
"""
