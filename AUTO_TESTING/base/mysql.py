# 提供于数据库相关的操作方法
import pymysql

def get_verifycode(session):
    # 定义SQL语句
    sql = "SELECT code FROM ds_verifycode WHERE session='"+session+"' ORDER BY id DESC LIMIT 0,1;"
    # 调用执行方法
    verifycode = execute_sql(sql)[0][0]
    # 返回验证码
    return verifycode    

def execute_sql(sql):
    # 连接数据库
    db =pymysql.connect("172.31.31.100", "root", "123456","p2p3")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询   
    cursor.execute(sql)
    # 使用 fetchall() 方法获取所有数据
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    # 返回数据内容
    return data

if __name__ == "__main__":
    print(get_verifycode("jinld2n4oeg845v6u78c8vnjs0"))
    
    