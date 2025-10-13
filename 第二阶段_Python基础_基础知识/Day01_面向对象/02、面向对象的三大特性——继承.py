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
    """
        super()：
            super() 是Python内置函数，用于调用父类(超类)的方法
            主要用于继承关系中，实现方法重写和扩展
    """
    def __init__(self,name, age):
        super().__init__(name, age)# 调用父类的构造方法
    def get_attr(self):
        print(f'{self.name}的年龄是{self.age}')# 公共属性
    def call(self):
        super().call()# 调用父类的方法
        print(f'{self.age}岁的{self.name},汪汪叫！！！')
Dog('旺财', 10).call() #实例化对象调用方法


print("--------------02、继承实例2_私有属性-----------------")

class Person(Animal):
    def __init__(self,name, age,sex,id):
        super().__init__(name,age)# 调用父类的构造方法
        self.sex=sex    # 重写
        self.id=id
    def get_attr(self):
        print(f'{self.name}的年龄是{self.age},性别是{self.sex}')# 公共属性
    def get_id(self):
        print(f'{self.name}的编号是{self.id}')
    def call(self):
        super().call()
        print(f'{self.name}哇哇哭！！！')

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
        Animal.__init__(self,name,age)# 调用父类的构造方法
    def __fly(self):
        print(f'我叫{self.name}，年龄{self.age}岁了，可以飞了！！！')
    def call(self):
        super().call()
        self.__fly()
bird=Bird('小鸽子', 1)
bird.call()
print("--------------04、Python继承特性_多继承-----------------")
"""
    多继承：
        和其他编程语言不同（如Java/C#）有说不同，Java支持单继承
        Python支持多个父类
        Python支持多个父类继承关系
        多个父类继承关系中，子类对象可以替代多个父类对象使用
        
        魔术变量方法mro(),可以表示类与类之间的继承关系
"""
class Parrot(Bird, Person):
    """
        避免在多重继承中使用 super() 传递不同参数
        建议显式调用具体父类的方法
    """
    def __init__(self,name,age):
        # 显式调用父类构造函数，提供所需的参数
        Bird.__init__(self, name, age)
        Person.__init__(self, name, age, '未知', '1002')
    def call(self):
        super().call()
        Person.get_id(self)
        print(f'{self.name}可以学习人说话！！！')

parrot=Parrot('小鹦鹉', 3)
parrot.call()

print("--------------05、继承拓展1_重写-----------------")

class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def call(self):
        super().call()
        print(f'{self.name}喵喵喵！！！')
cat1=Cat('小猫', 2)
cat1.call()

print("--------------05、继承拓展2_逆变和协变-----------------")
"""
    协变(Covariance): 子类对象可以替代父类对象使用
    逆变(Contravariance): 父类对象可以替代子类对象使用
    不变(Invariance): 既不支持协变也不支持逆变
"""
print("---------------------------00、原始-------------------------")
class A:
    def show(self, x: int) -> str:
        return "A"
class B:
    def show(self, x: float) -> str:
        return "B"
class C(A, B):
    def show(self, x) -> str:
        result_a=A.show(self,x)
        result_b=B.show(self,x)
        return f"{result_a},{result_b},C"

c1=C() #优先继承 A，继承链，继承了多个父类，优先继承最近的父类
print(C.mro()) # mro()方法返回继承关系,不清楚继承关系的时候可以使用mro()方法查看继承关系
print(c1.show('121c1c'))

print("---------------------------01、协变-------------------------")
# 协变: 子类对象可以替代父类对象使用
def process_animal(animal: Animal): # 参数类型为Animal
    animal.call()
dog=Dog('旺财', 10)
process_animal(dog) #   传值为子类(Dog是Animal的子类)，协变允许这种替换
bird=Bird('小鸽子1', 11)
process_animal(bird)

# 协变 - Sequence[Dog]可以当作Sequence[Animal]使用
from typing import Sequence
dogs: Sequence[Dog] = [Dog('旺财', 10)]
animals: Sequence[Animal] = dogs  # 这是允许的

print("---------------------------02、逆变-------------------------")
# 逆变: 父类对象可以替代子类对象使用
from typing import Callable
# 函数参数的逆变
def feed_animal(animal: Animal) -> None:
    print("Feeding animal")
def feed_dog(dog: Dog) -> None:
    print("Feeding dog")
# 逆变 - Callable[..., Dog]可以当作Callable[..., Animal]使用
handler1: Callable[[Animal], None] = feed_animal # 逆变：能处理Animal的函数也能处理Dog
handler2: Callable[[Dog], None] = feed_dog # 逆变
handler1(Dog("旺财22", 13)) # 正确,调用的是父类的方法
handler2(Dog("旺财22", 13)) # 正确,调用的是子类的方法
print("---------------------------03、不变-------------------------")
# 不变: 既不支持协变也不支持逆变
# 不变 - Sequence[Dog]不能当作Sequence[Animal]使用




