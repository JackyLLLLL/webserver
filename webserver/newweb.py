from flask import Flask, render_template,request,url_for
import time 
from time import sleep
from flask.helpers import url_for

app = Flask(__name__, static_url_path="/static", static_folder='/home/pi/Jacky/webserver/static' )

file = "/home/pi/Jacky/DHT22_LCD/DHT22_status_web.txt"
#demohtml = "/home/pi/Jacky/webserver/static/demo.html"
demohtml = "/home/pi/Jacky/webserver/templates/demo.html"


@app.route("/")
def static_file():
    
    with open(demohtml,'w') as f :
        f.write("<!DOCTYPE HTML>\n")
        f.write("<html>\n") 
        f.write("<head>\n") 
        f.write("<title>Jacky.L 專題 DEMO</title>\n")
        f.write("<meta charset=\"utf-8\" />\n")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, user-scalable=no\" />\n")
        
        f.write("<link rel='stylesheet' href='static/css/main.css' />\n")
        f.write("<noscript><link rel='stylesheet' href='static/css/noscript.css' /></noscript>\n")

        #f.write("{% load static %}")
        #f.write("<link href=\"{% static 'css/main.css' %}\" rel=\"stylesheet\"/>\n")
        #f.write("<noscript><link href=\"{% static 'css/noscript.css' %}\" rel=\"stylesheet\"/></noscript>\n")
        #f.write("<link rel=\"stylesheet\" href=\"{url_for('static', filename='css/main.css') }\n")
        #f.write("<noscript><link rel=\"stylesheet\" href=\"{ url_for('static', filename='css/noscrpit.css')}\n")
        
       
        # <link rel='stylesheet' href='static/css/main.css' />
        # <noscript><link rel='stylesheet' href='static/css/noscript.css' /></noscript>

        # f.write("<link rel=\"stylesheet\" href=\"static/css/main.css\" />\n")
        # f.write("<noscript><link rel=\"stylesheet\" href=\"static/css/noscript.css\" /></noscript>\n")
        
        f.write("</head>\n")
        f.write("<body class=\"is-preload\">\n")
        f.write("<div id=\"wrapper\">\n")
        f.write("<header id=\"header\">\n")
        f.write("<div class=\"logo\">\n")
        f.write("<span class=\"icon fa-gem\"></span>\n")
        f.write("</div>\n")
        f.write("<div class=\"content\">\n")
        f.write("<div class=\"inner\">\n")
        f.write("<h1>Jacky 專題展示</h1>\n")
        f.write("<p>物聯網(IoT)上的基礎應用實例</p>\n")
        f.write("</div></div>\n")
        f.write("<nav>\n")
        f.write("<ul>\n")
        f.write("<li><a href=\"#intro\">intro</a></li>\n")
        f.write("<li><a href=\"#Application\">Application</a></li>\n")
        f.write("<li><a href=\"#DHT22\">temperature</a></li>\n")
        f.write("<li><a href=\"#about\">About</a></li>\n")
        f.write("<li><a href=\"#contact\">Contact</a></li>\n")
        f.write("</ul>\n")
        f.write("</nav>\n")
        f.write("</header>\n")
        f.write("<div id=\"main\">\n")
        f.write("<article id=\"intro\">\n")
        f.write("<h2 class=\"major\">Intro</h2>\n")
        f.write("<span class=\"image main\"><img src=\"static/images/IoT.jpg\" alt=\"\" /></span>\n")
        f.write("<p>本文主要介紹我在樹莓派上的物聯網基礎應用實例</p>\n")
        f.write("<p>如何從零程式經驗到程式語言撰寫、IOT實務應用</p>\n")
        f.write("<p>透過Raspberry Pi 的實作快速進入到物聯網領域。</p>\n")
        f.write("</article>\n")
        f.write("<article id=\"Application\">\n")
        f.write("<h2 class=\"major\">Application</h2>\n")
        f.write("<span class=\"image main\"><img src=\"static/images/DHT22_LCD.jpg\" alt=\"\" /></span>\n")
        f.write("<style>li{margin:7px}</style>\n")
        f.write("<p>\n")
        f.write("<li><a href=\"static/images/LED.png\">GPIO & LED 基礎應用</a></li>\n")
        f.write("<li><a href=\"\">樹莓派 結合 超音波測距 / 雷射測距 應用</a></li>\n")
        f.write("<li><a href=\"\">溫濕度感測 & LCD模組 應用</a></li>\n")
        f.write("<li><a href=\"static/images/epaper.jpg\">電子紙 應用</a></li>\n")
        f.write("<li><a href=\"static/images/TM1637-Led-Raspberry-Pi.jpg\">樹莓派結合 七段顯示器 應用</a></li>\n")
        f.write("<li><a href=\"static/images/RFID.jpg\">樹莓派結合 RFID 應用</a></li>\n")
        f.write("<li><a href=\"static/images/retropie.jpg\">用樹莓派打造 Retropie 遊戲機</a></li>\n")
        f.write("</p>\n")
        f.write("<p></p>\n")
        f.write("</article>\n")
        f.write("<article id=\"DHT22\">\n")
        f.write("<h2 class=\"major\">辦公室目前溫濕度</h2>\n")
        f.write("<span class=\"image main\"><img src=\"static/images/bulid.jfif\" alt=\"\" /></span>\n")
        f.write("<p>目前溫度:</p>\n")
        f.write("<p>目前濕度:</p>\n")
        f.write("<p></p>\n")
        f.write("<h5><i>Update Time: 2021.09.14 08:35:52</i></h5>\n")
        f.write("</article>\n")
        f.write("<article id=\"about\">\n")
        f.write("<h2 class=\"major\">About</h2>\n")
        f.write("<span class=\"image main\"><img src=\"static/images/302R.jpg\" alt=\"\" /></span>\n")
        f.write("<p>工程師最基本的能力就是 \"自己判斷問題，並排除\"。</p>\n")
        f.write("<article id=\"contact\">\n")
        f.write("<h2 class=\"major\">Contact</h2>\n")
        f.write("<form method=\"post\" action=\"#\">\n")
        f.write("<div class=\"fields\">\n")
        f.write("<div class=\"field half\">\n")
        f.write("<label for=\"name\">Name</label>\n")
        f.write("<input type=\"text\" name=\"name\" id=\"name\" />\n")
        f.write("</div>\n")
        f.write("<div class=\"field half\">\n")
        f.write("<label for=\"email\">Email</label>\n")
        f.write("<input type=\"text\" name=\"email\" id=\"email\" />\n")
        f.write("</div>\n")
        f.write("<div class=\"field\">\n")
        f.write("<label for=\"message\">Message</label>\n")
        f.write("<textarea name=\"message\" id=\"message\" rows=\"4\"></textarea>\n")
        f.write("</div>\n")
        f.write("</div>\n")
        f.write("<ul class=\"actions\">\n")
        f.write("<li><input type=\"submit\" value=\"Send Message\" class=\"primary\" /></li>\n")
        f.write("<li><input type=\"reset\" value=\"Reset\" /></li>\n")
        f.write("</ul>\n")
        f.write("</form>\n")
        f.write("<ul class=\"icons\">\n")
        f.write("<li><a href=\"#\" class=\"icon brands fa-twitter\"><span class=\"label\">Twitter</span></a></li>\n")
        f.write("<li><a href=\"#\" class=\"icon brands fa-facebook-f\"><span class=\"label\">Facebook</span></a></li>\n")
        f.write("<li><a href=\"#\" class=\"icon brands fa-instagram\"><span class=\"label\">Instagram</span></a></li>\n")
        f.write("<li><a href=\"#\" class=\"icon brands fa-github\"><span class=\"label\">GitHub</span></a></li>\n")
        f.write("</ul>\n")
        f.write("</article>\n")
        f.write("<article id=\"elements\">\n")
        f.write("<h2 class=\"major\">Elements</h2>\n")
        f.write("<section>\n")
        f.write("<h3 class=\"major\">Text</h3>\n")
        f.write("<p>This is <b>bold</b> and this is <strong>strong</strong>. This is <i>italic</i> and this is <em>emphasized</em>.\n")
        f.write("This is <sup>superscript</sup> text and this is <sub>subscript</sub> text.\n")
        f.write("This is <u>underlined</u> and this is code: <code>for (;;) { ... }</code>. Finally, <a href=\"#\">this is a link</a>.</p>\n")
        f.write("<hr />\n")
        f.write("<h2>Heading Level 2</h2>\n")
        f.write("<h3>Heading Level 3</h3>\n")
        f.write("<h4>Heading Level 4</h4>\n")
        f.write("<h5>Heading Level 5</h5>\n")
        f.write("<h6>Heading Level 6</h6>\n")
        f.write("<hr />\n")
        f.write("<h4>Blockquote</h4>\n")
        f.write("<blockquote>Fringilla nisl. Donec accumsan interdum nisi, quis tincidunt felis sagittis eget tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan faucibus. Vestibulum ante ipsum primis in faucibus lorem ipsum dolor sit amet nullam adipiscing eu felis.</blockquote>\n")
        f.write("<h4>Preformatted</h4>\n")
        f.write("<pre><code>i = 0;\n")
        f.write("while (!deck.isInOrder()) {\n")
        f.write("print 'Iteration ' + i;\n")
        f.write("deck.shuffle();\n")
        f.write("i++;\n")
        f.write("}\n")
        f.write("print 'It took' + i + ' iterations to sort the deck.';</code></pre>\n")
        f.write("</section>\n")
        f.write("<section>\n")
        f.write("<h3 class=\"major\">Lists</h3>\n")
        f.write("<h4>Unordered</h4>n")
        f.write("<ul>\n")
        f.write("<li>Dolor pulvinar etiam.</li>\n")
        f.write("<li>Sagittis adipiscing.</li>\n")
        f.write("<li>Felis enim feugiat.</li>\n")
        f.write("</ul>\n")
        f.write("<h4>Alternate</h4>\n")
        f.write("\<ul class=\"alt\">n")
        f.write("<li>Dolor pulvinar etiam.</li>\n")
        f.write("<li>Sagittis adipiscing.</li>\n")
        f.write("<li>Felis enim feugiat.</li>\n")
        f.write("</ul>\n")
        f.write("<h4>Ordered</h4>\n")
        f.write("<ol>\n")
        f.write("<li>Dolor pulvinar etiam.</li>\n")
        f.write("<li>Etiam vel felis viverra.</li>\n")
        f.write("<li>Felis enim feugiat.</li>\n")
        f.write("<li>Dolor pulvinar etiam.</li>\n")
        f.write("<li>Etiam vel felis lorem.</li>\n")
        f.write("<li>Felis enim et feugiat.</li>\n")
        f.write("</ol>\n")
        f.write("<h4>Icons</h4>\n")
        f.write("<ul class=\"icons\">\n")
        f.write("<li><a href=\"#\" class=\"icon brands fa-twitter\"><span class=\"label\">Twitter</span></a></li>\n")
        f.write("<li><a href=\"#\" class=\"icon brands fa-facebook-f\"><span class=\"label\">Facebook</span></a></li>\n")
        f.write("<li><a href=\"#\" class=\"icon brands fa-instagram\"><span class=\"label\">Instagram</span></a></li>\n")
        f.write("<li><a href=\"#\" class=\"icon brands fa-github\"><span class=\"label\">Github</span></a></li>\n")
        f.write("</ul>\n")
        f.write("<h4>Actions</h4>\n")
        f.write("<ul class=\"actions\">\n")
        f.write("<li><a href=\"#\" class=\"button primary\">Default</a></li>\n")
        f.write("<li><a href=\"#\" class=\"button\">Default</a></li>\n")
        f.write("</ul>\n")
        f.write("</section>\n")
        f.write("<section>\n")
        f.write("<h3 class=\"major\">Table</h3>\n")
        f.write("<h4>Default</h4>\n")
        f.write("<div class=\"table-wrapper\">\n")
        f.write("<table>\n")
        f.write("<thead>\n")
        f.write("\<tr>n")
        f.write("<th>Name</th>\n")
        f.write("<th>Description</th>\n")
        f.write("<th>Price</th>\n")
        f.write("</tr>\n")
        f.write("</thead>\n")
        f.write("<tbody>\n")
        f.write("<tr>\n")
        f.write("<td>Item One</td>\n")
        f.write("<td>Ante turpis integer aliquet porttitor.</td>\n")
        f.write("<td>29.99</td>\n")
        f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td>Item Two</td>\n")
        f.write("<td>Vis ac commodo adipiscing arcu aliquet.</td>\n")
        f.write("<td>19.99</td>\n")
        f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td>Item Three</td>\n")
        f.write("<td> Morbi faucibus arcu accumsan lorem.</td>\n")
        f.write("<td>29.99</td>\n")
        f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td>Item Four</td>\n")
        f.write("<td>Vitae integer tempus condimentum.</td>\n")
        f.write("<td>19.99</td>\n")
        f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td>Item Five</td>\n")
        f.write("<td>Ante turpis integer aliquet porttitor.</td>\n")
        f.write("<td>29.99</td>\n")
        f.write("</tr>\n")
        f.write("</tbody>\n")
        f.write("<tfoot>\n")
        f.write("<tr>\n")
        f.write("<td colspan=\"2\"></td>\n")
        f.write("<td>100.00</td>\n")
        f.write("</tr>\n")
        f.write("</tfoot>\n")
        f.write("</table>\n")
        f.write("</div>\n")
        f.write("<h4>Alternate</h4>\n")
        f.write("<div class=\table-wrapper\">\n")
        f.write("<table class=\"alt\">\n")
        f.write("<thead>\n")
        f.write("<tr>\n")
        f.write("<th>Name</th>\n")
        f.write("<th>Description</th>\n")
        f.write("<th>Price</th>\n")
        f.write("</tr>\n")
        f.write("</thead>\n")
        f.write("<tbody>\n")
        f.write("<tr>\n")
        f.write("<td>Item One</td>\n")
        f.write("<td>Ante turpis integer aliquet porttitor.</td>\n")
        f.write("<td>29.99</td>\n")
        f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td>Item Two</td>\n")
        f.write("<td>Vis ac commodo adipiscing arcu aliquet.</td>\n")
        f.write("<td>19.99</td>\n")
        f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td>Item Three</td>\n")
        f.write("<td> Morbi faucibus arcu accumsan lorem.</td>\n")
        f.write("<td>29.99</td>\n")
        f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td>Item Four</td>\n")
        f.write("<td>Vitae integer tempus condimentum.</td>\n")
        f.write("<td>19.99</td>\n")
        f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td>Item Five</td>\n")
        f.write("<td>Ante turpis integer aliquet porttitor.</td>\n")
        f.write("<td>29.99</td>\n")
        f.write("</tr>\n")
        f.write("</tbody>\n")
        f.write("<tfoot>\n")
        f.write("<tr>\n")
        f.write("<td colspan=\"2\"></td>\n")
        f.write("<td>100.00</td>\n")
        f.write("</tr>\n")
        f.write("</tfoot>\n")
        f.write("</table>\n")
        f.write("</div>\n")
        f.write("</section>\n")
        f.write("<section>\n")
        f.write("<h3 class=\"major\">Buttons</h3>\n")
        f.write("<ul class=\"actions\">\n")
        f.write("<li><a href=\"#\" class=\"button primary\">Primary</a></li>\n")
        f.write("<li><a href=\"#\" class=\"button\">Default</a></li>\n")
        f.write("</ul>\n")
        f.write("<ul class=\"actions\">\n")
        f.write("<li><a href=\"#\" class=\"button\">Default</a></li>\n")
        f.write("<li><a href=\"#\" class=\"button small\">Small</a></li>\n")
        f.write("</ul>\n")
        f.write("<ul class=\"actions\">\n")
        f.write("<li><a href=\"#\" class=\"button primary icon solid fa-download\">Icon</a></li>\n")
        f.write("<li><a href=\"#\" class=\"button icon solid fa-download\">Icon</a></li>\n")
        f.write("</ul>\n")
        f.write("<ul class=\"actions\">\n")
        f.write("<li><span class=\"button primary disabled\">Disabled</span></li>\n")
        f.write("<li><span class=\"button disabled\">Disabled</span></li>\n")
        f.write("</ul>\n")
        f.write("</section>\n")
        f.write("<section>\n")
        f.write("<h3 class=\"major\">Form</h3>\n")
        f.write("<form method=\"post\" action=\"#\">\n")
        f.write("<div class=\"fields\">\n")
        f.write("<div class=\"field half\">\n")
        f.write("<label for=\"demo-name\">Name</label>\n")
        f.write("<input type=\"text\" name=\"demo-name\" id=\"demo-name\" value=\"\" placeholder=\"Jane Doe\" />\n")
        f.write("</div>\n")
        f.write("<div class=\"field half\">\n")
        f.write("<label for=\"demo-email\">Email</label>\n")
        f.write("<input type=\"emai\" name=\"demo-email\" id=\"demo-email\" value=\"\" placeholder=\"jane@untitled.tld\" />\n")
        f.write("</div>\n")
        f.write("<div class=\"field\">\n")
        f.write("<label for=\"demo-category\">Category</label>\n")
        f.write("<select name=\"demo-categor\" id=\"demo-category\">\n")
        f.write("<option value=\"\">-</option>\n")
        f.write("<option value=\"1\">Manufacturing</option>\n")
        f.write("<option value=\"1\">Shipping</option>\n")
        f.write("<option value=\"1\">Administration</option>\n")
        f.write("<option value=\"1\">Human Resources</option>\n")
        f.write("</select>\n")
        f.write("</div>\n")
        f.write("<div class=\"field half\">\n")
        f.write("<input type=\"radio\" id=\"demo-priority-low\" name=\"demo-priority\" checked>\n")
        f.write("<label for=\"demo-priority-low\">Low</label>\n")
        f.write("</div>\n")
        f.write("<div class=\"field half\">\n")
        f.write("<input type=\"radio\" id=\"demo-priority-high\" name=\"demo-priority\">\n")
        f.write("<label for=\"demo-priority-high\">High</label>\n")
        f.write("</div>\n")
        f.write("<div class=\"field half\">\n")
        f.write("<input type=\"checkbox\" id=\"demo-copy\" name=\"demo-copy\">\n")
        f.write("<label for=\"demo-copy\">Email me a copy</label>\n")
        f.write("</div>\n")
        f.write("<div class=\"field half\">\n")
        f.write("<input type=\"checkbox\" id=\"demo-human\" name=\"demo-human\" checked>\n")
        f.write("<label for=\"demo-human\">Not a robot</label>\n")
        f.write("</div>\n")
        f.write("<div class=\"field\">\n")
        f.write("<label for=\"demo-message\">Message</label>\n")
        f.write("<textarea name=\"demo-message\" id=\"demo-message\" placeholder=\"Enter your message\" rows=\"6\"></textarea>\n")
        f.write("</div>\n")
        f.write("</div>\n")
        f.write("<ul class=\"actions\">\n")
        f.write("<li><input type=\"submit\" value=\"Send Message\" class=\"primary\" /></li>\n")
        f.write("<li><input type=\"reset\" value=\"Reset\" /></li>\n")
        f.write("</ul>\n")
        f.write("</form>\n")
        f.write("</section>\n")
        f.write("</article>\n")
        f.write("</div>\n")
        f.write("<footer id=\"footer\">\n")
        f.write("<p class=\"copyright\">&copy; Untitled. Design: <a href=\"https://html5up.net\">HTML5 UP</a>.</p>\n")
        f.write("</footer>\n")
        f.write("</div>\n")
        f.write("<div id=\"bg\"><img src=\"static/images/bg.jpg\" alt=\"\" /></div>\n")
        f.write("<script src=\"static/js/jquery.min.js\"></script>\n")
        f.write("<script src=\"static/js/browser.min.js\"></script>\n")
        f.write("<script src=\"static/js/breakpoints.min.js\"></script>\n")
        f.write("<script src=\"static/js/util.js\"></script>\n")
        f.write("<script src=\"static/js/main.js\"></script>\n")
        f.write("</body>\n")
        f.write("</html>\n")

        return app.send_static_file("demo.html")
        #return render_template('demo.html')

if __name__ == '__main__' :
    app.debug = True
    app.run(host='10.192.172.220',port=5000)


