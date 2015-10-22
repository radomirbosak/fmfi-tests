import os.path
from os.path import join, splitext
from os import listdir

import csv
from functools import lru_cache

def get_smart_title(filename):
	onlyfirst = splitext(filename)[0]
		
	namedate = onlyfirst.split("_")
	if len(namedate) >= 2:
		datepart = namedate[1].split('-')
		datepart = '(' + '.'.join(reversed(datepart)) + ')'
	else:
		datepart = ''

	namepart = namedate[0].split('-')
	if len(namepart) >= 2:
		pismeno = namepart[1]
	else:
		pismeno = ''

	correction = {'pis': 'Písomka', 'pisomka': 'Písomka', 'skuskova': 'Skúšková'}
	firstpart = namepart[0]
	try:
		firstpart = correction[firstpart]
	except KeyError:
		pass
	
	return "{firstpart} {pismeno} {datepart}" .format(
			firstpart=firstpart, pismeno=pismeno, datepart=datepart)


def get_rich_files(dirpath, fresh_titlehelper):
	forbidden_extensions = ['.csv']	
	onlyfiles = [ f for f in listdir(dirpath) if os.path.isfile(join(dirpath, f)) ]

	onlyfiles = [f for f in onlyfiles 
		if splitext(join(dirpath, f))[1] not in forbidden_extensions]

	""" (title, path, extension) """
	richfiles = [(get_smart_title(f) if f not in fresh_titlehelper else fresh_titlehelper[f], join(dirpath, f), splitext(join(dirpath, f))[1]) for f in onlyfiles]
	return richfiles

def get_dirs(dirpath):
	return [d for d in listdir(dirpath) if os.path.isdir(join(dirpath, d))]

@lru_cache(maxsize=256)
def read_external_titlehelper(dirpath):
	mydict = dict()
	helper_file_name = 'titles.csv'
	helper_file_path = join(dirpath, helper_file_name)
	if os.path.isfile(helper_file_path):
		with open(helper_file_path, newline='') as f:
			rows = csv.reader(f, delimiter=',')
			for row in rows:
				mydict[row[0]] = row[1]
	return mydict

def dir_to_struct(dirpath, dirname, titlehelper):
	external_titlehelper = read_external_titlehelper(dirpath)
	fresh_titlehelper = dict()
	fresh_titlehelper.update(titlehelper)
	fresh_titlehelper.update(external_titlehelper)

	mydir = {
		'name': dirname,
		'path': dirpath,
		'files': get_rich_files(dirpath, fresh_titlehelper),
		'dirs': list(), }
	mydir['title'] = titlehelper[dirname] if dirname in titlehelper else dirname
	
	for subdir_name in get_dirs(dirpath):
		subdir = dir_to_struct(join(dirpath, subdir_name), subdir_name, fresh_titlehelper)
		mydir['dirs'].append(subdir)

	return mydir
