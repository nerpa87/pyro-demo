import Pyro4
Pyro4.config.SERIALIZERS_ACCEPTED='marshal,json,serpent,pickle'
Pyro4.config.SERIALIZER='pickle'

posadaFetcher = Pyro4.Proxy('PYRONAME:posada.DataFetcher')
posadaFetcher.getValues('/a/s/d')