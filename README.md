# ssh-selector
Command line tool for quick selecting of ssh hosts.

During my time in work I found myself spending too much time on finding and writing ssh connection commands. 
With this simple tool you will be able to quickly type part of host name from configuration file and connect to server.

### How to use it

    sshs <part of host name>
    
Which might be something like:

    sshs some.name.com
    sshs some.
    sshs s 
    
If partial match is present in multiple hosts, you will be prompt to select one.

Listing all hosts:

    sshs list


### Requirements:
* python 3.5 or newer

### Installation
To install this tool just simple go to root directory of project and type:
    
    sudo pip3 install .

To uninstall just type:

    sudo pip3 uninstall ssh-selector

### TODO
* Handle exceptions and provide more meaningful messages.