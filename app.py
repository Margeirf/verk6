import bottle
from bottle import run, route, static_file, error, request, default_app, get, response, template, redirect
import datetime
import html

import os
from os import environ as env
from sys import argv

@route("/")
def index():
    new_items = []
    if request.get_cookie("ny-vara") != None:
        new_items = list(request.get_cookie("ny-vara"))
    return template('index', nyvor=new_items)

@route('/static/<skra:path>')
def static_skrar(skra):
    return static_file(skra, root='./public/')

@route('/vorur')
def sida2():
    item_id = request.query.vara
    ts = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie("ny-vara", item_id, expires=ts)
    if request.get_cookie("ny-vara") != None:
        if len(request.get_cookie("ny-vara")) < 3:
            response.set_cookie("ny-vara", item_id + request.get_cookie("ny-vara"), expires=ts)
        else:
            response.set_cookie("ny-vara", item_id + request.get_cookie("ny-vara")[:-1], expires=ts)

    return template('item', nr=item_id)

bottle.run(host='0.0.0.0', port=argv[1])