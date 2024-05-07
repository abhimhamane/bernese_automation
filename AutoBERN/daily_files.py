#!/usr/bin/python3
# Script to automate downloading daily data for Bernese from ftp site
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
from ftplib import FTP_TLS
from tqdm import tqdm
import gpsdatetime as gpst

from AutoBERN.utils import download, login_aiub

# AIUB FTP
#- CLK, ERP, EPH, ION, 
#- Daily files - CLK, ERP, EPH and ION

def find_files(flist, gpsweek, dow, ftype):    
    try:
    # find files with given gps week
        gpsweek = str(gpsweek).zfill(4)
        res_gpsweek = [x for x in flist if re.search(f'{gpsweek}{dow}', x)]

        if res_gpsweek:
            # find the file type
            res_clk = [x for x in res_gpsweek if re.search(ftype, x)]
            return res_clk
        else:
            raise ValueError(f"File not found for GPS-Week={gpsweek} and dow={dow}")
    except:
        pass
    

def clk(download_dir, session, station, year, doy):
    FTP_DIR = '/CODE'
    FILE_FTP_DIR = f"{FTP_DIR}/{year}"
    session.cwd(FILE_FTP_DIR)

    fileslist = session.nlst()
    gpsweek = int(gpst.gpsdatetime(yyyy=year, doy=doy).wk)
    dow = int(gpst.gpsdatetime(yyyy=year, doy=doy).wd)

    datafiles = find_files(flist=fileslist, gpsweek=gpsweek, dow=dow, ftype='CLK')

    if len(datafiles) > 0:
        try:
            download(session=session, fname=datafiles[0], ftp_dir=FILE_FTP_DIR, download_dir=download_dir)
        except Exception as e:
            print(e)
    else:
        pass
    
def erp(download_dir, session, station, year, doy):
    FTP_DIR = '/CODE'
    FILE_FTP_DIR = f"{FTP_DIR}/{year}"
    session.cwd(FILE_FTP_DIR)

    fileslist = session.nlst()

    gpsweek = int(gpst.gpsdatetime(yyyy=year, doy=doy).wk)
    dow = int(gpst.gpsdatetime(yyyy=year, doy=doy).wd)

    datafiles = find_files(flist=fileslist, gpsweek=gpsweek, dow=dow, ftype='ERP')

    if len(datafiles) > 0:
        try:
            download(session=session, fname=datafiles[0], ftp_dir=FILE_FTP_DIR, download_dir=download_dir)
        except Exception as e:
            print(e)
    else:
        pass

def eph(download_dir, session, station, year, doy):
    FTP_DIR = '/CODE'
    FILE_FTP_DIR = f"{FTP_DIR}/{year}"
    session.cwd(FILE_FTP_DIR)

    fileslist = session.nlst()
    gpsweek = int(gpst.gpsdatetime(yyyy=year, doy=doy).wk)
    dow = int(gpst.gpsdatetime(yyyy=year, doy=doy).wd)

    datafiles = find_files(flist=fileslist, gpsweek=gpsweek, dow=dow, ftype='EPH')

    if len(datafiles) > 0:
        try:
            download(session=session, fname=datafiles[0], ftp_dir=FILE_FTP_DIR, download_dir=download_dir)
        except Exception as e:
            print(e)
    else:
        pass


def ion(download_dir, session, station, year, doy):
    FTP_DIR = '/CODE'
    FILE_FTP_DIR = f"{FTP_DIR}/{year}"
    session.cwd(FILE_FTP_DIR)

    fileslist = session.nlst()
    gpsweek = int(gpst.gpsdatetime(yyyy=year, doy=doy).wk)
    dow = int(gpst.gpsdatetime(yyyy=year, doy=doy).wd)

    datafiles = find_files(flist=fileslist, gpsweek=gpsweek, dow=dow, ftype='ION')

    if len(datafiles) > 0:
        try:
            download(session=session, fname=datafiles[0], ftp_dir=FILE_FTP_DIR, download_dir=download_dir)
        except Exception as e:
            print(e)
    else:
        pass

def bulk_daily_files(download_dir, session, station, start_year, start_doy, end_year, end_doy):  


    raise NotImplementedError
