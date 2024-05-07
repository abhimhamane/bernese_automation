#!/usr/bin/python3
# Script to automate downloading standard station files from relevant ftp site
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
import time
from ftplib import FTP_TLS
from tqdm import tqdm
from scripts.utils import dir_exists, login_aiub

# AIUB FTP
#- CRD, VEL, FIX, PSD from ../BSWUSER52/STA
#- SAT_xxxx.CRX from ../BSWUSER52/GEN



def crd(opt_dir: str):

    ftps = login_aiub()
    ftps.cwd('BSWUSER52/STA')
    files = ftps.nlst()
    print(files)
    time.sleep(1)
    try:
    
        fname = input("Enter the fname: ")
        if fname in files:
            return(fname)
    
    except Exception as e:
        print(e)



    if dir_exists(opt_dir):
        pass
    pass

def vel(ftps, opt_dir):
    pass

def fix(ftps, opt_dir):
    pass

def psd(ftps, opt_dir):
    pass

def sat(ftps, opt_dir):
    pass

