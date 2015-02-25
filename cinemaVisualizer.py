#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from PIL import Image



# cinemagraph読み込み
argvs = sys.argv
argc = len(argvs)
if(argc != 2):
	quit()

im = Image.open(argvs[1] + ".gif")

try:
	# 一枚ずつ処理
	while True:
		tmp = im.copy()

		# modeがRGBAでなければ，RGBAに変換
		try:
			if(tmp.mode != "RGB"):
				tmp = tmp.convert("RGB")
		except IOError:
			print "cannot convert", tmp.name

		fig = plt.figure()
		ax = Axes3D(fig)

		# ピクセル値を取り出してscatter
		# l = list(tmp.getdata())
		l = tmp.getcolors()
		counts = [row[0] for row in l]
		colors = [row[1] for row in l]
		r = [row[0] for row in colors]
		g = [row[1] for row in colors]
		b = [row[2] for row in colors]

		colors = [[c/255.0 for c in color] for color in colors]
		ax.scatter3D(r, g, b, color=colors, marker="o", s=[count/10.0 for count in counts])

		# ラベル
		ax.set_xlabel("Red")
		ax.set_ylabel("Green")
		ax.set_zlabel("Blue")
		ax.xaxis.label.set_color("red")
		ax.yaxis.label.set_color("green")
		ax.zaxis.label.set_color("blue")

		# 軸の範囲
		ax.set_xlim(0, 255)
		ax.set_ylim(0, 255)
		ax.set_zlim(0, 255)

		# 保存
		plt.savefig("./" + argvs[1] + "/" + str(im.tell()) + ".gif")
		
		# 次のコマへ
		im.seek(im.tell() + 1)
except EOFError:
	pass
