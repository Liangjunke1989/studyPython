# classmethod
mysql_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'db': 'test_db'
}
"""
    类方法：
        类方法：类方法，类方法第一个参数是cls，cls表示类本身
"""
print("---------------------------1、classmethod 类方法--------------------------------------")
class Mysql:
    def __init__(self,host,port,user,password,db):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
    def connect(self):
        print(f'连接数据库：{self.host}，端口：{self.port}，用户名：{self.user}，密码：{self.password}，数据库：{self.db}')
    @classmethod #类方法
    def get_mysql_config(cls):
        return cls(**mysql_config)#返回的是一个实例化对象
mysql=Mysql.get_mysql_config()
print( mysql.__dict__) #__dict__属性返回 对象属性的字典
print(mysql.connect())

print("---------------------------2、staticmethod方法--------------------------------------")
"""
    静态方法：静态方法，静态方法第一个参数是self，self表示对象本身
"""
class Mysql:
    def __init__(self,host,port,user,password,db):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
    @staticmethod
    def create_id():
        import  uuid
        return uuid.uuid4()
mysql=Mysql('localhost',3306,'root','password','test')
print(mysql.create_id())
print(Mysql.create_id())

print("---------------------------3、类方法和静态方法的不同--------------------------------------")
"""
    类方法和静态方法不同：
        1、类方法第一个参数是cls，cls表示类本身
        2、静态方法第一个参数是self，self表示对象本身
        3、继承中的表现不同：
            类方法：在子类中调用时，cls 参数指向子类
            静态方法：在子类中表现与父类相同，无特殊行为
            类方法主要用于需要访问类本身或类属性的场景，
            而静态方法适用于与类相关但不需要访问类或实例数据的工具函数。   
"""