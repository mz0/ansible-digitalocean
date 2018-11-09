I do not recommend the way I did that, it's all based on wrong premises, 
however that worked:)

```
$ pip3 install dopy==0.3.5

$ export PYTHONPATH=/usr/local/lib/python3.6/dist-packages

$ ls -l $PYTHONPATH/dopy*
/usr/local/lib/python3.6/dist-packages/dopy:
   68 __init__.py
18800 manager.py

/usr/local/lib/python3.6/dist-packages/dopy-0.3.5.dist-info:
 3743 DESCRIPTION.rst
    4 INSTALLER
 4057 METADATA
  571 metadata.json
   47 pbr.json
  877 RECORD
    5 top_level.txt
   93 WHEEL

```

*Note:* dopy PyPI points to older repo, 
the actual one is https://github.com/Wiredcraft/dopy
