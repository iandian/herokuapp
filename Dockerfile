#FROM debian:wheezy
FROM ubuntu
MAINTAINER Apex Yu <apex_yu@sohu.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -yq update && apt-get -yq upgrade
RUN apt-get -yq install python-software-properties \ 
                        software-properties-common \
                        build-essential \
                        curl \
                        python \
                        g++ \
                        make \
                        git \
                        ruby-full \
                        libfreetype6 
# Install pre-requisites
#RUN apt-get -y install python-software-properties git g++ libc-dev build-essential
#RUN apt-get -yq install python-software-properties software-properties-common \
#                     python g++ make git ruby-compass libfreetype6 libpng-dev adduser
# Install node.js, then npm install yo and the generators
RUN add-apt-repository -y ppa:chris-lea/node.js && \
    apt-get -yq update && \
    apt-get -yq install nodejs && \
    gem install sass compass && \ 
    npm install -g npm@2.11.3&& \
    npm install -g n && \
    n v0.12.7 && \
    npm cache clean && \
    npm install -g yo@1.4.7 bower@1.4.1 grunt-cli && \
    npm install -g generator-webapp generator-angular-bootstrap@0.4.3 && \
    npm cache clean
# Add an xroot user because grunt doesn't like being root
RUN adduser --disabled-password --gecos "" xroot && \
  echo "xroot ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

#RUN apt-get -yq remove adduser
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose the port
EXPOSE 3000 9000

# set HOME so 'npm install' and 'bower install' don't write to /
ENV HOME /home/xroot

ENV LANG en_US.UTF-8

RUN mkdir /src && chown xroot:xroot /src
WORKDIR /src

# Always run as the xroot user
USER xroot

RUN git config --global url."https://".insteadOf git://

# Set aliases
RUN echo "alias ls='ls --color=auto'" >> /home/xroot/.bashrc
RUN echo "alias ll='ls --color=auto -l'" >> /home/xroot/.bashrc
RUN echo "alias l='ls --color=auto -lA'" >> /home/xroot/.bashrc
RUN echo "alias c='clear'" >> /home/xroot/.bashrc

CMD /bin/bash


