#!/bin/bash
echo on
export TIKA_SERVER_JAR=$PWD/tika-server.jar
if test -f "tika-server.jar"; then
   echo "tika-server.jar exists"
else
   echo "tika-server.jar does not exists, downloading now"
   wget -O tika-server.jar http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar
fi
mkdir /tmp
cp tika-server.jar /tmp/
echo "Installing python requirements"
pip install -r requirements.txt
