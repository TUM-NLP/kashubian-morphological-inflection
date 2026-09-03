TRAIN_FILEPATH = "../../2023InflectionST/part1/data/"
TEST_FILEPATH = "../../2023InflectionST/part1/data/"
EVAL_FILEPATH = "../../2023InflectionST/part1/data/"
OUT_DIR = TRAIN_FILEPATH
LANGS = ["deu","eng"]
TARGET_LANG = "deu_eng"
LANGS = ["grc","dan","fra","sme","deu","nav","jap","klr","eng"]
TARGET_LANG = "mul"
LANGS = ["grc","dan","fra","sme","deu","nav","jap","klr","eng"]+["ote","pol","amh","csb"]
TARGET_LANG = "mul_2"
print(OUT_DIR)
with open (OUT_DIR + TARGET_LANG + ".trn","w") as out_train_file,  open (OUT_DIR + TARGET_LANG+ ".dev","w") as out_eval_file, open (OUT_DIR + TARGET_LANG + ".tst", "w") as out_test_file:
    for lang in LANGS:
        if lang == "csb":
            with open(TEST_FILEPATH + lang + ".tst","r") as test_file:
                out_test_file.write(test_file.read())
        else:
            with open(TRAIN_FILEPATH + lang + ".trn","r") as train_file, open(EVAL_FILEPATH + lang + ".dev","r") as eval_file, open(TEST_FILEPATH + lang + ".tst","r") as test_file:
                out_train_file.write(train_file.read())
                out_test_file.write(test_file.read())
                out_eval_file.write(eval_file.read())

