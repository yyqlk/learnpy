# AUTHOR : YYQLK
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('found model:%s'% name)
        mappings=dict()
        for k, v in attrs.items():
            if isinstance(v,Field):
                mappings[k] = v
                print('found mappings:%s==>%s'%(k,v))
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__' ]= name
        return type.__new__(cls, name, bases, attrs) #这句话是干什么用的？


class Model(dict, metaclass=ModelMetaclass):      #编写基类用来定义子类的基本方法
    def __init__(self,**kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s(%s) values (%s)'%(self.__table__, ','.join(fields), ','.join(params))
        print('sql:%s'%sql)
        print('args:',args)

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')

# 保存到数据库：
u.save()


