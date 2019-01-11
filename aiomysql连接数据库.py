import asyncio
import aiomysql
import logging

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

@asyncio.coroutine
def select(sql):
    logging.info(sql)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql)
        yield from cur.close()

@asyncio.coroutine
def create_connect(loop,sql):
    yield from create_pool(loop, user="root", password="root", db="awesome")
    yield from select(sql)


sql = "insert into users (id, email, passwd, admin, name) values ('2', 'test2', '123', 2, 'test2');"
loop = asyncio.get_event_loop()
loop.run_until_complete(create_connect(loop,sql))
loop.run_forever()