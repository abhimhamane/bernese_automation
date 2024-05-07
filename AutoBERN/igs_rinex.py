#!/usr/bin/python3
# Script to automate downloading IGS rinex files from relevant ftp site
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
import numpy as np
from ftplib import FTP_TLS, FTP
from tqdm import tqdm
from AutoBERN.utils import login_cddis, login_sopac, download

# RINEX Files - daily and station dependent
#- ftp://garner.ucsd.edu/pub/rinex
#- https://cddis.nasa.gov/archive/gnss/


def find_station(fileslist, stn_code):

    try:
        # version 2 file
        res2 = [x for x in fileslist if re.search(stn_code.lower(), x)]

        # version 3 file
        res3 = [x for x in fileslist if re.search(stn_code.upper(), x)]
        
        return res2 + res3
    except Exception as e:
        print(e)


def sopac_rinex(download_dir, session, station, year, doy):
    FTP_ROOT = '/pub/rinex'
    doy = str(doy).zfill(3)
    FILE_FTP_DIR = f'{FTP_ROOT}/{year}/{doy}'
    
    session.cwd(FILE_FTP_DIR)
    all_stations = session.nlst()
    datafiles = find_station(all_stations, stn_code=station)

    if len(datafiles) > 0:
        try:
            download(session=session, fname=datafiles[0], ftp_dir=FILE_FTP_DIR, download_dir=download_dir)
        except Exception as e:
            print(e)

    elif len(datafiles) == 0:
        raise ValueError(f"Station code - {station} data for {year} and day {doy} Not Found")
    

def sopac_bulk_download(download_dir, station, start_year, start_doy, end_year, end_doy):
    sopac = login_sopac()

    if start_year == end_year:
        doys = np.arange(start_doy, end_doy+1, 1)
        for _doy in tqdm(doys):
            try:
                sopac_rinex(download_dir=download_dir, session=sopac, station=station, year=start_year, doy=_doy)
            except ValueError as e:
                print(f"File Not Found - {station} data for {start_year} and day {_doy} - skipping!")

    elif start_year > end_year:
        raise ValueError("Invalid Input: end year should be higher than starting year")
    
    else:
        years = np.arange(start_year, end_year+1, 1)
        for yr in tqdm(years):
            if yr == start_year:
                doys = np.arange(start_doy, 366+1, 1)
                for _doy in tqdm(doys):
                    try:
                        sopac_rinex(download_dir=download_dir, session=sopac, station=station, year=start_year, doy=_doy)
                    except ValueError as e:
                        print(f"File Not Found - {station} data for {start_year} and day {_doy} - skipping!")


            if yr > start_year and yr < end_year:
                doys = np.arange(1, 366+1, 1)
                for _doy in tqdm(doys):
                    try:
                        sopac_rinex(download_dir=download_dir, session=sopac, station=station, year=start_year, doy=_doy)
                    except ValueError as e:
                        print(f"File Not Found - {station} data for {start_year} and day {_doy} - skipping!")

            if yr == end_year:
                doys = np.arange(1, end_doy+1, 1)
                for _doy in tqdm(doys):
                    try:
                        sopac_rinex(download_dir=download_dir, session=sopac, station=station, year=start_year, doy=_doy)
                    except ValueError as e:
                        print(f"File Not Found - {station} data for {start_year} and day {_doy} - skipping!")



