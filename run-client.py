import sys, logging
sys.path.append('./src')

logging.getLogger().setLevel(logging.DEBUG)

import argparse
parser = argparse.ArgumentParser(description='Pyro client demo, calls one method')
parser.add_argument('-H', '--hostname', action="store", help='Hostname of Pyro name server (i.e. ipnb2.solab.rshu.ru)', required=True)
options = parser.parse_args()

from client import init, execute_method

init(options.hostname)
execute_method()