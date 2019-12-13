import io
import os
import numpy as np
import csv

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

for filename in os.listdir():
	if filename.endswith(".jpg"):
		# The name of the image file to annotate
		file_name = os.path.join(os.path.dirname(__file__),filename)

		# Loads the image into memory
		with io.open(file_name, 'rb') as image_file:
			content = image_file.read()

		image = types.Image(content=content)

		# Performs label detection on the image file
		response = client.label_detection(image=image)
		labels = response.label_annotations

		print('Labels:')
		values = []
		id_ = filename.replace('.jpg','')
		values.append(id_)
		for label in labels:
			print(id_)
			values.append(label.description)
			values.append(label.score)

		with open('labels.csv', 'a',newline='') as f:
			#df.to_csv(f, index = None, header = False) 
			writer = csv.writer(f)
			writer.writerow(values)
		f.close()