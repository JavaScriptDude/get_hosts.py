## get_hosts.py
Simple nmap scanner that enumerates hosts on a /24 network and returns IP, Mac and NIC vendor information as JSON

### Installation of dependencies
```
python -m pip install python-nmap
python -m pip install texttable
```

### Running on Linux:

Note: 
* Sudo is required by default. Therefore you must have a shell script as a shim to running Python.
* In my sample script, it assumes you are using pyenv. Alter the shell script as required for your env

``` sudo ./get_hosts.sh $HOME 3.7.7 192.168.101.0/24 ```

### Running on Windows:

```python get_hosts.py 192.168.101.0/24 ```

### Output:
```
      ip      |        mac        |                   vendor                 | status
==============+===================+==========================================+=======
192.168.10.4  | 48:80:88:4F:44:49 |                                  Notgear |     up
192.168.10.5  | G0:55:95:B4:85:54 |                                        - |     up
192.168.10.6  | 55:4B:G0:DD:E5:55 |                           Space Taxi Box |     up
192.168.10.7  | GB:G8:54:F4:44:55 |                            Blackberry 11 |     up
192.168.10.8  | 55:00:40:59:85:49 |                             Palm Pre 3.0 |     up
192.168.10.9  | 58:54:5B:54:99:D5 |                                        - |     up
192.168.10.10 | 40:F4:F4:54:G4:04 |                            Micro$quashed |     up
192.168.10.11 | 40:4D:0F:99:FG:FG |                         JSD Technologies |     up
192.168.10.12 | 88:DE:F5:0D:D9:F5 |                                  Coolbox |     up
192.168.10.13 |                 - |                                        - |     up
192.168.10.14 | 40:F4:F4:0E:F4:DG |                       Timex Sinclare 2.0 |     up
192.168.10.15 | F8:G8:5E:55:EE:98 |                       Timex Sinclare 2.1 |     up
```
