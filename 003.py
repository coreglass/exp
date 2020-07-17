import os

# try:
#     f = open('python.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
print(os.path.split("python.txt"))
# print(os.rename("python1.txt","python.txt"))
try:
    open("python1.txt")
except FileNotFoundError:
    print("没有这个文件")