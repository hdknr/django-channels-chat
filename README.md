# Channels Sample

## 1. Setup 

[Tutorial Part 1: Basic Setup](https://channels.readthedocs.io/en/latest/tutorial/part_1.html)

~~~bash
$ django-admin startproject app web
$ cd web
$ python manage.py startapp chat
~~~

~~~bash
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:9000

Performing system checks...

System check identified no issues (0 silenced).
October 31, 2018 - 20:55:50
Django version 2.1, using settings 'app.settings'
Starting ASGI/Channels version 2.1.5 development server at http://0.0.0.0:9000/
Quit the server with CONTROL-C.
~~~

## 2 [Tutorial Part 2: Implement a Chat Server](https://channels.readthedocs.io/en/latest/tutorial/part_2.html)

- room view & template
- consumer
- routing
- redis-server
- channel layer

## 3. [Tutorial Part 3: Rewrite Chat Server as Asynchronous](https://channels.readthedocs.io/en/latest/tutorial/part_3.html)

- AsyncWebsocketConsumer
- async def  methods

## 4. [Tutorial Part 4: Automated Testing ](https://channels.readthedocs.io/en/latest/tutorial/part_4.html)

- [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/getting-started)
- [EC2 UbuntuでGoogle Chromeをヘッドレス実行してスクリーンショットを採取する手順 - Qiita](https://qiita.com/shinsaka/items/37436e256c813d277d6d)

~~~bash 
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ sudo apt update
$ sudo apt -f install -y
~~~

~~~bash 
$ wget https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip -d ~/bin/
$ sudo mv ~/bin/chromedriver /usr/local/bin/
~~~

