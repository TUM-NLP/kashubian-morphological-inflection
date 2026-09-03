TRAIN_FILEPATH = "../../2023InflectionST/part1/data/"
TEST_FILEPATH = "../../2023InflectionST/part1/data/"
EVAL_FILEPATH = "../../2023InflectionST/part1/data/"
LANGS = ["grc","dan","fra","sme","deu","nav","jap","klr","eng","mul","deu_eng"]+["ote","pol","mul_2","csb","amh"]
OUTPUT_TRAIN_FILEPATH = "data/"
OUTPUT_TEST_FILEPATH = "data/"  
OUTPUT_EVAL_FILEPATH = "data/"  

PREFIX = ""
def preprocess(x):
    x = x.strip()
    lemma, features, target = x.split("\t")
    prompt = "Inflect " + lemma + " using " + features
    target_string = target
    line = '{"input":"'+prompt+'","target":"'+target_string+'"}'
    return line


for lang in LANGS:
    print(lang)
    if lang == "csb":
        with open(TEST_FILEPATH + lang + ".tst","r") as test_file, open (OUTPUT_TEST_FILEPATH + lang + "_test.json", "w") as out_test_file:
            test_lines = test_file.readlines()
            test_json_lines = "\n".join(map(preprocess,test_lines))
            out_test_file.write(test_json_lines)
    else:
        with open(TRAIN_FILEPATH + lang + ".trn","r") as train_file, open(EVAL_FILEPATH + lang + ".dev","r") as eval_file, open(TEST_FILEPATH + lang + ".tst","r") as test_file, open (OUTPUT_TRAIN_FILEPATH + lang+ "_train.json","w") as out_train_file,  open (OUTPUT_EVAL_FILEPATH + lang+ "_eval.json","w") as out_eval_file, open (OUTPUT_TEST_FILEPATH + lang + "_test.json", "w") as out_test_file:
            train_lines = train_file.readlines()
            eval_lines = eval_file.readlines()
            test_lines = test_file.readlines()
            train_json_lines = "\n".join(map(preprocess,train_lines))
            test_json_lines = "\n".join(map(preprocess,test_lines))
            eval_json_lines = "\n".join(map(preprocess,eval_lines))
            out_train_file.write(train_json_lines)
            out_test_file.write(test_json_lines)
            out_eval_file.write(eval_json_lines)
