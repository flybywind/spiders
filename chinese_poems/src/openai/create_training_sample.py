from itertools import chain
import json
from random import sample
import regex

prompt_end = "\n\n###\n\n"
prompt_end_len = len(prompt_end)
chi_seg = regex.compile("？|！|。")
yiwen_compl = ['全诗大意', '全诗译文', '全诗解析']
# poem_yiwen = ['该句大意', '该句译文', '该句解析']
famous_author = [
    '李白〔唐代〕',
    '苏轼〔宋代〕',
    '杜甫〔唐代〕',
    '纳兰性德〔清代〕',
    '李商隐〔唐代〕',
    '白居易〔唐代〕',
    '陆游〔宋代〕',
    '王维〔唐代〕',
    '辛弃疾〔宋代〕',
    '温庭筠〔唐代〕',
    '李贺〔唐代〕',
    '刘禹锡〔唐代〕',
    '杜牧〔唐代〕',
    '欧阳修〔宋代〕',
    '王安石〔宋代〕',
    '元好问〔金朝〕',
    '孟浩然〔唐代〕',
    '吴文英〔宋代〕',
    '岑参〔唐代〕',
    '晏几道〔宋代〕',
    '柳宗元〔唐代〕',
    '陶渊明〔魏晋〕',
    '李煜〔五代〕',
    '杨万里〔宋代〕',
    '李清照〔宋代〕',
    '黄庭坚〔宋代〕',
    '韦庄〔唐代〕',
    '秦观〔宋代〕',
    '范成大〔宋代〕',
    '韦应物〔唐代〕',
    '毛泽东〔近现代〕',
    '柳永〔宋代〕',
    '王昌龄〔唐代〕',
    '刘长卿〔唐代〕',
    '晏殊〔宋代〕',
    '曹雪芹〔清代〕',
    '韩愈〔唐代〕',
    '张可久〔元代〕',
    '王国维〔近现代〕',
    '贺铸〔宋代〕',
    '元稹〔唐代〕',
    '周邦彦〔宋代〕',
    '王建〔唐代〕',
    '陈子昂〔唐代〕',
    '冯延巳〔五代〕',
    '贾岛〔唐代〕',
    '陈与义〔宋代〕',
    '高适〔唐代〕',
    '王勃〔唐代〕',
    '孙光宪〔五代〕',
    '姜夔〔宋代〕',
    '张籍〔唐代〕',
    '乔吉〔元代〕',
    '杜荀鹤〔唐代〕',
    '马致远〔元代〕',
    '曹植〔两汉〕',
    '朱淑真〔宋代〕',
    '李珣〔五代〕',
    '李益〔唐代〕',
    '罗隐〔唐代〕',
    '张先〔宋代〕',
    '孟郊〔唐代〕',
    '欧阳炯〔五代〕',
    '袁枚〔清代〕',
    '刘克庄〔宋代〕',
    '张祜〔唐代〕',
    '毛文锡〔五代〕',
    '沈约〔南北朝〕',
    '谢朓〔南北朝〕',
    '郑燮〔清代〕',
    '陈师道〔宋代〕',
    '顾敻〔五代〕',
    '和凝〔五代〕',
    '白朴〔元代〕',
    '钱起〔唐代〕',
    '卢挚〔元代〕',
    '唐寅〔明代〕',
    '张九龄〔唐代〕',
    '张孝祥〔宋代〕',
    '张泌〔唐代〕',
    '戴叔伦〔唐代〕',
    '梅尧臣〔宋代〕',
    '陆龟蒙〔唐代〕',
    '陈子龙〔明代〕',
    '鲁迅〔近现代〕',
    '黄景仁〔清代〕',
    '于谦〔明代〕',
    '吴均〔南北朝〕',
    '张养浩〔元代〕',
    '徐再思〔元代〕',
    '戴复古〔宋代〕',
    '李世民〔唐代〕',
    '汪遵〔唐代〕',
    '王士祯〔清代〕',
    '王守仁〔明代〕',
    '许浑〔唐代〕',
    '雍陶〔唐代〕',
    '韩偓〔唐代〕',
]


