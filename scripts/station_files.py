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
from scripts.utils import dir_exists, login_aiub, download

# AIUB FTP
#- CRD, VEL, FIX, PSD from ../BSWUSER52/STA
#- SAT_xxxx.CRX from ../BSWUSER52/GEN

def find_files(flist, extn):
    req_files = []
    for fle in flist:
        try:
            fname,fextn = fle.split('.')
            if fextn == extn:
                req_files.append(fle)
        except:
            pass
    return req_files


def crd(ftps, opt_dir: str):

    FTP_DIR = '/BSWUSER52/STA'

    ftps.cwd('/BSWUSER52/STA')
    files = ftps.nlst()
    crd_files = find_files(files, 'CRD')
    print(crd_files)
    time.sleep(1)
    try:
        fname = input("Enter the name of required CRD File: ")
        if fname in files:
            print(fname)
    
    except Exception as e:
        print(e)

    if dir_exists(opt_dir):
        download(session=ftps, fname=fname, ftp_dir=FTP_DIR, download_dir=opt_dir)
    else:
        raise ValueError("Download Folder does not exists")
    
     

def vel(ftps, opt_dir):
    FTP_DIR = '/BSWUSER52/STA'

    ftps.cwd('/BSWUSER52/STA')
    files = ftps.nlst()
    crd_files = find_files(files, 'VEL')
    print(crd_files)
    time.sleep(1)
    try:
        fname = input("Enter the name of required VEL File: ")
        if fname in files:
            print(fname)
    
    except Exception as e:
        print(e)

    if dir_exists(opt_dir):
        download(session=ftps, fname=fname, ftp_dir=FTP_DIR, download_dir=opt_dir)
    else:
        raise ValueError("Download Folder does not exists")

def fix(ftps, opt_dir):
    FTP_DIR = '/BSWUSER52/STA'

    ftps.cwd('/BSWUSER52/STA')
    files = ftps.nlst()
    crd_files = find_files(files, 'FIX')
    print(crd_files)
    time.sleep(1)
    try:
        fname = input("Enter the name of required FIX File: ")
        if fname in files:
            print(fname)
    
    except Exception as e:
        print(e)

    if dir_exists(opt_dir):
        download(session=ftps, fname=fname, ftp_dir=FTP_DIR, download_dir=opt_dir)
    else:
        raise ValueError("Download Folder does not exists")

def psd(ftps, opt_dir):
    FTP_DIR = '/BSWUSER52/STA'

    ftps.cwd('/BSWUSER52/STA')
    files = ftps.nlst()
    crd_files = find_files(files, 'PSD')
    print(crd_files)
    time.sleep(1)
    try:
        fname = input("Enter the name of required PSD File: ")
        if fname in files:
            print(fname)
    
    except Exception as e:
        print(e)

    if dir_exists(opt_dir):
        download(session=ftps, fname=fname, ftp_dir=FTP_DIR, download_dir=opt_dir)
    else:
        raise ValueError("Download Folder does not exists")

def sat(ftps, opt_dir):
    FTP_DIR = '/BSWUSER52/GEN'

    ftps.cwd('/BSWUSER52/GEN')
    files = ftps.nlst()
    crd_files = find_files(files, 'CRX')
    print(crd_files)
    time.sleep(1)
    try:
        fname = input("Enter the name of required SAT File: ")
        if fname in files:
            print(fname)
    
    except Exception as e:
        print(e)

    if dir_exists(opt_dir):
        download(session=ftps, fname=fname, ftp_dir=FTP_DIR, download_dir=opt_dir)
    else:
        raise ValueError("Download Folder does not exists")

