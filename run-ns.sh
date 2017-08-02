#!/bin/bash
export PYRO_SERIALIZERS_ACCEPTED=marshal,json,serpent,pickle
export PYRO_LOGLEVEL=DEBUG
pyro4-ns