def sample_one(ll):
    return sample(ll, 1)[0]


def get_poem_type(title, poem_lines):
    seg = title.split("·")
    if len(seg) == 2:
        return seg[0]

    def _length_type(seg, type):
        if len(seg[0]) == 5:
            return "五言"+type
        elif len(seg[0]) == 7:
            return "七言"+type
        return ""

    n = len(poem_lines)
    seg = poem_lines[0].split("，")
    if n == 2:
        return _length_type(seg, "绝句")
    if n == 4:
        return _length_type(seg, "律诗")
    if n > 4:
        return _length_type(seg, "古诗")
    return ""


def ft_samples(obj, file, vendor="openai"):
    if vendor == 'openai':
        file.write(json.dumps(obj, ensure_ascii=False))
        file.write("\n")
    elif vendor == 'cohere':
        file.write(f"question:{obj['prompt'][:-prompt_end_len]}\n")
        file.write(f"answer:{obj['completion']}\n")
        file.write(prompt_end)


def create_fine_tune_samples(db_path, output_jsonl, vendor, offset=0, size=100):
    db = SqliteDB(db_path)
    famous_author_list = "'" + "', '".join(famous_author) + "'"
    rows = db.scan_db(
        f"id > {offset} and id < {offset+size} and length(poem) < 100 and length(yiwen) > length(poem) and author in ({famous_author_list})")
    if len(rows) == 0:
        print("WARN: no data!")
        return
    with open(output_jsonl, 'wt') as jsonl:
        for r in rows:
            poem_lines = r.poem.split("\n")
            yiwen_lines = r.yiwen.split("\n")
            if len(yiwen_lines) < len(poem_lines):
                print(f"WARN: {r} invalid, yiwen < poem lines")
                continue
            yiwen_lines_clean = "\n".join(yiwen_lines[:-1])
            # template 1
            prompt = {
                'prompt': f"诗句:\n{r.poem}\n出处是哪里？{prompt_end}",
                'completion': f""" 您的诗句出自{r.author}所做的《{r.title}》\n"""
            }
            ft_samples(prompt, jsonl, vendor)
            # template 2
            prompt = {
                'prompt': f"解释诗句:\n{r.poem}\n意思是什么{prompt_end}",
                'completion': f""" 本诗是{r.author}所做的《{r.title}》，
    {sample_one(yiwen_compl)}：
    {r.yiwen.strip()}\n"""
            }
            ft_samples(prompt, jsonl, vendor)
            # template 3
            poem_type = get_poem_type(r.title, poem_lines)
            poem_line_num = len(poem_lines)
            yiwen_lines2 = [
                x for x in chain.from_iterable(
                    [chi_seg.split(x) for x in yiwen_lines])
                if len(x) > 5][:poem_line_num]
            one_yiwen = sample_one(yiwen_lines2)
            seg_comma = one_yiwen.split("，")
            if len(seg_comma) > 4:
                one_yiwen = "，".join(seg_comma[:4])
            prompt = {
                'prompt': f"请根据提示作一首{poem_type}：\n{one_yiwen}{prompt_end}",
                'completion': f" 《{poem_type}》:\n{r.poem}\n"
            }
            ft_samples(prompt, jsonl, vendor)
            # template 4
            # todo: query davinci-3 to get the keywords of the poem
            # jsonl.write(json.dumps(prompt))
            # jsonl.write("\n")


if __name__ == "__main__":
    import pathlib
    import sys
    db_path = sys.argv[1]
    output_jsonl = sys.argv[2]
    vendor = sys.argv[3]
    offset = 0 if len(sys.argv) < 5 else int(sys.argv[4])
    size = 100 if len(sys.argv) < 6 else int(sys.argv[5])

    work_dir = pathlib.Path(__file__).parent.parent
    sys.path.insert(0, work_dir.as_posix())
    sys.path.insert(0, work_dir.parent.as_posix())
    from src.sqlite_dao import SqliteDB
    from src.conf import *

    create_fine_tune_samples(db_path, output_jsonl, vendor, offset, size)
