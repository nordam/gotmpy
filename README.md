# gotmpy

Simple python interface to GOTM, to make a copy of a GOTM setup and modify parameters. Given an input folder which contains a complete GOTM setup, it can read that setup, modify any parameter, and then write the modified setup to an output folder, and run GOTM in that folder.

Usage:

```
from gotmpy import GOTMSettings
gotm = GOTMSettings(inputpath, outputpath, executablepath)
gotm['const_tx'] = 0.1
gotm.write()
gotm.run()
```

