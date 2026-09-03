lang = "klr"
PATH_NEURAL_BASELINE = f"../../neural-transducer/checkpoints/sig23/tagtransformer/{lang}.decode.test.tsv"
PATH_NONNEURAL_BASELINE = f"../../2023InflectionST/part1/data/{lang}.out"
path = PATH_NEURAL_BASELINE
ref_file_path = f"../..//2023InflectionST/part1/data/{lang}.tst"
output_file_path = f"{lang}_neural_baseline.errors"
with open(path,"r") as f, open(ref_file_path,"r") as ref_file, open (output_file_path,"w") as output_file, open(PATH_NONNEURAL_BASELINE,"r") as FILE_NONNEURAL_BASELINE:
    LINES_NEURAL = f.readlines()[1:]
    LINES_REF = ref_file.readlines()
    LINES_NONNEURAL_BASELINE = FILE_NONNEURAL_BASELINE.readlines()
    for pred_line_neural,ref_line,pred_line_nonneural in zip(LINES_NEURAL,LINES_REF,LINES_NONNEURAL_BASELINE):
        pred_line_neural,ref_line,pred_line_nonneural = pred_line_neural.strip(),ref_line.strip(),pred_line_nonneural.strip()
        error_detect = False

        # neural model mistakes
        if not pred_line_neural.endswith("0"):
            error_detect = True
            pred, ref = pred_line_neural.split("\t")[:2]
            lemma,rule = ref_line.split("\t")[:2]
            pred = "".join(pred.split())
            print(pred)
            output_file.write(f"{lemma}\t{rule}\t{pred}\n")

        # non-neural model mistakes
        if pred_line_nonneural != ref_line:
            error_detect = True
            output_file.write(pred_line_nonneural+"\n")
        
        # golden reference
        if error_detect:
            output_file.write(f"{ref_line}\n\n")
            # output_file.flush()
    
print(output_file_path)