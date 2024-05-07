#!/usr/bin/python3
# Script to automate downloading daily data for Bernese from ftp site
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
from ftplib import FTP_TLS
from tqdm import tqdm

# AIUB FTP
#- CLK, ERP, EPH, ION, 
#- Daily files - CLK, ERP, EPH and ION


