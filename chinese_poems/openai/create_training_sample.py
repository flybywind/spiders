import json
from random import sample

prompt_end = "\n\n###\n\n"
yiwen_compl = ['全诗大意', '全诗译文', '全诗解析']
poem_yiwen = ['该句大意', '该句译文', '该句解析']


def sample_one(ll):
    return sample(ll, 1)[0]


def create_fine_tune_samples(db_path, output_jsonl, offset=0, size=100):
    db = SqliteDB(db_path)
    rows = db.scan_db(
        f"id > {offset} and id < {offset+size} and length(poem) < 100 and length(yiwen) > length(poem)")
    if len(rows) == 0:
        print("WARN: no data!")
        return
    with open(output_jsonl, 'wt') as jsonl:
        for r in rows:
            poem_lines = r.poem.split("\n")
            poem_idx = range(len(poem_lines))
            yiwen_lines = r.yiwen.split("\n")
            if len(yiwen_lines) < len(poem_lines):
                print(f"WARN: {r} invalid, yiwen < poem lines")
                continue
            # template 1
            prompt = {
                'prompt': f"诗句:{sample_one(poem_lines)}的出处是什么？{prompt_end}",
                'completion': f"""您的诗句出自{r.author}所做的《{r.title}》，
    全诗如下：
    {r.poem}
    {sample_one(yiwen_compl)}：
    {r.yiwen}\n"""
            }
            jsonl.write(json.dumps(prompt))
            jsonl.write("\n")
            # template 2
            lidx = sample_one(poem_idx)
            prompt = {
                'prompt': f"解释诗句:{poem_lines[lidx]}{prompt_end}",
                'completion': f"""{sample_one(poem_yiwen)}: {yiwen_lines[lidx]}
    本诗是{r.author}所做的《{r.title}》的第{lidx}句，
    全诗如下：
    {r.poem}
    {sample_one(yiwen_compl)}：
    {r.yiwen}\n"""
            }
            jsonl.write(json.dumps(prompt))
            jsonl.write("\n")
            # template 3
            # todo: query davinci-3 to get the keywords of the poem
            # jsonl.write(json.dumps(prompt))
            # jsonl.write("\n")


if __name__ == "__main__":
    import pathlib
    import sys
    db_path = sys.argv[1]
    output_jsonl = sys.argv[2]
    offset = 0 if len(sys.argv) < 4 else int(sys.argv[3])
    size = 100 if len(sys.argv) < 5 else int(sys.argv[4])

    work_dir = pathlib.Path(__file__).parent.parent
    sys.path.insert(0, work_dir.as_posix())
    sys.path.insert(1, work_dir.joinpath("src").as_posix())
    from src.sqlite_dao import SqliteDB
    from src.conf import *

    create_fine_tune_samples(db_path, output_jsonl, offset, size)
