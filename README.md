# Compiler for Multisig commands.

## Pre-Reqs

Experimental SmartPy :) 

```shell
sh <(curl -s https://smartpy.io/releases/20201226-dd504def6c81863a145679ba459652ed454a2b52/cli/install.sh) local-install ~/smartpy-cli
```

## Usage

```shell
$ ./compile-command.sh <id>
```

## Writing Commands

(1) Make a new command with a unique ID
```shell
mkdir commands/<id>
touch commands/<id>/command.py
```

(2) Write a command.

**NOTE: ** the function must be named `command`.

```python
import smartpy as sp

def command(self, unit):
  <commands here>
```

(3) Compile
```shell
compile-command.sh <id>
```

