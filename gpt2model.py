from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

tokenizer = GPT2Tokenizer.from_pretrained('') #insert directory of trained model here
model = GPT2LMHeadModel.from_pretrained('', pad_token_id=tokenizer.eos_token_id) #insert directory of trained model here

sentence = "" #insert prompt here

input_ids = tokenizer.encode(sentence, return_tensors='pt')

generated_text_samples = model.generate(
    input_ids, 
    max_length=150,  
    num_return_sequences=5,
    no_repeat_ngram_size=2,
    repetition_penalty=1.5,
    top_p=0.92,
    temperature=.85,
    do_sample=True,
    top_k=125,
    early_stopping=True
)

test = []
for sample in generated_text_samples:
	test.append(tokenizer.decode(sample, skip_special_tokens=True))

print(random.choice(test))
