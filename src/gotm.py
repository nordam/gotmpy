#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GOTMSettings():
    def __init__(self, inputfolder, outputfolder, executable):
        self.inputfolder  = inputfolder
        self.outputfolder = outputfolder
        self.executable   = executable
        self.files = ['airsea', 'gotmmean', 'gotmrun', 'gotmturb', 'obs']
        self.read()

    def read(self):
        self.setup = {}
        for filename in self.files:
            self.setup[filename] = {}
            with open(os.path.join(self.inputfolder, filename) + '.nml') as f:
                for line in f:
                    if not line.strip().startswith('!'):
                        if line.strip().startswith('&'):
                            group = line.strip()
                            self.setup[filename][group] = {}
                        elif len(line.strip()) > 1:
                            key = line.split('=')[0].strip()
                            value = line.split('=')[1].replace(',', '').strip()
                            self.setup[filename][group][key] = value
                        else:
                            pass

    def write(self):
        for filename in self.files:
            with open(os.path.join(self.outputfolder, filename) + '.nml', 'w') as f:
                for group, groupdict in self.setup[filename].items():
                    f.write(group + '\n')
                    for key, value in groupdict.items():
                        f.write(key + ' = ' + value + ',\n')
                    f.write('/\n\n')

    def __getitem__(self, key):
        # Implementing __getitem__ to allow dictionary-like lookup
        # This is handled by searching all group dictionaries
        # until the desired key is found
        for filename in self.files:
            for group, groupdict in self.setup[filename].items():
                for k, v in groupdict.items():
                    if k == key:
                        return v
        raise KeyError('Key %s not found' % key)

    def __setitem__(self, key, value):
        # Implementing __getitem__ to allow dictionary-like lookup
        # This is handled by searching all group dictionaries
        # until the desired key is found
        # Note: This function does not allow creating a new key
        for filename in self.files:
            for group, groupdict in self.setup[filename].items():
                for k, v in groupdict.items():
                    if k == key:
                        self.setup[filename][group][key] = str(value)
                        return
        raise KeyError('Key %s not found' % key)

    def run(self):
        os.chdir(self.outputfolder)
        os.system(self.executable)
