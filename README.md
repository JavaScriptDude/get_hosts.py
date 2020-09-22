## get_hosts.py
Simple nmap scanner that enumerates hosts on a /24 network and returns IP, Mac and NIC vendor information as JSON

### Installation of dependencies
```python -m pip install python-nmap```

### Running on Linux:

Note: 
* Sudo is required by default. Therefore you must have a shell script as a shim to running Python.
* In my sample script, it assumes you are using pyenv. Alter the shell script as required for your env

``` sudo ./get_hosts.sh $HOME 3.7.7 192.168.101.0/24 ```

### Running on Windows:

```python get_hosts.py 192.168.101.0/24 ```
