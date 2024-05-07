#!/usr/bin/python3
# Script to automate downloading IGS rinex files from relevant ftp site
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
from ftplib import FTP_TLS, FTP
from tqdm import tqdm
from scripts.utils import login_cddis, login_garner

# RINEX Files - daily and station dependent
#- ftp://garner.ucsd.edu/pub/rinex
#- https://cddis.nasa.gov/archive/gnss/



def login(server='cddis', username='', password=''):
    """_summary_

    Args:
        server (str, optional): _description_. Defaults to 'cddis'.
        username (str, optional): _description_. Defaults to ''.
        password (str, optional): _description_. Defaults to ''.
    """
    # check server
    if server.lower() == 'cddis':
        login_cddis()
    elif server.lower() == 'garner':
        login_garner()
    else:
        ValueError("Server Name not valid. cddis and garner servers supported.")

def bulk_download(start_year, start_doy, end_year, end_doy, server='cddis'):
    
    pass



def single_download():
    pass

def multiple_download():
    pass



