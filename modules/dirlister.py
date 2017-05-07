# -*- coding: utf-8 -*-
import os

def run(**aggs):
    
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return str(files)
