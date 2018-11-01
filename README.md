# summon
generate project structure, submodule and new files for cmake projects

## summon.py <classname>
    creates .cc and .h files for specified class, which initially include copy right info, the liscence, a common header, #pragma once, namespace and empty class structures

## valuesemantic_summon.py <classname>
    summon special 'valuesemantic' classes

## module_summon.py <modulename>
    create a folder named after this module, its CMakeList.txt and then update CMakeList.txt in current dir to include this submodule

## init.py <projectname> <submodule1> <submodule2> <submodule3>
    init a c++ cmake project in its root directory