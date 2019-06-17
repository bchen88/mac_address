

GetMacAddress command to retrieve the company name along with the mac address from MAC address API

###Environment:

centOS 7.6 Python 2.7.5 docker 18.09.6

###Prerequisites:

You need to obtain your personal API key from the MAC address API website in order to be able to use the tool. Once you have it, you can pass it via --apikey argument.

###Usage:

Make sure firewalld is started.

First build docker images

docker build -t python-getmacaddress .

Show docker images you just build

docker images

###usage examples:

docker run --rm python-getmacaddress --search XX:XX:XX:XX:XX:XX --apikey xxxxxxxxxxxxxxxxxxx

