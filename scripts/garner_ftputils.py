#!/usr/bin/python3
# Script to automate downloading data from GARNER(SOPAC) UCSD ftp site
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
from ftplib import FTP_TLS
from tqdm import tqdm

