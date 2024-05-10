# Bernese Automation Scripts

Python functions and scripts to automate data downloading for long-tern GNSS processing.

## Usage
- utils.py - deals with ftp server login 
- station_files.py - deals with downloading standard station files (CRD, VEL, FIX, PSD,SAT_xxxx.CRX)
- daily_files.py - deals with downloading files for clock, ephemerides, earth rotation params and ionosphere (CLK, ERP, EPH, ION)
- monthly_files.py - P1C1XXXX.DCB, P1P2XXXX.DCB
- igs_rinex.py - deals with downlaoding the raw rinex data of IGS stations from CDDIS and SOPAC ftp servers


## Author
Abhishek Mhamane, MS-R Geoinformatics, IIT Kanpur


## Other similar tools
1. Parallel.GAMIT - GAMIT Automation scripts in Python by Prof. Demián D. Gómez, The Ohio State University
