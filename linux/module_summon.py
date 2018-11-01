#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import os

script_path_ = sys.argv[0]
module_name_ = sys.argv[1]
libs_=sys.argv[2:]
libs_str_=""
encoding_="utf-8"

for lib in libs_:
    libs_str_+=" "+lib

print("libs:" +libs_str_)

def create_dir(newdir):
    """works the way a good mkdir should :)
        - already exists, silently complete
        - regular file in the way, raise an exception
        - parent directory(ies) does not exist, make them as well
    """
    if os.path.isdir(newdir):
        pass
    elif os.path.isfile(newdir):
        raise OSError("a file with the same name as the desired " \
                      "dir, '%s', already exists." % newdir)
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            _mkdir(head)
        if tail:
            os.mkdir(newdir)

def gen_cmakelists_txt(module, libs):
    "generate CMakeLists.txt content"
    str="""aux_source_directory(. DIRSRCS)
add_library(%s ${DIRSRCS})
target_link_libraries(%s%s)
""" % (module, module, libs)
    return str

def write_str(filename, str):
    "create on !exist; truncate otherwise"
    with open(filename, 'w', encoding=encoding_) as fd:
        fd.write(str)
    return

def append_str(filename, str):
    "append write"
    with open(filename, 'a', encoding=encoding_) as fd:
        fd.write(str)
    return

append_str_="""
link_directories(./{module}/)
include_directories(./{module}/)
add_subdirectory({module})
""".format(module=module_name_)

create_dir(module_name_)
cmakelists_str=gen_cmakelists_txt(module_name_, libs_str_)
write_str("./"+module_name_+"/CMakeLists.txt", cmakelists_str)
append_str("./CMakeLists.txt", append_str_)

