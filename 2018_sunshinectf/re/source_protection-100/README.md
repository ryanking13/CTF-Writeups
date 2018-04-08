## Source Protection - 100

### Description

> People said I shouldn't use Python to write my password vault because they would be able to read my source code, but they underestimated how smart I am. In fact, I'm so confident in my source code protection that I'm going to upload my password vault and challeng a bunch of nerds to hack it. Good luck :)Author: hackucf_dmariapasswords.exe

### Write up

The Description says that exe file is generated from python.

```
$ strings passwords.exe -n 10 | grep Python
Py_SetPythonHome
Failed to get address for Py_SetPythonHome
Error loading Python DLL '%s'.
Error detected starting Python VM.
```

Yes it is.

There are two well known modules which convert python scripts to exe file; `py2exe` and `pyinstaller`.

I found a great tool -- [python-exe-unpacker](https://github.com/countercept/python-exe-unpacker) that unpacks both `py2exe`, `pyinstaller` generated exe binary.

By using that tool, pyc files and other resources are unpacked. By analysing those files, the flag can be obtained.
