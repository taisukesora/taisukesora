#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from PIL import Image

# cinemagraph読み込み
im = Image.open("c4.gif")

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
		l = list(tmp.getdata())
		l_uniq = list(set(l))
		colors = np.array(l_uniq)
		ax.scatter3D(colors[:, 0], colors[:, 1], colors[:, 2], color=colors/255.0, marker="o")

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
		plt.savefig("./c4/" + str(im.tell()) + ".gif")

		# 次のコマへ
		im.seek(im.tell() + 1)
except EOFError:
	pass
