# EVE-NG API

_Note_: Active project. Documentation may not be complete.

The idea of this respository came from getting tired having to start the same lab everytime the EVE-NG server shutdown or reboot. . Cloning this repo to the EVE-NG server will allow the __startup_lab.py__ script to be ran after boot.

## Variables

Environment variables are stored in the __environment.json__ file.

Rename __environment-default.json__ to __environment.json__.

```sh
mv environment-default.json environment.json
```

### Variable Details

Edit the JSON file with your server and lab information.

- __Server__
  - Replace _1.2.3.4_ with the IP address or host name of the target EVE-NG server
- __Credentials__
  - Contains the default EVE-NG username and password
  - Update accordingly
- __Lab__
  - Identifies a default lab that can easily be called via the JSON file vs being hard coded into the script.
    - Name: The name of the lab, including the .unl extention.
    - Path: The lab folder path of the default lab.

## Start script at boot

The script __startup_lab.py__ is used to start one or more labs at boot. The current process uses _systemd_ to run the script as a process. The systemd file is set to wait for the _ua-timer.timer_ process to complete before starting. This seems to give EVE-NG enough time to finish so that the script can start the lab(s).

### Instructions for Setup

For the easiest setup, ssh with root and clone the repository. This will create a directory __/root/EVE-NG-API__.

You only need to update script's path in the __startup_lab.service__ if you clone to another location.

__Change__:

```sh
ExecStart=/usr/bin/python3 /root/EVE-NG-API/startup_lab.py
```

__To__:

```sh
ExecStart=/usr/bin/python3 <file_path>/startup_lab.py
```

Next move __startup_lab.service__ to the systemd directory and set it to start at boot.

```sh
mv startup_lab.service /etc/systemd/system

systemctl enable startup_lab.service
```

Verify the process works by manually starting the service and checkingg on the status. Note that the script has a 60 second hold timer to make sure that all other processes are up.

```sh
systemctl start startup_lab.service

systemctl status startup_lab.service
```
