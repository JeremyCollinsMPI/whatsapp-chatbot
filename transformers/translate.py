from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

while True:
  new = input()
  batch_input_str = (("我要五個"), (new))
  encoded = tokenizer.prepare_seq2seq_batch(batch_input_str)
  translated = model.generate(**encoded)
  x = tokenizer.batch_decode(translated, skip_special_tokens=True)
  print(x)


# 
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-en")
# tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
# batch_input_str = (("Mary gasta $ 20 en pizza"), ("A ella le gusta comerlo"), ("La pizza estuvo genial"))
# encoded = tokenizer.prepare_seq2seq_batch(batch_input_str)
# translated = model.generate(**encoded)
# x = tokenizer.batch_decode(translated, skip_special_tokens=True)
# print(x)