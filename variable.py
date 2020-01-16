# 第二章
# 变量
message = "hello python world"
print(message)

# 变量的命名和使用
# 变量名只能包含字母、数字和下划线。但不能以数字开头，例如，message_1,但不能将其命名 1_message 。
# 变量中不能含有空格
# 不要将python 关键字和函数名用作变量名

# 字符串
print("This is a string.")
print('This is also a string.')

# 使用方法修改字符串的大小写
name = "ada lovelace"
print(name.title())  # Ada Lovelace
print(name.upper())  # ADA LOVELACE
print(name.lower())  # ada lovelace

# 合并（拼接）字符串
first_name = "ada lovelace"
last_name = "love"
full_name = first_name + last_name
print(full_name)
print("hello," + full_name.title() + "!")

# 使用制表符或换行符添加空白
print("\tPython")
print("python")
print("Language:\nPython\nC\nJavascript")
print("Language:\n\tPython\n\tC\n\tJavascript")

# 删除空白
favorite_language = " python "
# print(favorite_language.strip()) #删除前后空白
print(favorite_language.rstrip())  # 删除末尾空白
print(favorite_language.lstrip())  # 删除前面空白

# 转义符 \
# 例如：'One of Python\' strength is its diverse community.' python后面加了 \

# 整数
print(2 + 3)
print(2 / 3)
print(5 // 2)  # 取商
print(2 ** 3)  # 乘方

# 浮点数
print(0.1 + 0.1)

# 使用str()避免类型错误
age = 23
print("Happy " + str(age) + "rd Birthday")

