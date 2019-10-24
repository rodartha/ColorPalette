import os
from PIL import Image
import matplotlib.pyplot as plt
from scipy import cluster
import pandas as pd
import math

def get_color_pallete(input_file, output_file, num_colors):
	img = plt.imread(input_file)

	red, green, blue = [], [], []
	for line in img:
		for pixel in line:
			r, g, b = pixel
			red.append(r)
			green.append(g)
			blue.append(b)

	df = pd.DataFrame({
		'red': red,
		'green': green,
		'blue': blue
	})

	df['standardized_red'] = cluster.vq.whiten(df['red'])
	df['standardized_green'] = cluster.vq.whiten(df['green'])
	df['standardized_blue'] = cluster.vq.whiten(df['blue'])

	color_pallete, distortion = cluster.vq.kmeans(df[['standardized_red', 'standardized_green', 'standardized_blue']], num_colors)
	colors = []
	red_std, green_std, blue_std = df[['red', 'green', 'blue']].std()
	for color in color_pallete:
		scaled_red, scaled_green, scaled_blue = color
		colors.append((
			math.ceil(scaled_red * red_std) ,
			math.ceil(scaled_green * green_std) ,
			math.ceil(scaled_blue * blue_std) 
		))

	pil_img = Image.open(input_file)
	pil_width, pil_height = pil_img.size
	height = 0
	if pil_height > pil_width:
		height = math.floor(pil_height / 6)
	else:
		height = math.floor(pil_height / 4)

	pallete = Image.new('RGB', (pil_width, height))
	single_img_width = math.floor(pil_width / num_colors)
	final_img_width = single_img_width + (pil_width - (single_img_width * num_colors))

	x_offset = 0
	for i in range(len(colors)):
		if i == len(colors) - 1:
			new_img = Image.new('RGB', (final_img_width, height), colors[i])
			pallete.paste(new_img, (x_offset, 0))
		else:
			new_img = Image.new('RGB', (single_img_width, height), colors[i])
			pallete.paste(new_img, (x_offset, 0))
		x_offset += single_img_width

	pallete.save(output_file)

def append_color_pallete(original_image, color_pallete, output_file):
	og_img = Image.open(original_image)
	og_width, og_height = og_img.size
	pallete_img = Image.open(color_pallete)
	pallete_width, pallete_height = pallete_img.size

	height_offset = math.ceil(og_height / 16)

	total_width = og_width
	total_height = og_height + pallete_height + height_offset

	pallete_img.resize((total_width, pallete_height), Image.ANTIALIAS)
	pallete_img.save('test.png')

	combined_img = Image.new('RGB', (total_width, total_height), (255, 255, 255))

	combined_img.paste(og_img, (0, 0))
	combined_img.paste(pallete_img, (0, og_height + height_offset))

	combined_img.save(output_file)

def create_pallete(filename, num_colors):
	file_path = filename.split('/')
	file_prefix = ''
	file_split = ''
	for i in range(len(file_path)):
		if i != len(file_path) - 1:
			file_prefix = file_prefix + file_path[i] + '/'
		else:
			file_split = file_path[i]
	file_split = file_split.split('.')
	if file_split[1] != 'jpg' and file_split[1] != 'png':
		raise("The file must be a jpg or png")

	output_palette = file_prefix + file_split[0] + '_pallete.' + file_split[1]
	output_combined = file_prefix + file_split[0] + '_with_pallete.' + file_split[1]
	get_color_pallete(filename, output_palette, num_colors)
	append_color_pallete(filename, output_palette, output_combined)

create_pallete('../blade.jpg', 5)
