def add(a, b):
    return a + b

def product(a, b):
	return a * b

if __name__ == '__main__':
    import sys
    args = sys.argv  # 用于获取命令行参数
    if args[1] == "product":
    	print(args)
    	print(product(int(args[2]), int(args[3])))
    elif args[1] == "add":
    	print(args)
    	print(add(int(args[2]), int(args[3])))