# coding=utf-8

####################################
# Please don't remove my credit :) #
####################################
# Copyright (C) 2018 Alex Gompper  #
#        agompper@gmail.com        #
#    https://github.com/alxgmpr    #
####################################

import sys
import os
import threading
import select
from time import sleep
from datetime import datetime

import urllib3
import requests
import paramiko
import linode

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def log(text):
    print '[{}] :: {}'.format(datetime.strftime(datetime.now(), '%H:%M:%S'), text)


class PyNode(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.is_user_pass = False
        self.is_ip_addr = False

        self.username = ''
        self.password = ''

        self.ip_addr = ''

        self.server_ip_addr = ''
        self.server_pw = ''

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        log('Importing Linode API key from apikey.txt')
        try:
            with open('apikey.txt') as api_key_file:
                self.api_key = api_key_file.read()
                if self.api_key in {None, ''}:
                    log('[error] Blank api key')
                    sys.exit(-1)
        except IOError:
            log('[error] Unable to locate apikey.txt')
            sys.exit(-1)

    def configure(self):

        while True:
            log('Awaiting config\n\nMenu:\n(0) - Username/password\n(1) - IP address\nPlease enter your selection:')
            try:
                selection = int(raw_input('> '))
                print
            except TypeError:
                log('[error] Please enter 0 or 1')
            if selection in {0, 1}:
                break
            else:
                log('[error] Please enter 0 or 1')

        if selection == 0:
            self.is_ip_addr = False
            self.is_user_pass = True
            while True:
                log('Awaiting config\n\nEnter username and password in format USERNAME:PASSWORD')
                user_pass = raw_input('> ')
                print
                if ':' in user_pass:
                    break
                else:
                    log('[error] Please enter in format USERNAME:PASSWORD')
            self.username = user_pass.split(':')[0]
            self.password = user_pass.split(':')[1]
            return True
        else:
            self.is_ip_addr = True
            self.is_user_pass = False
            while True:
                log('Awaiting config\n\nMenu:\n(0) - Fetch IP automatically\n(1) - Enter IPv4 manually\nPlease enter your selection:')
                try:
                    selection = int(raw_input('> '))
                    print
                except TypeError:
                    log('[error] Please enter 0 or 1')
                if selection in {0, 1}:
                    break
                else:
                    log('[error] Please enter 0 or 1')
            if selection == 0:
                log('Retrieving local IPv4 address')
                try:
                    r = requests.get(
                        url='https://httpbin.org/ip',
                        verify=False,
                        allow_redirects=False,
                        timeout=5
                    )
                    r.raise_for_status()
                except (requests.exceptions.HTTPError, requests.exceptions.Timeout):
                    log('[error] Failed to retrieve local IPv4 address')
                    sys.exit(-1)
                j = r.json()
                try:
                    self.ip_addr = j['origin']
                except KeyError:
                    log('[error] Couldnt find IPv4 address in response')
                    sys.exit(-1)
            else:
                log('Please enter the IPv4 address you would like the proxies tied to:')
                self.ip_addr = raw_input('> ')
                print
            if len(self.ip_addr.split(':')) > 1:
                log('[error] Got IPv6 address instead of IPv4')
                sys.exit(-1)
            else:
                log('Proxies will be tied to {}'.format(self.ip_addr))
                return True

    def generate_linode(self):
        client = linode.LinodeClient(self.api_key)
        region = client.get_regions()[3]
        log('Selected region {}'.format(region.id))
        image = client.get_images()[-2]
        log('Selected image {}'.format(image.id))
        ltype = client.linode.get_types()[8]
        log('Selected type {}'.format(ltype.id))

        log('Creating VPS')
        try:
            l, pw = client.linode.create_instance(ltype, region, image)
        except linode.ApiError:
            log('[error] Invalid API key. Refer to readme')
            sys.exit(-1)
        log('VPS Credentials: \n\nUsername: root\nPassword: {}\n'.format(pw))
        log('Booting VPS')
        log('Server IP: ' + str(l.ipv4[0]))
        self.server_ip_addr = str(l.ipv4[0])
        self.server_pw = pw

    def build_commands(self):
        command_template = """
#!/bin/bash
#
# Ubuntu 14 LTS
#

set -v

apt-get -y update

apt-get install -y ntpdate
apt-get install -y squid3 apache2-utils

cp /etc/squid/squid.conf /etc/squid/squid.conf.bak

cat << EOF > /etc/squid/squid.conf
http_port 8000
http_port 8001
http_port 8002
http_port 8003
http_port 8004
http_port 8005
http_port 8006
http_port 8007
http_port 8008
http_port 8009
http_port 8010
http_port 8011
http_port 8012
http_port 8013
http_port 8014
http_port 8015
http_port 8016
http_port 8017
http_port 8018
http_port 8019
http_port 8020
http_port 8021
http_port 8022
http_port 8023
http_port 8024
http_port 8025
http_port 8026
http_port 8027
http_port 8028
http_port 8029
http_port 8030
http_port 8031
http_port 8032
http_port 8033
http_port 8034
http_port 8035
http_port 8036
http_port 8037
http_port 8038
http_port 8039
http_port 8040
http_port 8041
http_port 8042
http_port 8043
http_port 8044
http_port 8045
http_port 8046
http_port 8047
http_port 8048
http_port 8049
http_port 8050
http_port 8051
http_port 8052
http_port 8053
http_port 8054
http_port 8055
http_port 8056
http_port 8057
http_port 8058
http_port 8059
http_port 8060
http_port 8061
http_port 8062
http_port 8063
http_port 8064
http_port 8065
http_port 8066
http_port 8067
http_port 8068
http_port 8069
http_port 8070
http_port 8071
http_port 8072
http_port 8073
http_port 8074
http_port 8075
http_port 8076
http_port 8077
http_port 8078
http_port 8079
http_port 8080
http_port 8081
http_port 8082
http_port 8083
http_port 8084
http_port 8085
http_port 8086
http_port 8087
http_port 8088
http_port 8089
http_port 8090
http_port 8091
http_port 8092
http_port 8093
http_port 8094
http_port 8095
http_port 8096
http_port 8097
http_port 8098
http_port 8099
http_port 8100
http_port 8101
http_port 8102
http_port 8103
http_port 8104
http_port 8105
http_port 8106
http_port 8107
http_port 8108
http_port 8109
http_port 8110
http_port 8111
http_port 8112
http_port 8113
http_port 8114
http_port 8115
http_port 8116
http_port 8117
http_port 8118
http_port 8119
http_port 8120
http_port 8121
http_port 8122
http_port 8123
http_port 8124
http_port 8125
http_port 8126
http_port 8127
{}
http_access allow ncsa_users
cache deny all
forwarded_for delete
request_header_access Via deny all
request_header_access Allow allow all
request_header_access Authorization allow all
request_header_access WWW-Authenticate allow all
request_header_access Proxy-Authorization allow all
request_header_access Proxy-Authenticate allow all
request_header_access Cache-Control allow all
request_header_access Content-Encoding allow all
request_header_access Content-Length allow all
request_header_access Content-Type allow all
request_header_access Date allow all
request_header_access Expires allow all
request_header_access Host allow all
request_header_access If-Modified-Since allow all
request_header_access Last-Modified allow all
request_header_access Location allow all
request_header_access Pragma allow all
request_header_access Accept allow all
request_header_access Accept-Charset allow all
request_header_access Accept-Encoding allow all
request_header_access Accept-Language allow all
request_header_access Content-Language allow all
request_header_access Mime-Version allow all
request_header_access Retry-After allow all
request_header_access Title allow all
request_header_access Connection allow all
request_header_access Proxy-Connection allow all
request_header_access User-Agent allow all
request_header_access Cookie allow all
request_header_access All deny all
always_direct deny all
EOF

{}

service squid restart
        """
        if self.is_user_pass:
            config_snippet = """auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/squid_passwd
acl ncsa_users proxy_auth REQUIRED"""

            end_snippet = """sudo touch /etc/squid/squid_passwd
sudo chown proxy /etc/squid/squid_passwd

sudo htpasswd -b /etc/squid/squid_passwd {} {} """.format(self.username, self.password)

            return command_template.format(config_snippet, end_snippet)
        elif self.is_ip_addr:
            config_snippet = """acl ncsa_users src {}""".format(self.ip_addr)
            return command_template.format(config_snippet, '')

    def connect(self):
        while True:
            try:
                log('Trying to connect to server')
                self.ssh.connect(self.server_ip_addr, port=22, username='root', password=self.server_pw, timeout=5)
                log('Connected to server')
                break
            except (paramiko.AuthenticationException, Exception):
                log('Couldnt connect to host yet. Its probably not started yet. Will retry')
                sleep(5)
        return True

    def execute(self):
        log('Sending commands to enable proxies')
        stdin, stdout, stderr = self.ssh.exec_command(self.build_commands())
        log('Commands sent, awaiting response and completion\n\n')
        # Wait for the command to terminate
        while not stdout.channel.exit_status_ready():
            # Only print data if there is data to read in the channel
            if stdout.channel.recv_ready():
                rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
                if len(rl) > 0:
                    # Print data from stdout
                    print stdout.channel.recv(1024),
        self.ssh.close()
        log('\nSSH Tunnel complete and connection closed')
        return True

    def write_file(self):
        log('Writing proxies to file')
        print
        i = 0
        filename = 'proxies-{}.txt'.format(i)
        while filename in os.listdir('/'):
            i += 1
        log('Proxies will be saved in {}'.format(filename))
        with open(filename, 'w') as proxyfile:
            if self.is_ip_addr:
                for j in range(8000, 8050):
                    proxyfile.write('{}:{}\n'.format(self.server_ip_addr, j))
            elif self.is_user_pass:
                for j in range(8000, 8050):
                    proxyfile.write('{}:{}:{}:{}\n'.format(self.server_ip_addr, j, self.username, self.password))
        log('Proxies successfully written to file')

    def run(self):
        while True:
            log('How many servers would you like to create (50 proxies per server)?')
            log('Different configuration can be used for each server\n')
            try:
                server_qty = int(raw_input('> '))
            except TypeError:
                log('[error] Please enter a number between 1 and 20')
            if (server_qty < 1) or (server_qty > 20):
                log('[error] Please enter a number between 1 and 20')
            else:
                break
        for i in range(server_qty):
            self.generate_linode()
            self.configure()
            self.connect()
            self.execute()
            self.write_file()


def main():
    pynode = PyNode()
    pynode.start()

if __name__ == '__main__':
    main()
