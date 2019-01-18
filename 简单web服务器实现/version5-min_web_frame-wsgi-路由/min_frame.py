import time

g_url_route = dict()
DOCUMENTS_ROOT = './html'

def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url] = func
        def func2(get_file_name):
            return func(get_file_name)
        return func2
    return func1

@route('/')
def index(get_file_name):
    get_file_name = DOCUMENTS_ROOT + 'index.html'

    print("file name is ===2>%s" % get_file_name)
    try:
        f = open(get_file_name, "rb")
    except IOError:
        response_header = "HTTP/1.1 404 not found\r\n"
        response_header += "\r\n"
        response_body = b"====sorry ,file not found===="
    else:
        response_body = f.read()
        f.close()
    return response_body   

@route("/login.html")   
def login(get_file_name):
    get_file_name = DOCUMENTS_ROOT + get_file_name
    print("file name is ===2>%s" % get_file_name)

    try:
        f = open(get_file_name, "rb")
    except IOError:
        response_header = "HTTP/1.1 404 not found\r\n"
        response_header += "\r\n"
        response_body = b"====sorry ,file not found===="
    else:
        response_body = f.read()
        f.close()
    return response_body

@route("/regist.html")
def regist():
	return 'this is a regiest dynamic web %s' %time.ctime()

@route("/profile.html")
def profile():
	return 'this is profile a dynamic web %s' %time.ctime()

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html;charset=utf-8',)]
    get_file_name = environ["PATH_INFO"]
    start_response(status, response_headers)
    try:
        return g_url_route[get_file_name](get_file_name)
    except:
        return str(environ) + '==no match--->%s\n' % time.ctime()