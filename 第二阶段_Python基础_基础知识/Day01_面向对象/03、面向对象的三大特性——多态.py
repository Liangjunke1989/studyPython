# 多态：同一个事务的多种状态
# 多态性指的是可以在不考虑对象具体类型的情况下，直接使用对象
class Animal:
    def say(self):
        print("动物可以叫！！！")
class Dog(Animal):
    def say(self):
        print("汪汪汪！！！")
class Cat(Animal):
    def say(self):
        print("喵喵喵！！！")
class Person(Animal):
    def say(self):
        print("哇哇哭！！！")

dog=Dog()
cat=Cat()
person=Person()

print("---------------------------1、多态性,协变-----------------------------------")
## 定义统一的接口，实现多态
def animal_say(animal):
    animal.say()
animal_say(dog)
animal_say(cat)
animal_say(person)

## 多态性
def my_len(val):
    return val.__len__()

print(my_len([1,2,3,4,5]))
print(my_len("hello world"))
print(my_len({"name":"小王","age":18}))

## 鸭子类型不用继承
'''
1. 鸭子类型的概念
    核心思想：「当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子」
    Python实现：不关心对象的具体类型，只关心对象是否具有所需的方法和属性
    动态特性：Python是动态类型语言，支持运行时确定对象行为
2. 鸭子类型与继承的区别?
    （1）鸭子类型的特点：
        灵活性：不需要严格的继承体系
        解耦合：减少类之间的依赖关系
        易扩展：新类型只需实现相应方法即可使用
        符合Python哲学：「We are all consenting adults here」
    （2）继承与鸭子类型的最大不同：    
        继承：
            需要预先设计类层次结构
            修改继承关系成本高
            类之间耦合度较高
        鸭子类型：
            运行时动态确定行为
            可以轻松添加新类型
            类之间松耦合
        类型检查时机
            继承：编译时/静态类型检查（如使用mypy）
            鸭子类型：运行时动态检查，延迟发现问题
'''
# 鸭子类型的实际应用
class FileLikeObject:
    def read(self):
        return "file content"
    def write(self, data):
        pass
def process_data(source):
    # 不关心source的具体类型，只要能read就行
    return source.read()
# 可以处理文件对象、自定义类等
file=FileLikeObject ()
print(process_data(file))

# 鸭子类型与委托、事件的区别？TODO:拓展内容