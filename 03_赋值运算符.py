a = 21
b = 10
c = 0

# 简单的赋值运算符
c = a + b
print("1 - c 的值为：", c)

# 加法赋值运算符
c += a
print("2 - c 的值为：", c)

# 乘法赋值运算符
c *= a
print("3 - c 的值为：", c)

# 除法赋值运算符
c /= a
print("4 - c 的值为：", c)

c = 2
# 取模赋值运算符
c %= a
print("5 - c 的值为：", c)

# 幂赋值运算符
c **= a
print("6 - c 的值为：", c)

# 取整除赋值运算符
c //= a
print("7 - c 的值为：", c)

# 海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。
# 在这个示例中，赋值表达式可以避免调用 len() 两次:
texta = "aaaaaaaaaaaaa"
if (n := len(texta)) > 10:
    print(f"长度：{n} , 预设 <= 10)")
