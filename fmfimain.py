from bottle import route, run, template, static_file, abort, error

import os.path
from os.path import join, splitext
from os import listdir

# local modules
from predmety import *
from config import *
from aux import read_external_titlehelper, dir_to_struct

predmety_dict = {abbrev: (abbrev, class_, title) for (abbrev, class_, title) in predmety}

@route('/')
def index():
	bcmgr = 'bc'
	d = {
		'predmety': predmety_bak,
		'updated': updated,
		'base': base_url,
		'bcmgr': bcmgr,
		'include_page': 'default',
		'content': {}, }

	return template('index', **d)

@route('/c/<name:re:[a-z0-9]+>')
def category(name):
	bcmgr = 'bc'
	if name == 'bak':
		custom_predmety = predmety_bak
	elif name == 'mag':
		custom_predmety = predmety_mag
		bcmgr = 'mgr'
	else:
		custom_predmety = predmety

	d = {
		'predmety': custom_predmety,
		'updated': updated,
		'bcmgr': bcmgr,
		'base': base_url,
		'include_page': 'default',
		'content': {}, }

	return template('index', **d)

@route('/s/<name:re:[a-z0-9]+>')
def subject(name):
	rootdir = 'files'
	predmet_dir = os.path.join(rootdir, name)

	if not os.path.isdir(predmet_dir) or name not in predmety_dict:
		abort(404, "No such predmet.")

	external_titlehelper = read_external_titlehelper('.')
	titlehelper = dict()
	titlehelper.update(external_titlehelper)

	bcmgr = 'bc' if predmet_to_studium[name] == predmety_bak else 'mgr'

	page = dir_to_struct(predmet_dir, name, titlehelper)
	page['title'] = predmety_dict[name][2]

	d = {
		'predmety': predmet_to_studium[name],
		'updated': updated,
		'base': base_url,
		'bcmgr': bcmgr,
		'include_page': 'predmet',
		'content': page, }

	return template('index', **d)

@route('/static/<filepath:path>')
def callback(filepath):
	return static_file(filepath, root='./static/')

@route('/files/<filepath:path>')
def callback(filepath):
	return static_file(filepath, root='./files/')

@error(404)
def error404(error):
	return template('error404', base=base_url)


# @error(404)
# def error404(error):
# 	return "nothing here"

run(host='localhost', port=port)