from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import load_dataset
import random
import numpy
# get tokenizer and sentinal tokens for masking
tokenizer = AutoTokenizer.from_pretrained("google/byt5-small")
extra_id_0 = tokenizer.convert_tokens_to_ids("<extra_id_0>")
print(extra_id_0, extra_id_1)

# Load pre-trained model
model = AutoModelForSeq2SeqLM.from_pretrained("google/byt5-small")
data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, return_tensors="pt")
random.seed(10)

def preprocess_function(examples): # receives unmasked sentence as input

    inputs_batch = examples["input"]
    print(inputs_batch)
    for inputs in inputs_batch:
        inputs = inputs.strip()
        model_inputs = tokenizer(inputs)
        print(model_inputs)
        input_ids = model_inputs.input_ids
        attention_mask = model_inputs.attention_mask
        # print(input_ids, attention_mask, len(input_ids),len(attention_mask))
        print(input_ids)
        # mask 15% of the bytes randomly in the tokenized sentence leaving out bordering bytes.
        print(len(input_ids))
        length = round(len(input_ids) * 0.15) # mask 15% of character (T5 and mT5 do that for tokens)
        print(length)
        return length

from array import array
# load dataset
lang = "csb-pol-sent"
train_path = f"<path_to>/kashubian-morphological-inflection/preprocessing/preprocessing_to_json_or_tsv/data/{lang}_trn.tsv"
eval_path = f"<path_to>/kashubian-morphological-inflection/preprocessing/preprocessing_to_json_or_tsv/data/{lang}_dev.tsv"
dataset = load_dataset("csv", delimiter="\t",column_names=["input"],data_files={"train": train_path,"validation": eval_path},quoting=3) # disable quote parsing
mean_train = numpy.mean(
    list(map(preprocess_function, dataset["train"]))
)
mean_train = numpy.mean ( map(preprocess_function, dataset["train"]) ) 
mean_dev = numpy.mean ( dataset["validation"]["input"].map(preprocess_function) )
mean = numpy.mean ( dataset["validation"]["input"].map(preprocess_function) + dataset["train"]["input"].map(preprocess_function) )
print(mean)
