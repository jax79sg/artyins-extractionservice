#!/bin/bash
echo on
export TIKA_SERVER_JAR=/tmp/tika-server.jar
mkdir /tmp
if test -f "/tmp/tika-server.jar"; then
   echo "tika-server.jar exists"
else
   echo "tika-server.jar does not exists, downloading now"
   axel -n 5 -o /tmp/tika-server.jar  http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar
   axel -n 5 -o /tmp/tika-server.jar.md5 http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar.md5
fi
mkdir /mnt
mkdir /mnt/shareddata
cp test.pdf /mnt/shareddata
cp test2.pdf /mnt/shareddata
echo "Installing python requirements"
pip install -r requirements.txt
