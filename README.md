# summon
python scripts for file/dir generation in cpp cmake projects

> summon.py <classname>
    create .cc and .h files for specified class, which initially include copy right info, the liscence, a common header, #pragma once, namespace and empty class structures

> valuesemantic_summon.py <classname>
    special summon script for 'valuesemantic' classes

> module_summon.py <modulename>
    create a folder named after this module, its CMakeList.txt and then update CMakeList.txt in current dir to include this submodule
