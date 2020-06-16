# scot-gov-featurecode-parser

Utility to parse csv files from statistics.gov.scot and add a new column with human readable official_name for each feature code.  Making the file easier to graph

Translating this
```
  FeatureCode        DateCode Measurement  Value  
0   S12000013  w/c 2020-02-10       Count      3  
1   S12000014  w/c 2020-02-10       Count     32  
2   S12000010  w/c 2020-02-10       Count     22  
3   S12000006  w/c 2020-02-10       Count     43  
4   S12000035  w/c 2020-02-10       Count     26  
```
into
```
  FeatureCode        DateCode Measurement  Value          official_name
0   S12000013  w/c 2020-02-10       Count      3     Na h-Eileanan Siar
1   S12000014  w/c 2020-02-10       Count     32                Falkirk
2   S12000010  w/c 2020-02-10       Count     22           East Lothian
3   S12000006  w/c 2020-02-10       Count     43  Dumfries and Galloway
4   S12000035  w/c 2020-02-10       Count     26        Argyll and Bute
```

## Installing
Util requires Python3 (most probably Python 3.6+, I developed on Python 3.8)

```python
python -m venv ./venv
./venv/Scripts/actvate
pip install -r requirements.txt

```

## Running
With your virtual environment running you can supply the name of the csv you want to download.  The csv MUST be in the same directory as the the python utility

```python
python gen_geo_names.py test.csv
```

Util will output a new .csv with the addtional column `test_geo_names.csv`