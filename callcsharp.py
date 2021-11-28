import collections

from pydotnet.clr import CLRApi
from pydotnet import *


clr = CLRApi(dll=r'C:\Users\dharr\source\repos\PythonExport2\PythonExport2\bin\Release\netstandard2.0\PythonExport2.dll',
             hostname='127.0.0.1')

obj = clr.new('PythonExport2.Tester')

ret = obj.TestExport(2, 4)


for i in range(120000000000):
    print(obj.TestExport(i, 1 + 2))







