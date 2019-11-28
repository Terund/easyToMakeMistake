def strtest1(num):
    str = "first"
    for i in range(num):
        str += "X"
    return str

"""
解释上面的代码慢在哪？
    由于变量str是个不可变对象，每次迭代，Python都会生成新的str对象来存储新的字符串，num越大，创建的str对象越多，内存消耗越大
"""