import random
import re
import torch
import json
import glob

def tokenize(dataset, epochs):
	total_text = '<|endoftext|>' #token
	tweets = [t for t in dataset]
	for _ in range(epochs):
		random.shuffle(tweets)
		total_text += '<|endoftext|>'.join(tweets) + '<|endoftext|>'

	return total_text

def create_dataset(user_id, files, train_dataset_size=0.9):
	user_text = []
	for f in files:
		print(f)
		file_data = open(f, encoding="utf8")

		data = json.load(file_data)

		messages = data["messages"]

		for m in messages:
			if(m["author"]["id"] == user_id):
				user_text.append(m["content"])

	random.shuffle(user_text)
	train_size = int(train_dataset_size * len(user_text))
	valid_size = len(user_text) - train_size
	train_dataset, valid_dataset = torch.utils.data.random_split(user_text, [train_size, valid_size])

	EPOCHS = 4

	with open('{}_train.txt'.format(user_id), 'w') as f:
		data = tokenize(train_dataset, EPOCHS)
		f.write(data)

	with open('{}_valid.txt'.format(user_id), 'w') as f:
		data = tokenize(valid_dataset, 1)
		f.write(data)

if __name__ == "__main__":
	user_id = "" #insert discord id here
	files = glob.glob("*.json")
	create_dataset(user_id, files)
