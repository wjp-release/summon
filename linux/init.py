#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os, sys, stat

script_path_ = sys.argv[0]
project_name_ = sys.argv[1]
modules_=sys.argv[2:]
modules_str_=""
encoding_="utf-8"

for module_ in modules_:
    modules_str_+=" "+module_

print(project_name_+", submodules:" +modules_str_)


'''
initial project structure:

/project_root_dir
    Readme.md
    LISCENCE
    gitpush.sh
    include/
    src/
        internal.h                ## common header, optional
        compile.sh
        CMakeLists.txt
        build/
        cmakedir/                 ## cmake dir, optional
        module1/
            CMakeLists.txt
        module2/
            CMakeLists.txt
        module3/
            CMakeLists.txt
    doc/
    scripts/
    tests/
        module1/
        module2/
        module3/
'''


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

gitpush_str="""#!/bin/bash
git add .
git commit -m "w"
git push origin master
"""

write_str("gitpush.sh",gitpush_str)
os.chmod("./gitpush.sh", stat.S_IRWXG+stat.S_IRWXO+stat.S_IRWXU)

create_dir("src")
create_dir("src/build")
# create_dir("src/cmakedir")  # optional
create_dir("doc")
create_dir("scripts")
create_dir("tests")

for module_ in modules_:
    create_dir("./tests/"+module_)

def gen_cmakelists_txt(module, libs):
    "generate CMakeLists.txt content"
    str="""aux_source_directory(. DIRSRCS)
add_library(%s ${DIRSRCS})
target_link_libraries(%s%s)
""" % (module, module, libs)
    return str


def module_summon(module_name, libstr):
    append_str_="""
link_directories(./{module}/)
include_directories(./{module}/)
add_subdirectory({module})
""".format(module=module_name)
    create_dir(module_name)
    cmakelists_str=gen_cmakelists_txt(module_name, libstr)
    write_str("./"+module_name+"/CMakeLists.txt", cmakelists_str)
    append_str("./CMakeLists.txt", append_str_)
    return



# enter src
os.chdir("./src")

compile_str="""#!/bin/bash
cd build
rm -rf *
cmake -GNinja -DCMAKE_PREFIX_PATH=../cmakedir/ ..
ninja
"""

write_str("./compile.sh",compile_str)
os.chmod("./compile.sh", stat.S_IRWXG+stat.S_IRWXO+stat.S_IRWXU)

cmakelists_str="""cmake_minimum_required(VERSION 3.5)
project(%s)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "-fPIC")
set(CMAKE_C_FKAGS "-fPIC")
include_directories(/usr/local/include)
include_directories(./include)
include_directories(.)
link_directories(/usr/local/lib)
""" % (project_name_)
write_str("./CMakeLists.txt",cmakelists_str)

for module_ in modules_:
    module_summon(module_, "")
