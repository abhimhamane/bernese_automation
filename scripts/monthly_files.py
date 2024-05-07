#!/usr/bin/python3
# Script to automate downloading monthly data for Bernese from ftp site
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
from ftplib import FTP_TLS
from tqdm import tqdm

# AIUB FTP
#- P1C1XXXX.DCB, P1P2XXXX.DCB
#- Monthly files - P1C1 and P1P2


