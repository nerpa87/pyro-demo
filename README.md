## python pyro4 client-server demo

Running under python3.

#### On server run

./run-ns.sh
  python run-server.py
  
#### On client run
  python run-client.py -H server.host.name
  
Hostname on server has to be correct.
Pickle is used as serializer. Test method returns numpy array transparently.
