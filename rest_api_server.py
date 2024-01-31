from bottle import *

from pprint import pprint

import time

import algebra

 

# query , vary header, set cookie


secret = 'CS218 is a Masters class'

 

@route('/')

def welcome():

    pprint(dict(request.headers))

    response.set_header('Vary', 'Accept')

    if 'text/html' in request.headers.get('Accept', '*/*'):

        response.content_type = 'text/html'

        return '<h1>Welcome to CS 218!!!</h1>'

  

    response.content_type = 'text/plain'

    return 'hello'

 

@route('/now')

def time_server():

    response.content_type = 'text/plain'

    response.set_header('Cache-Control', 'max-age=30')

    return time.ctime()

 

@route('/upper/<word>')

def upper_case_service(word):

    response.content_type = 'text/plain'

    return word.upper()

 

@route('/area/circle')
def circle_area_service():

    # last_visit = request.get_cookie('last-visit', 'unknown')

    last_visit = request.get_cookie('last-visit', 'unknown', secret=secret) 

    print(f'Last visit {last_visit}')

    response.set_header('Vary', 'Accept')

    # response.set_cookie('last-visit', time.ctime())

    response.set_cookie('last-visit', time.ctime(), secret=secret)

    pprint(dict(request.query))

    try:

        radius = float(request.query.get('radius', '0.0'))

    except ValueError as e:

        return e.args[0]

 

    area = algebra.area_circle(radius)

 

    if 'text/html' in request.headers.get('Accept', '*/*'):

        response.content_type = 'text/html'

        return f'<p>The area of the circle is <em>{area}</em> </p>'

 

    return dict(radius=radius, area=area, service=request.path)

    #return 'Test %r ' % area

 

if __name__ == '__main__':

    run(host='localhost', port='8080')