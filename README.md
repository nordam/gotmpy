# gotmpy
Simple python interface to GOTM, to make a copy of a GOTM setup and modify parameters.

Usage:

```
from gotmpy import GOTMSettings
gotm = GOTMSettings(inputpath, outputpath, executablepath)
gotm['const_tx'] = 0.1
gotm.write()
gotm.run()
```

