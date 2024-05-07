#!/usr/bin/python3
# Script to automate downloading data from AIUB
# Author: Abhishek Mhamane, MS-R Geoinformatics
# Location: IIT Kanpur, India

import sys
import os
import re
from ftplib import FTP_TLS
from tqdm import tqdm

#- CLK, ERP, EPH, ION, P1C1XXXX.DCB, P1P2XXXX.DCB
#- Daily files - CLK, ERP, EPH and ION
#- Monthly files - P1C1 and P1P22
#- CRD, VEL, FIX, PSD from ../BSWUSER52/STA
#- SAT_xxxx.CRX from ../BSWUSER52/GEN