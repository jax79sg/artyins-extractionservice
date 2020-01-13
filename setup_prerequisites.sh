#!/bin/bash
echo on
export TIKA_SERVER_JAR=/tmp/tika-server.jar
mkdir /tmp
rm -r /tmp/tika*
axel -n 5 -o /tmp/tika-server.jar  http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar
axel -n 5 -o /tmp/tika-server.jar.md5 http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar.md5
mkdir /mnt
mkdir /mnt/shareddata
cp test.pdf /mnt/shareddata
cp test2.pdf /mnt/shareddata
echo "Installing python requirements"
pip install -r requirements.txt
