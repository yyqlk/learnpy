""" @property装饰器就是负责把一个方法变成属性调用的"""
class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,value):
        self._width = value

    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.width)
print(s.height)
print('resolution =', s.resolution)


# 输出
# 1024
# 768
# resolution = 786432