import zlib

class a:
    def t(self,s):
        t = zlib.compress(s)
        print(t)
        print(zlib.decompress(t))
ob=a()
k = 'hello world!hello world!hello world!hello world!'
ob.t(k)
