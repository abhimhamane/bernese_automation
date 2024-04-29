#!/usr/bin/python3

# Script to automate downloading the IGS site data from CDDIS Server
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India



import sys
import os
import re
from ftplib import FTP_TLS
from tqdm import tqdm

# inputa

def igs_cddis_single(year: int, doy: int, station: str, ftype: str, version: int, email: str, dest_folder: str):
    """Script to automate downloading IGS Site data from CDDIS server.
        Arguments-
            1. year - 4 digit (eg. 2020, 2011, 1999)
            2. doy - day of year (001 to 365)
            3. station - name of station (4 letter IGS site name)
            4. ftype - single letter file type (o, n, d, etc...)
            5. version - rinex version (2 or 3) (DEFAULT = 2)
            6. --help - to read the docstrigs

        Improvements Required
            - input handling
            - error handling 
                + for missing/unavailable data
                + login errors
                + invalid paths
            - progress bar
            - rinex version
    """
    os.chdir(dest_folder)
    # check inputs
    print(f"{year}, {doy}, {station}, {ftype}, {version}, {type(year)}")

    # 
    directory = f'gnss/data/daily/{year}/{doy}/{year[-2:]}{ftype}/'
    print(f"\n {directory} \n")
    ftps = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
    ftps.login(user='anonymous', passwd=email)
    ftps.prot_p()
    ftps.cwd(directory)

    lst = ftps.nlst()
    res = [x for x in lst if re.search(station, x)]
    print(res)
    if len(res) == 0:
        print(f"{station} - {year} - {doy} - not found")
        pass
    else:
        ftps.retrbinary("RETR " + res[0], open(res[0], 'wb').write)

def igs_cddis_multiple(years: list, doys: list, stations: list, ftype: str, version: int, email: str, dest_folder: str):
    
    os.chdir(dest_folder)
    
    for station in (stations):
        for year in tqdm(years):
            for doy in tqdm(doys):
                igs_cddis_single(year=year, doy=doy, station=station, ftype='o', version=2, 
                     email=email, dest_folder=dest_folder)
    