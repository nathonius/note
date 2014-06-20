#!/usr/bin/env python
"""Note To Self written by Nathan Smith 6/20/2014"""
import argparse
import os

def main():
	parser = argparse.ArgumentParser(description="Note to Self")
	parser.add_argument('note', nargs='*', help="Your 'note to self'. Omit to retrieve notes.")
	args = parser.parse_args()
	if(args.note):
		takeNote(args)
	else:
		printNotes()

def takeNote(args):
	path = os.path.dirname(__file__)
	relpath = "notes"
	path = os.path.join(path, relpath)
	f = open(path, 'r+')
	noteNumber = 1
	for line in f:
		noteNumber+=1
	f.seek(0, 2)
	note = str(noteNumber)+". "
	for word in args.note:
		note += word + " "
	note += "\n"
	f.write(note)
	f.close()

def printNotes():
	path = os.path.dirname(__file__)
	relpath = "notes"
	path = os.path.join(path, relpath)
	f = open(path, 'r')
	notes = f.read()
	print("Note to self:")
	print notes
	f.close()

if __name__ == "__main__":
    main()
