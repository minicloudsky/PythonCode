			 心情驿站
心情驿站给大家提供尽情上网，吐槽心情，分享好心情的地方，我们有如下特色功能:
1 基本的发帖和浏览帖子功能
2 发帖时候可以输入你的个性化昵称，帖子发布时候你可以设置密码，只有你和管理员才能删除你的帖子哦^_^。
3 帖子发布后存入django后台数据库，经过管理员审核即可发布.
4 伊人看电影，可以给大家提供了解和观看最新电影的功能，这些数据是由我们精心从豆瓣电影用python requests类库爬取的数据，有最新和豆瓣评分最高的精彩美剧，也有充满人文视野的最优秀的纪录片。
点击图片即可跳转到豆瓣该电影首页，尽情的和豆瓣网友吐槽，数据写入excel表格，然后由python脚本自动生成html前端代码展示出来，这些电影采用jQuery瀑布流形式无限刷新加载，给你震撼的视觉享受。
5 伊人学编程。
在心情驿站玩的尽兴了，是不是很想知道这些功能是如何实现的?我们给你提供了伊人学编程博客，在这里你可以学习最新的python文件操作，python分布式爬虫的技术，满足你对技术的好奇心。
6 联系管理员功能。
想和管理员吐槽下网站的功能，没问题，管理员欢迎你的来信。 
技术特色:
1 采用python3.5+django1.9+Bootstrap+JQuery开发。
2 伊人博客内容支持markdown语法解析，能够提供html页面解析，支持插入图片，自定义表格和标题。
3 论坛前端模板基于bootstrap，由bootstrap的container等class实现帖子的css样式。
3伊人看电影采用jQuery瀑布流形式加载，先预加载几十张图片，后面的图片由JavaScript进行字符串替换形式将图片插入，实现无限加载图片的效果。
4电影的图片url和标题等数据由python爬虫从豆瓣爬取存入excel，然后由python读取excel后自动生成电影的html代码。
5前端表单采用get和post两种请求，一种原生表单，一种采用django内置表单，充分显示django优秀的技术。
6 django数据库基于MVC框架，同时django深度定制了符合django自身的MTV框架，由models.py 定义数据库，views.py接收前端发起的的HttpRequest,同时views.py进行和数据库进行交互，将后台数据库回传给前端，返回后台数据库的HttpResponse。
7 about页面采用box盒子模型，实现了文字渐入的效果。
代码运行:
在文件夹根目录打开命令行，输入一下命令安装依赖包
python pip install requirements.txt

输入以下命令迁移数据库
python manage.py migrate
python manage.py makemigrations
python  manage.py migrate

输入以下命令，然后打开浏览器，输入 http://127.0.0.1:8000/ 即可运行网站
python manage.py runserver

