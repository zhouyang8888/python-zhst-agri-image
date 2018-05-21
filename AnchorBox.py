#!/usr/bin/env python
# coding=utf-8

import numpy as np

class AnchorBox:
	def __init__(self, scale, ratio, centors, area=16):
		boxes = []
		new_area = area * np.array(scale)
		new_edge_length = np.sqrt(new_area)
		new_root_ratio = np.sqrt(ratio)
		for edge_length in new_edge_length:
			for root_ratio in new_root_ratio:
				boxes.append((edge_length * root_ratio, edge_length / root_ratio))
		
		self.boxes = []
		boxes = np.array(boxes) / 2
		for b in boxes:
			print b
		for centor in centors:
			for box in boxes:
				x = (centor[0] - box[0], centor[1] - box[1], centor[0] + box[0], centor[1] + box[1])
				self.boxes.append(x)
	
	def dump(self):
		for box in self.boxes:
			print "(xmin, ymin, xmax, ymax) : ", box


if __name__ == "__main__":
	boxes = AnchorBox(scale=[0.25, 1, 4], ratio=[0.25, 1, 4], centors=[(16, 16), (32, 32)], area=64)
	boxes.dump()


