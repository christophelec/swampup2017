FROM jenkins:latest

COPY plugins.txt /tmp/plugins.txt
RUN /usr/local/bin/install-plugins.sh `cat /tmp/plugins.txt`
