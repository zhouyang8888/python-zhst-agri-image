#!/usr/bin/env python
# coding=utf-8

import xml.etree.ElementTree as ET

class PicInfo:
	def __init__(self, xmltree):
		fullpath = xmltree.find('path').text
		self.relpath = '/'.join(fullpath.split('\\')[3:])
		
		size = xmltree.find('size')
		[self.width, self.height, self.depth] = [int(x.text) for x in size]
		self.bndbox = []
		
		class Bnd:
			def __init__(self, classname, bndbox):
				self.classname = classname
				self.bndbox = bndbox
			def dump(self):
				print 'name = ', self.classname
				for k, v in self.bndbox.items():
					print k, v
		
		objs = xmltree.findall('object')
		for obj in objs:
			classname = obj.find('name').text
			bndbox = dict()
			for xy in obj.find('bndbox'):
				bndbox[xy.tag] = int(xy.text)
			self.bndbox.append(Bnd(classname, bndbox))
	
	def dump(self):
		print self.relpath, self.width, self.height, self.depth
		for bnd in self.bndbox:
			bnd.dump()


def parse(xmlpath):
	return Pic(ET.parse(xmlpath))
