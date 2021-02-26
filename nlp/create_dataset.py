import random
import re
import torch
import json
import os

FACEBOOK_NAME = ""
DISCORD_AUTHOR_ID = ""

def tokenize(dataset, epochs):
	total_text = '<|endoftext|>' #token
	tweets = [t for t in dataset]
	for _ in range(epochs):
		random.shuffle(tweets)
		total_text += '<|endoftext|>'.join(tweets) + '<|endoftext|>'

	print(len(total_text))
	return total_text

def create_dataset(fb_name, discord_id, files, train_dataset_size=0.9):
	user_text = []
	for source in files:
		filenames = files[source]
		for file in filenames:
			file_data = open("./{}/{}".format(source, file), encoding="utf8")
			data = json.load(file_data)
			messages = data["messages"]

			for m in messages:
				try:
					if source == "fb":
						if m["sender_name"] == fb_name:
							try:
								if "http" not in m["content"]:
									user_text.append(m["content"])
							except:
								pass
					elif source == "discord":
						if m["author"]["id"] == discord_id:
							try:
								if "http" not in m["content"]:
									user_text.append(m["content"])
							except:
								pass
				except:
					pass

	random.shuffle(user_text)
	train_size = int(train_dataset_size * len(user_text))
	valid_size = len(user_text) - train_size
	train_dataset, valid_dataset = torch.utils.data.random_split(user_text, [train_size, valid_size])

	EPOCHS = 4

	with open('{}_train.txt'.format(discord_id), 'w', encoding="utf8") as f:
		data = tokenize(train_dataset, EPOCHS)
		f.write(data)

	with open('{}_valid.txt'.format(discord_id), 'w', encoding="utf8") as f:
		data = tokenize(valid_dataset, 1)
		f.write(data)

if __name__ == "__main__":
	fb_name = FACEBOOK_NAME
	discord_id = DISCORD_AUTHOR_ID

	fb_files = [f for f in os.listdir("./fb/") if f.endswith('.json')]
	discord_files = [f for f in os.listdir("./discord/") if f.endswith('.json')]

	files = {}
	files["fb"] = fb_files
	files["discord"] = discord_files
	create_dataset(fb_name, discord_id, files)
