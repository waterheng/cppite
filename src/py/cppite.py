#!/usr/bin/env python
# -*- coding:utf-8 -*-

########################################################
# ITE command start with: #//
# ITE command keywords:quit,exit,byebye,bye, begin, end,
# verbose, concise, dump_project, dump_make_file, dump_cpp,
# dump_fragment,load_fragment
#
########################################################

import settings as st
from cpp_fragment_tmpl import hpp_tmpl, cpp_tmpl

class CppIte:
    def __init__(self):
        self.cpp_fragment = ""
        self.ite_cmd=""
        
    def is_cpp(self, ri):
        """ Test wether the raw input is c++ code fragment,
        or it is a ITE(interactive test environment) command
        """
        ri = ri.strip()
        if ri.startswith( "#//" ):
            self.ite_cmd = ri.strip("#//").upper()
            return False
        else:
            self.cpp_fragment=ri
            return True

    def compile_run(self):
        """ Compile the self.cpp_fragment(newest inputted) and run it"""
        print "Compile & run c++ code: {cpp}".format( cpp=self.cpp_fragment )

    def do_ite_cmd(self):
        """ Do the ITE command self.ite_cmd(newest inputted)"""
        print "Do c++ ITE command:{c}".format( c = self.ite_cmd )
        self.gen_cpp_code_file()
        
    def gen_cpp_code_file(self):
        hpp_code= hpp_tmpl.format( includes="#include <vector>" )
        cpp_code = cpp_tmpl.format( head_file=st.hpp_filename, tmp_cpp=self.cpp_fragment )
        with open( st.cpp_code_dir + st.hpp_filename, 'w') as hf:
            hf.write( hpp_code )
        with open( st.cpp_code_dir + st.cpp_filename, 'w') as cf:
            cf.write( cpp_code )