###############################
# 方法一：将import语句移到函数内部 #
###############################
def f1():
	from complicated import foo
	foo()
	import sys
	print(sys.modules)

def f2():
	from complicated import foo
	foo()


###########################################
# 方法二：继承ModuleType并实现__getattr__方法 #
###########################################
import tflazyload  # prints nothing
tflazyload.complicated.f


############################################
# 方法三：利用Python3.7+ 的模块__getattr__方法 #
############################################
import nativelazyload
nativelazyload.complicated.fo

