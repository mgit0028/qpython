#一些重要的内建函数

函数	描述
abs(number)	返回一个数的绝对值
apply(function[, args[, kwds]])	调用给定函数，可选择提供参数
all(iterable)	如果所有iterable的元素均为真则返回True, 否则返回False
any(iterable)	如果有任一iterable的元素为真则返回True，否则返回False
basestring()	str和unicode抽象超类，用于检查类型
bool(object)	返回True或False，取决于Object的布尔值
callable(object)	检查对象是否可调用
chr(number)	返回ASCII码为给定数字的字符
classmethod(func)	通过一个实例方法创建类的方法
cmp(x, y)	比较x和y——如果x<y，则返回负数；如果x>y则返回证书；如果x==y，返回0
complex(real[, imag])	返回给定实部（以及可选的虚部）的复数
delattr(object, name)	从给定的对象中删除给定的属性
dict([mapping-or-sequence])	构造一个字典，可选择从映射或（键、值）对组成的列表构造。
也可以使用关键字参数调用。
dir([object])	当前可见作用于域的（大多数）名称的列表，
或者是选择性地列出给定对象的（大多数）特性
divmod(a, b)	返回(a//b, a%b)（float类型有特殊规则）
enumerate(iterable)	对iterable中的所有项迭代（索引，项目）对
eval(string[, globals[, locals]])	对包含表达式的字符串进行计算。
可选择在给定的全局作用域或者局部作用域中进行
execfile(file[, globals[, locals]])	执行一个python文件，
可选在给定全局作用域或者局部作用域中进行
file(filename[, mode[, bufsize]])	创建给定文件名的文件，
可选择使用给定的模式和缓冲区大小
filter(function, sequence)	返回给定序列中函数返回值的元素的列表
float(object)	将字符串或者数值转换为float类型
frozenset([iterable])	创建一个不可变集合，这意味着不能将添加到其它集合中
getattr(object, name[, default])	返回给定对象中所指定的特性的值，可选择给定默认值
globals()	返回表示当前作用域的字典
hasattr(object, name)	检查给定的对象是否有指定的属性
help([object])	调用内建的帮助系统，或者打印给定对象的帮助信息
id(number)	返回给定对象的唯一ID
input([prompt])	等同于eval(raw_input(prompt)
int(object[, radix])	将字符串或者数字（可以提供基数）转换为整数
isinstance(object, classinfo)	检查给定的对象object是否是给定的classinfo值的实例，
classinfo可以是类对象、类型对象或者类对象和类型对象的元组
issubclass(class1, class2)	检查class1是否是class2的子类（每个类都是自身的子类）
iter(object[, sentinel])	返回一个迭代器对象，可以是用于迭代序列的object_iter()迭代器
（如果object支持_getitem_方法的话），或者提供一个sentinel，
迭代器会在每次迭代中调用object，直到返回sentinel
len(object)	返回给定对象的长度（项的个数）
list([sequence])	构造一个列表，可选择使用与所提供序列squence相同的项
locals()	返回表示当前局部作用域的字典（不要修改这个字典）
long(object[, radix])	将字符串（可选择使用给定的基数radix）或者数字转化为长整型
map(function, sequence, ...)	创建由给定函数function应用到所提供列表sequence每个项目时返回的值组成的列表
max(object1, [object2, ...])	如果object1是非空序列，那么就返回最大的元素。
否则返回所提供参数（object1,object2...）的最大值
min(object1, [object2, ...])	如果object1是非空序列，那么就返回最小的元素。
否则返回所提供参数（object1,object2...）的最小值
object()	返回所有新式类的技术Object的实例
oct(number)	将整型数转换为八进制表示的字符串
open(filename[, mode[, bufsize]])	file的别名（在打开文件的时候使用open而不是file
ord(char)	返回给定单字符（长度为1的字符串或者Unicode字符串）的ASCII值
pow(x, y[, z])	返回x的y次方，可选择模除z
property([fget[, fset[, fdel[, doc]]]])	通过一组访问器创建属性
range([start, ]stop[, step])	使用给定的起始值（包括起始值，默认为0）和结束值（不包括）
以及步长（默认为1）返回数值范围（以列表形式）
raw_input([prompt])	将用户输入的数据作为字符串返回，可选择使用给定的提示符prompt
reduce(function, sequence[, initializer])	对序列的所有渐增地应用于给定的函数，
使用累积的结果作为第一个参数，
所有的项作为第二个参数，可选择给定的起始值（initializer）
reload(module)	重载入一个已经载入的模块并将其返回
repr(object)	返回表示对象的字符串，一般作为eval的参数使用
reversed(sequence)	返回序列的反向迭代器
round(float[, n])	将给定的浮点数四舍五入，小数点后保留n位（默认为0）
set([iterable)	返回从iterable（如果给出）生成的元素集合
setattr(object, name, value)	设定给定对象的指定属性的值为给定的值
sorted(iterable[, cmp][,key][, reverse])	从iterable的项目中返回一个新的排序后的列表。
可选的参数和列表方法与sort中的相同
staticmethod(func)	从一个实例方法创建静态（类）方法
str(object)	返回表示给定对象object的格式化好的字符串
sum(seq[, start])	返回添加到可选参数start（默认为0）中的一系列数字的和
super(type[, obj/type)	返回给定类型（可选为实例化的）的超类
tuple([sequence])	构造一个元祖，可选择使用同提供的序列sequence一样的项
type(object)	返回给定对象的类型
type(name, base, dict)	使用给定的名称、基类和作用域返回一个新的类型对象
unichr(number)	chr的Unicode版本
unicode(object[, encoding[, errors]])	返回给定对象的Unicode编码版本，可以给定编码方式和处理错误的模式
（'strict'、'replace'或者'ignore'，'strict'为默认模式）
vars([object])	返回表示局部作用域的字典，或者对应给定对象特性的字典
xrange([start, ]stop[, step])	类似于range，但是返回的对象使用内存较少，而且只用于迭代
zip(sequence1, ...)	返回元组的列表，每个元组包括一个给定序列中的项。
返回的列表的长度和所提供的序列的最短长度相同