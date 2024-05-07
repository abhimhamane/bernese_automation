#!/usr/bin/python3
# Script related to different ftp servers and logins
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
from ftplib import FTP_TLS, FTP
from tqdm import tqdm
from pathlib import Path

def login_cddis(username='', password=''):
    """_summary_

    Args:
        username (str, optional): _description_. Defaults to 'anonymous'.
        password (str, optional): _description_. Defaults to ''.

    Returns:
        _type_: _description_
    """

    try:
        ftps = FTP_TLS()
        ftps.connect('gdc.cddis.eosdis.nasa.gov')
        ftps.login(user=username, passwd=password)
        ftps.prot_p()
        print(ftps.welcome)
        return ftps


    except Exception as e:
        print("Error:", e)  # Catch-all for other issues
    
    
def login_sopac(username='anonymous', password='random@gmail.com'):
    """_summary_

    Args:
        username (str, optional): _description_. Defaults to ''.
        password (str, optional): _description_. Defaults to ''.

    Returns:
        _type_: _description_
    """
    try:
        ftps = FTP()
        ftps.connect('garner.ucsd.edu')
        ftps.login(user=username, passwd=password)
        print(ftps.welcome)
        return ftps

    except Exception as e:
        print("Error:", e)  # Catch-all for other issues


def login_aiub():
    """_summary_

    Returns:
        _type_: _description_
    """

    try:
        ftps = FTP()
        ftps.connect('ftp.aiub.unibe.ch')
        ftps.login()
        print(ftps.welcome)
        return ftps

    except Exception as e:
        print("Error:", e)  # Catch-all for other issues



def NOOPCHECK(ftp_connection):
    """The NOOP command does not cause the server to perform any action beyond 
    acknowledging the receipt of the command.

    Args:
        ftp_connection (_type_): _description_

    Returns:
        _type_: _description_
    """

    try:
        # Send the NOOP command
        response = ftp_connection.voidcmd("NOOP")
        print(response)
        return True  # If no exception, session is active

    except Exception as e:
        print("An error occurred:", e)  # Catch any other exceptions
        return False

def get_hash():
    
    raise NotImplementedError


def dir_exists(directory_path):

    path = Path(directory_path)
    if path.is_dir():
        print(f"The directory - {directory_path} exists")
        return True
    else:
        print(f"The directory - {directory_path} does not exist")
        return False

def download(session, fname, ftp_dir, download_dir):
    try:
        print(f"FTP Dir: {session.pwd()}, Local Dir: {os.getcwd()}")

        session.retrbinary("RETR " + fname, open(os.path.join(download_dir, fname), 'wb').write)

        return(f'{os.path.join(download_dir, fname)}')
    except Exception as e:
        print(f"Error occured, {e}")