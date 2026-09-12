# import torch
# from transformers import pipeline

# pipeline = pipeline(
#     task="text2text-generation",
#     model="google/byt5-small",
#     dtype=torch.float16,
#     device=0
# )

# pipeline("translate English to French: The weather is nice today")

# import torch
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained(
#     "google/byt5-small"
# )
# model = AutoModelForSeq2SeqLM.from_pretrained(
#     "google/byt5-small",
#     dtype=torch.float16,
#     device_map="auto"
# )

# input_ids = tokenizer("go + PST -> went\n help + PST -> helped\n know + PST ->", return_tensors="pt").to(model.device)

# output = model.generate(**input_ids)
# print("hello")
# print(tokenizer.decode(output[0], skip_special_tokens=True))

import torch
from transformers import TorchAoConfig, AutoModelForSeq2SeqLM, AutoTokenizer

quantization_config = TorchAoConfig("int4_weight_only", group_size=128)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "google/byt5-xl",
    dtype=torch.bfloat16,
    device_map="auto",
    quantization_config=quantization_config
)

tokenizer = AutoTokenizer.from_pretrained("google/byt5-xl")
input_ids = tokenizer("translate English to French: The weather is nice today.", return_tensors="pt").to(model.device)

output = model.generate(**input_ids)
print(tokenizer.decode(output[0], skip_special_tokens=True))