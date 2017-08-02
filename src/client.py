import Pyro4, logging
Pyro4.config.SERIALIZERS_ACCEPTED='marshal,json,serpent,pickle'
Pyro4.config.SERIALIZER='pickle'

proxy = None

def init(server_hostname):
  global proxy
  nameserver = Pyro4.locateNS(server_hostname)
  obj_uri = nameserver.lookup('posada.DataFetcher')
  logging.debug('obj_uri %s' % obj_uri)
  proxy = Pyro4.Proxy(obj_uri)
  logging.debug('proxy initialized %s' % proxy)

def execute_method():
  logging.debug('proxy %s' % proxy)
  res = proxy.getValues('/some/args/here')
  logging.info('result received')
  print(res)