## Discord bot
### Training NLP model

 - Obtained discord chat log using [DiscordChatExported](https://github.com/Tyrrrz/DiscordChatExporter) in JSON format
 - Isolated messages from user using ID by running create_dataset.py
 - Train NLP model using [run_clm.py](https://github.com/huggingface/transformers/blob/master/examples/language-modeling/run_clm.py) on datasets created by running the following script:

    python run_clm.py --model_name_or_path gpt2 --train_file=<TRAIN_DATASET> --validation_file=<VALIDATE_DATASET> --do_train --do_eval --output_dir=<OUTPUT_DIRECTORY> --block_size=32
