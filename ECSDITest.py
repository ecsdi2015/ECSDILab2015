# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:28:58 2013

@author: javier
"""

import rdflib
import rdfextras
from rdflib.graph import Graph
from rdflib import OWL,Namespace
import pprint
from rdflib import plugin

# plugin.register(
#     'sparql', rdflib.query.Processor,
#     'rdfextras.sparql.processor', 'Processor')
# plugin.register(
#     'sparql', rdflib.query.Result,
#     'rdfextras.sparql.query', 'SPARQLQueryResult')
#

g = Graph()

g.parse('/home/javier/Documentos/ECSDI/code/ExampOnto.owl')

for (a,b,c) in g:
    print a,b,c

#for stmt in g:
#    pprint.pprint(stmt)
    

#qres = g.query(
#    """
#       SELECT DISTINCT ?aname ?bname
#       WHERE {
#          ?a ex:Likes ?b .
#          ?a ex:Name ?aname .
#          ?b ex:Name ?bname .
#        }""",
#    initNs=dict(
#        ex=Namespace("http://www.owl-ontologies.com/OntoTest.owl#")))

# qres = g.query(
#     """
#        SELECT DISTINCT ?a ?b
#        WHERE {
#           ?a ex:Likes ?b .
#         }""",
#     initNs=dict(
#         ex=Namespace("http://www.owl-ontologies.com/OntoTest.owl#")))
        
# pprint.pprint(qres.result)
# for row in qres.result:
#     print("%s likes %s" % row)