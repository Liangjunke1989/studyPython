# 面向对象的三大特性——继承
""""
    继承：
        在Python的面向对象编程中，继承是其中一个核心特性。
        通过继承，子类可以获取父类的属性和方法。
        然而，对于公共属性和私有属性，它们在继承中的表现有所不同：
    公共属性和私有属性的继承区别
    1. 公共属性继承
        公共属性（没有前缀下划线或单下划线）可以直接被子类继承
        子类可以直接访问和使用这些属性
        在示例中，name 属性是公共属性，子类 Dog 和 Girl 都可以正常访问
    2. 私有属性继承
        私有属性（双下划线前缀，如 __sex1 和 __sex2）遵循Python的名称改写机制
        虽然技术上被继承，但不能直接通过实例访问
        Python会将双下划线开头的属性名改写为 _类名__属性名 的形式
        在示例中，Girl 类的 __sex1 和 __sex2 属性无法直接从实例访问
    3. 访问控制
        对于私有属性，通常需要提供公共方法作为访问接口
        如示例中的 get_sex() 方法，提供了对私有属性的安全访问
    这种封装方式可以添加权限控制等逻辑

"""
print("---------------------------1、继承--------------------------------------")
print("--------------01、继承实例1_公共属性-----------------")
class Animal:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def call(self):
        print(f'动物可以叫！！！')

class Dog(Animal):
    def __init__(self,name, age):
        super().__init__(age, name)# 调用父类的构造方法
    def get_attr(self):
        print(f'{self.name}的年龄是{self.age}')# 公共属性
    def call(self):
        super().call()# 调用父类的方法
        print(f'{self.name}汪汪叫！！！')
Dog('旺财', 10).call() #实例化对象调用方法


print("--------------02、继承实例2_私有属性-----------------")

class Person(Animal):
    def __init__(self,name, age,sex,id):
        super().__init__(name,age)# 调用父类的构造方法
        self.sex=sex
        self.id=id
    def get_attr(self):
        print(f'{self.name}的年龄是{self.age},性别是{self.sex}')# 公共属性
    def call(self):
        print(f'{self.name}哇哇哭！！！')
    def __get_id(self):
        print(f'{self.name}的编号是{self.id}')

class Girl(Person):
    # 类常量定义
    MINOR_FEMALE = '未成年女性'
    ADULT_FEMALE = '成年女性'
    VALID_FEMALE_GENDERS = {'女', '女性'}
    ADULT_AGE_THRESHOLD: int = 18

    def __init__(self, name, age, sex):
        super().__init__(name, age, sex, '0001')  # 调用父类的构造方法
        # 输入合法性校验
        if not isinstance(age, int) or age < 0:
            raise ValueError("年龄必须是非负整数")   # raise的作用是抛出异常
        if sex not in self.VALID_FEMALE_GENDERS:
            raise ValueError(f"性别必须是以下之一：{self.VALID_FEMALE_GENDERS}")
    # 封装专门用于设置私有属性公共方法（接口）
    def get_sex(self):
        """
        获取性别信息
        Returns:
            str: 根据年龄和性别返回对应的性别描述或错误信息
        """
        if self.sex in self.VALID_FEMALE_GENDERS:
            if self.age >= self.ADULT_AGE_THRESHOLD:
                return self.ADULT_FEMALE
            else:
                return self.MINOR_FEMALE
        return '性别录入错误！'
g1 = Girl('小丽', 11, '女')
print(g1.get_sex())

g2 = Girl('小刘', 18, '女性')
print(g2.get_sex())

# g3 = Girl('小萌', 21, '女人')
# print(g3.get_sex())

print("--------------03、继承实例3_私有方法-----------------")
class Bird(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def __fly(self):
        print(f'我叫{self.name}，年龄{self.age}岁了，可以飞了！！！')
    def call(self):
        super().call()
        self.__fly()
bird=Bird('小鸽子', 1)
bird.call()


