# flaskr
使用Flask框架制作一个简单的博客网站



## 环境搭建
1.安装flask开发框架

    pip2 install flask

2.写一个最简单的flask测试代码，并运行
    
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return "index page"
    
    if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)


运行命令：

    python flaskr.py

## 生成SQLite3数据库文件

    sqlite3 flaskr.db < schema.sql
    
    root# sqlite3
    > .exit 退出
    > .help 查看帮助命令
    > .database 显示数据库信息，包含当前数据库的位置
    > .tables 显示表名称
    
