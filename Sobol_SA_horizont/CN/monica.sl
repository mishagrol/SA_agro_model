#!/bin/bash
#rm *.csv
cat sobol_monica.py | tail -20 | head -15 > conditions.txt
touch sugar-beet-2011.csv spring-barley-2012.csv sugar-beet-2014.csv soybean-000-2015.csv sugar-beet-2017.csv
./sobol_monica.py > /dev/null
