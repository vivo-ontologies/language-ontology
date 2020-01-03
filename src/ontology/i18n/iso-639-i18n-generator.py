#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    iso-639-i18n-generator.py: read the LOC ttl to a graph.  Select labels to a dict, keyed on iso-639-2 code.
    For each fr label, match the iso-639-2 to the lang ontology and output a triple with the iri of the language,
    rdfs:label as the predicate, and the french label.  Repeat for the german labels.
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright (c) 2020 Michael Conlon"
__license__ = "Apache-2"
__version__ = "0.1.0"

from rdflib import Graph, URIRef
from rdflib.namespace import SKOS, RDFS, Namespace

obo = Namespace("http://purl.obolibrary.org/obo/")

def main():

    uri = {}
    new_uri = {}

    g = Graph()
    g.parse("vocabularyiso639-2.ttl", format="ttl")
    print("lines in ISO vocab", len(g))


    g1 = Graph()
    g1.parse('../templates/iso-639-terms.owl', format="xml")
    g1s = Graph()
    for s, p, o in g1:
        if p == obo.LANG_0000003:  # Part 2T code
            g1s.add((s, RDFS.label, o))
            uri[str(o)] = s
            print(s, p, o)
    for s, p, o in g1:
        if p == obo.LANG_0000004:  # Part 2B Code
            g1s.add((s, RDFS.label, o))
            uri[str(o)] = s
            print(s, p, o)
    g1s.serialize('out.nt', format='nt')

    print(len(uri))

    print(sorted(uri.keys()))



    g2 = Graph()

    for s, p, o in g:
        if p == SKOS.notation:
            if str(o) in uri.keys():
                new_uri[s] = uri[str(o)]
            else:
                print('key in LOC', str(o), 'not found in lang terms')

    print(new_uri)

    for s, p, o in g:
        if p == SKOS.prefLabel:
            if hasattr(o, 'language') and (o.language == 'fr' or o.language == 'de'):
                if s in new_uri.keys():
                    g2.add((new_uri[s], RDFS.label, o))

    print(len(g2), 'labels to add')
    g2.serialize("iso-639-i18n.nt", format="nt")
    return


if __name__ == "__main__":
    main()
