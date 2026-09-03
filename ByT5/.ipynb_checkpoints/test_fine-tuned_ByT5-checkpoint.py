from dotenv import load_dotenv
import os
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

from huggingface_hub import login
login(HF_TOKEN)

LANGS = ["grc","dan","fra","sme","deu","nav","jap","klr","eng","mul","deu_eng"]
for lang in LANGS:
    import torch
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    PRETRAINED_MODEL = "google/byt5-small"
    FINETUNED_MODEL ="livles/byt5-small/"+lang
    FINETUNED_MODEL ="./byt5-small"+lang
    MODEL = FINETUNED_MODEL
    print(MODEL)
    tokenizer = AutoTokenizer.from_pretrained(
        FINETUNED_MODEL,
    )
    model = AutoModelForSeq2SeqLM.from_pretrained(
        FINETUNED_MODEL,
    dtype=torch.float16,
    device_map="auto"
    )

    from datasets import load_dataset
    OUT_DIR = "output_byt5_small/"
    PATH = "../preprocessing_to_json/data/" + LANG + "_test.json"
    PATH_ORIG = "../2023InflectionST/part1/data/" + LANG + ".tst"
    LEN = 1000
    with open (OUT_DIR + LANG + "_byt5-small.out","w") as out_file, open (PATH_ORIG, "r") as test_file:
        COUNTER = 0
        dataset = load_dataset("json",data_files={"test":PATH})
        covered_test_lines = dataset["test"]["text"]


        # preds = map (generate,covered_test_lines)
        for line in covered_test_lines:
            input_ids = tokenizer(line, return_tensors="pt").to(model.device)
            output = model.generate(
                **input_ids,
                # max_new_tokens=100,
                num_beams=4,
                # early_stopping=True
            )
            output_string = (tokenizer.decode(output[0], skip_special_tokens=True))
            lemma, features, ref = test_file.readline().strip().split("\t")

            # evaluate
            if (ref == output_string):
                COUNTER += 1
                print(ref,output_string)
            else:
                print("ref:",ref,"pred:",output_string)
            
            # write
            out_file.write(lemma + "\t" +features+ "\t" + output_string + "\n")
            out_file.flush()

        accuracy = COUNTER / 1000
        out_file.write("accuracy:"+ str(accuracy))
        print(accuracy)
