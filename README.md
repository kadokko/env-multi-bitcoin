# Multiple Bitcoin Environment (regtest)


## Overview

This script easily builds two communicable bitcoin-core daemons. 

The daemons run in regtest mode. 

Also, they run as docker containers.

- OS: Ubuntu Bionic(18.04)
- Bitcoin Core: 0.18.1


## Requirement

- Vagrant ( 2.2.0 )
- VirtualBox ( 5.2.20 )


## Usage

* installation

```bash
$ git clone https://github.com/kadokko/env-multi-bitcoin.git
$ cd env-multi-bitcoin
$ vagrant up
$ vagrant ssh
$ cd /vagrant_share
$ ./start.sh
```

* bitcoin-cli

```bash
$ docker exec -it bitcoin1 /bin/bash
$ bitcoin-cli generate 3
$ exit

$ docker exec -it bitcoin2 /bin/bash
$ bitcoin-cli getblockcount
$ exit
```

* bitcoin rpc

```bash
$ curl --data-binary '{"jsonrpc": "1.0", "id":"rpc-test", "method": "getblockcount", "params": [] }' \
       -H 'content-type: text/plain;' http://user:password@localhost:18332/
$ curl --data-binary '{"jsonrpc": "1.0", "id":"rpc-test", "method": "getblockcount", "params": [] }' \
       -H 'content-type: text/plain;' http://user:password@localhost:19332/
```
