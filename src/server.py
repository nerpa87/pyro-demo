import Pyro4
import numpy as np
import logging
from random import random, randint

Pyro4.config.SERIALIZER='pickle'

@Pyro4.expose
class DataFetcher(object):
  def __init__(self):
    logging.debug('DataFetcher class created')
  def getValues(self, filename, extent=None, resolution=None, variables=[]):
    w = randint(4, 8)
    h = randint(2, 5)
    raw = np.ndarray(shape=(w*h, 1), dtype=float)
    for x in raw:
      x[...] = 10*random() - 5
    res = raw.reshape(w,h)
    logging.debug("filename %s, extent %s, resolution %s, variables %s" % (filename, extent, resolution, variables))
    logging.debug("result %s" % res)
    return res

def start():
  daemon = Pyro4.Daemon()
  uri = daemon.register(DataFetcher)
  ns = Pyro4.locateNS()
  ns.register('posada.DataFetcher', uri)

  logging.info('posada.DataFetcher uri %s, starting now ...' %uri)
  daemon.requestLoop()
  logging.info('daemon is terminating ...')

