# Flask-Babel(多國語言轉換) example
How Use Flask-Babel on Windows - Python Flask

* [Demo](https://youtu.be/3mBodR0uWfo)  

使用Python [Flask](http://flask.pocoo.org/) 搭配 [Flask-Babel](https://pythonhosted.org/Flask-Babel/) 快速實現多國語系轉換，希望這個簡單的範例可以幫助想要學習的朋友。

## 特色
* 透過 [Flask-Babel](https://pythonhosted.org/Flask-Babel/) 實現多國語系轉換。
* 更多的文件可以參考官方文件 [Flask-Babel](https://pythonhosted.org/Flask-Babel/)

## 安裝套件 Babel 以及 Flask-Babel
請先確定電腦有安裝 [Python](https://www.python.org/)

### Babel
``` 
pip install babel
```
安裝完後，使用 cmd(命令提示字元) 輸入
``` 
pybabel --version
```
如果看到版本號，如下圖，代表安裝且設定成功<br>
![alt tag](http://i.imgur.com/wKVo5mD.png)

如果你出現 <b> 'pybabel' 不是內部或外部命令、可執行的程式或批次檔。 </b>

代表你需要設定環境變數或是安裝失敗。

### Flask-Babel

``` 
pip install flask-babel
```

## 開始實做

先建立好 flask 之後

建立 <b> settings.cfg </b> ，裡面請輸入，如下圖
``` 
BABEL_DEFAULT_LOCALE="en"
BABEL_DEFAULT_TIMEZONE="UTC"
```
BABEL_DEFAULT_LOCALE 代表你默認要顯示的語言

![alt tag](http://i.imgur.com/MkYNAqA.png)

程式碼( app.py )裡設定
``` 
app.config.from_pyfile('settings.cfg')
```

建立 <b> babel.cfg </b> ，裡面請輸入
``` 
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
![alt tag](http://i.imgur.com/TbEC8CW.png)

接下來請到 目錄下 使用 cmd(命令提示字元) 輸入下列指令，注意，最後那個 <b>.</b> 是需要的 !!
``` 
pybabel extract -F babel.cfg -o messages.pot .
```
![alt tag](http://i.imgur.com/sv6Gd99.png)

到專案底下會發現多出一個檔案<b> messages.pot </b> ,<b> pot 檔只是翻譯模板，檔案內不包含任何翻譯 </b>。
![alt tag](http://i.imgur.com/NnW2Ues.png)

先建立中文(zh)的翻譯，到 目錄下 使用 cmd(命令提示字元) 輸入下列指令
``` 
pybabel init -i messages.pot -d translations -l zh
```
![alt tag](http://i.imgur.com/MuabvLi.png)

到專案下會發現多出一個資料夾，如下圖
![alt tag](http://i.imgur.com/BCqNoz2.png)

<b> messages.po </b> 就是你必須要翻譯的地方!!

以下是我在這裡輸入的翻譯
<br>
![alt tag](http://i.imgur.com/u3elJwk.png)

最後只需要到 目錄下 使用 cmd(命令提示字元) 輸入以下指令進行編譯即完成。
``` 
pybabel compile -d translations
```
![alt tag](http://i.imgur.com/PF8X9fc.png)

編譯完後，資料夾會多出 <b> messages.mo </b>
<br>
![alt tag](http://i.imgur.com/XpIasBS.png)

如要新增其他語言，以此類推。

如果今天<b> messages.pot </b> 有更新了，只需要執行以下指令
``` 
pybabel update -i messages.pot -d translations
```
如果你又有新增需要翻譯的文字，這時候你該怎麼辦呢 ?

首先，先執行下方的指令，讓他重新掃一次整個目錄
``` 
pybabel extract -F babel.cfg -o messages.pot .
```

執行後你會發現 <b> messages.pot</b> 裡面多了你剛剛的更新 (也就是新增加的文字)

由於 <b> messages.pot</b> 更新了，所以必須要再執行以下指令

``` 
pybabel update -i messages.pot -d translations
```

你會發現 en 資料夾(這裡舉例英文) 裡面的  <b>messages.po</b> 多了你剛剛的更新內容

這時候，再翻譯，翻譯完畢後，再用以下的指令編譯就完成了

``` 
pybabel compile -d translations
```

以上可能會有點小複雜，但多做幾次你就會了解了 :smile:

接著使用下列指令即可運行

``` 
python app.py
```

P.S

通常翻譯我們用的語法是
``` 
gettext("string")
```
但要注意，這個 "string" 裡面的文字，如果有要用的 "%" 這個符號，必須用 <b>全形</b> !! 如果你用 <b>半形</b> 會出問題。

## 執行畫面

瀏覽器語系 - 英文<br>
![alt tag](http://i.imgur.com/Po0mZkl.png)

瀏覽器語系 - 中文<br>
![alt tag](http://i.imgur.com/786Wdmn.png)


## 執行環境
* Python 3.5.2

## License
MIT license
