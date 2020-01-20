
"""要点：open第三个参数设置为1是行缓冲，写入内容的时候加上换行符文件就会被自动写入
参考：刷新缓冲区的四个条件
"""

# f=open('flush.txt','w+',1)
# while True:
#     data=input('输入内容>>')
#     f.write(data+'\n')



"""或者直接调用flush"""

f=open('flush.txt','w+')
while True:
    data=input('输入内容>>')
    if not data:
        break
    f.write(data)
    f.flush()

f.close()

