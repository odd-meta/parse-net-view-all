# parse-net-view-all

Parser for the raw output of the Windows "net view /all" command

I built this to throw together a list of hosts to feed into Invoke-MassMimikatz, but it may have some other useful purpose.

Functionally this script is examining the amount of spaces on the header line:
```
    Server Name            Remark
```
The number of spaces from the start of this line to "Remark" is the assumed maximum size of the computer name.

## TODO

rewrite in powershell
