
import sys
import pathlib


def add_src2path():
    cur_work_dir = pathlib.Path(
        __file__).absolute().parent.parent
    cur_src_dir = cur_work_dir.joinpath("src")
    sys.path.insert(0, cur_src_dir.as_posix())
