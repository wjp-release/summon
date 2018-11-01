#!/opt/local/bin/python3
# -*- coding: UTF-8 -*-

import sys

script_path_ = sys.argv[0]
classname_ = sys.argv[1]
encoding_ = 'utf-8'
namespace_ = 'hmq'
common_header_ = "internal.h"

print('class %s summoned in the name of %s in %s\n' % (classname_, namespace_, encoding_)) 

def gen_header_str(classname):
    "generate header content"
    str="""/*
 * MIT License
 * 
 * Copyright (c) 2018 jipeng wu
 * <recvfromsockaddr at gmail dot com>
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#pragma once

#include {header}

namespace {namespace}{{

class {foo}{{
public:
    {foo}();
    {foo}(const {foo} d) : meta(d.meta){{}}
    {foo}& operator= ({foo}&&d) noexcept : meta(d.meta){{
        meta.swap(d.meta);
        return *this;
    }}
    {foo}& operator= (const {foo}& d) noexcept{{
        meta=d.meta;
        return *this;
    }}
    bool operator== (const {foo}& d) noexcept{{
        return meta.get()==d.meta.get();
    }}
    bool operator!= (const {foo}& d) const noexcept{{
        return !(*this==d);
    }}

private:
    struct meta_t{{

    }};
    std::shared_ptr<meta_t> meta;
}};

}}

""".format(foo=classname, namespace=namespace_, header=common_header_)
    return str

def gen_cc_str(classname):
    "generate c++ file content"
    str="""/*
 * MIT License
 * 
 * Copyright (c) 2018 jipeng wu
 * <recvfromsockaddr at gmail dot com>
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#include "%s.h"

namespace %s{


}

""" % (classname, namespace_)
    return str

def write_str(filename, str):
    "create on !exist; truncate otherwise"
    with open(filename, 'w', encoding=encoding_) as fd:
        fd.write(str)
    return

def summon(classname):
    hstr=gen_header_str(classname)
    ccstr=gen_cc_str(classname)
    write_str("./"+classname+".cc", ccstr)
    write_str("./"+classname+".h", hstr)
    return

summon(classname_)