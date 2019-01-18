import time

def login():
	return 'this is a login dynamic web %s' %time.ctime()
def regist():
	return 'this is a regiest dynamic web %s' %time.ctime()
def profile():
	return 'this is profile a dynamic web %s' %time.ctime()

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    get_file_name = environ["PATH_INFO"]
    start_response(status, response_headers)
    if get_file_name == "/login.py":
    	return login()	
    else:
    	return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()