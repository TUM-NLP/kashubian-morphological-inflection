langs = ["nav","sme","klr"]
for lang in langs:
    PATH_NONNEURAL_BASELINE = f"../../2023InflectionST/part1/data/{lang}.out"
    path = PATH_NONNEURAL_BASELINE
    path2 = f"../../2023InflectionST/part1/data/{lang}.tst"
    path_error = f"{lang}_nonneural_baseline.errors"
    with open(path,"r") as f, open(path2,"r") as g, open (path_error,"w") as h:
        lines_f = f.readlines()
        lines_g = g.readlines()
        for pred,ref in zip(lines_f,lines_g):
            if pred != ref:
                h.write(f"{pred.strip()}\n")
                h.write(f"{ref.strip()}\n\n")
                h.flush()
        