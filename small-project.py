recycle_bin = [1,2,"Fastcampus", [], 5,4,5.6,"패스트캠퍼스"]
list(map(lambda x: x**2,filter(lambda x: isinstance(x,int), recycle_bin)))

