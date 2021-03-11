
## Discord bot
### Creating Datasets
The current dataset creation is based on Discord and Facebook chatlogs. Both chatlogs must be in JSON format.

- Discord chat logs are obtained using [DiscordChatExported](https://github.com/Tyrrrz/DiscordChatExporter).
- Facebook chat logs are obtained by going to Setting > Your Facebook Information > Download a copy of your information.

The datasets are created using [create_dataset.py](https://github.com/jdamascoty/discordbot/blob/main/nlp/create_dataset.py). Run the code after changing lines 7 and 8 to include the Facebook name and Discord author ID of the targeted user.

    FACEBOOK_NAME = ""
    DISCORD_AUTHOR_ID = ""

Running [create_dataset.py](https://github.com/jdamascoty/discordbot/blob/main/nlp/create_dataset.py) will create two text files named <DISCORD_AUTHOR_ID>_train.txt and <DISCORD_AUTHOR_ID>_test.txt

### Training NLP model

- Train NLP model using [run_clm.py](https://github.com/huggingface/transformers/blob/master/examples/language-modeling/run_clm.py) from HuggingFace on the datasets created by running the following script:

`python run_clm.py --model_name_or_path gpt2 --train_file=<TRAIN_DATASET> --validation_file=<VALIDATE_DATASET> --do_train --do_eval --output_dir=<OUTPUT_DIRECTORY> --block_size=32`

### Running the trained model
- Change lines 4 and 5 in [gpt2model.py](https://github.com/jdamascoty/discordbot/blob/main/nlp/gpt2model.py) to include the directory of the trained model. 

`tokenizer = GPT2Tokenizer.from_pretrained('')`
`model = GPT2LMHeadModel.from_pretrained('', pad_token_id=tokenizer.eos_token_id)`
