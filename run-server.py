import sys, os, logging
sys.path.append('./src')

logging.getLogger().setLevel(logging.DEBUG)
logging.debug('Initialization')

os.environ['PYRO_SERIALIZERS_ACCEPTED'] = 'marshal,json,serpent,pickle'
os.environ['PYRO_LOGLEVEL'] = 'DEBUG'

from server import start
start()