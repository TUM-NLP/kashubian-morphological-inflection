from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

# print("HF_TOKEN: ", HF_TOKEN)

# source: https://huggingface.co/docs/transformers/v4.28.1/tasks/summarization
from huggingface_hub import login

login(HF_TOKEN)
LANGS = ["grc","dan","fra","sme","deu","nav","jap","klr","eng","mul","deu_eng"]
PATH_JSON_DATA = "../preprocessing_to_json/data/"

for lang in LANGS:
    from datasets import load_dataset
    # dataset= dataset.train_test_split(test_size=0.2) #train_size=10000,
    dataset = load_dataset("json", data_files={"train": PATH_JSON_DATA + lang + "_train.json", "validation": PATH_JSON_DATA + lang + "_eval.json"})

    print(dataset["train"][0])

    from transformers import AutoTokenizer

    checkpoint = "google/byt5-small"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    # -

    import torch

    from transformers import (
        AutoTokenizer,
        TrainingArguments,
        Trainer,
        AutoModelForSeq2SeqLM,
        Seq2SeqTrainingArguments,
        Seq2SeqTrainer
    )
    from datasets import load_dataset

    # prefix = "summarize: "


    def preprocess_function(examples):
        # inputs = [prefix + doc for doc in examples["text"]]
        inputs = examples["text"]
        model_inputs = tokenizer(inputs)

        labels = tokenizer(text_target=examples["summary"]) # same length irrelevant here, so no truncation or padding

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs


    tokenized_dataset = dataset.map(preprocess_function, batched=True)
    print(tokenized_dataset)
    sample = tokenized_dataset["train"][0]
    print(sample["labels"])

    from transformers import DataCollatorForSeq2Seq

    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=checkpoint)

    # import evaluate

    # rouge = evaluate.load("rouge")

    # import numpy as np


    # def compute_metrics(eval_pred):
    #     predictions, labels = eval_pred
    #     decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    #     labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    #     decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    #     result = rouge.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)

    #     prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in predictions]
    #     result["gen_len"] = np.mean(prediction_lens)

    #     return {k: round(v, 4) for k, v in result.items()}

    # import numpy as np
    # import evaluate

    # metric = evaluate.load("accuracy")

    # def compute_metrics(eval_pred):
    #     predictions, labels = eval_pred # TODO: labels vs title?

    #     decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)

    #     labels = np.where(labels != -100, labels, tokenizer.pad_token_id) # TODO: correct?

    #     decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    #     return metric.compute(predictions=predictions, references=labels)

    from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer

    model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    training_args = Seq2SeqTrainingArguments(
        output_dir="byt5-small/"+lang,
        eval_strategy="epoch",
        learning_rate=5e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        weight_decay=0.01,
        save_total_limit=3,
        num_train_epochs=4,
        predict_with_generate=True,
        # save_strategy="epoch",
        fp16=False,# did not work with True #change to bf16=True for XPU 
        # bf16 = True, # because Nvidia Ampere A100 supports bf16
        push_to_hub=True,
        warmup_steps = 500,
        # load_best_model_at_end=True, # otherwise not model with minimum loss during training, like https://huggingface.co/docs/transformers/tasks/sequence_classification
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["validation"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        # compute_metrics=compute_metrics,
    )

    trainer.train()
    trainer.push_to_hub()
