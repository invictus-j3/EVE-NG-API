# EVE-NG API Class

_Note_: Active project. Documentation may not be complete.

The idea of this respository came from getting tired having to start the same lab everytime the EVE-NG server shutdown or reboot. The __startup_lab.py__ script needs to be set to run at boot.

## Variables

All environment variables are stored in the __environment.json__ file.

Rename __environment-default.json__ to __environment.json__.

Variable Details:

- __Server__
  - Replace _1.2.3.4_ with the IP address or host name of the target EVE-NG server
- __Credentials__
  - Contains the default EVE-NG username and password
  - Update accordingly
- __Lab__
  - Identifies the default lab. The lab will be affected if none is specified.
    - Name: The name of the lab, including the .unl extention.
    - Path: The lab folder path of the default lab.

## Start script at boot

Actively working to find the best way to have the startup script to run at boot, after EVE-NG starts.

Current effort is via rc.local

- Copy startup_lab.service to /etc/systemd/system/
- Run systemctl enable startup_lab.service
