#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    iso-639-i18n-generator.py: read the LOC ttl to a graph.  Select labels to a dict, keyed on iso-639-2 code.
    Read the LOC translation data to a graph.  For each fr label, match the iso-639-2 to the lang ontology and output
    a triple with the iri of the language, rdfs:label as the predicate, and the french label.  Repeat for the german
    labels.
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright (c) 2020 Michael Conlon"
__license__ = "Apache-2"
__version__ = "0.1.0"

from rdflib import Graph, URIRef
from rdflib.namespace import SKOS, RDFS, Namespace

OBO = Namespace("http://purl.obolibrary.org/obo/")


def main():

    uri = {}
    new_uri = {}

    #  Read the LOC translation data a graph.  These have the french and german translations and the codes.

    g = Graph()
    g.parse("vocabularyiso639-2.ttl", format="ttl")
    print("Assertions in LOC vocabulary", len(g))

    # Read the language terms to a graph.  These have the LANG IRI, and the codes.

    g1 = Graph()
    g1.parse('../templates/iso-639-terms.owl', format="xml")
    g1s = Graph()
    for s, p, o in g1:
        if p == OBO.LANG_0000003:  # Part 2T code
            g1s.add((s, RDFS.label, o))
            uri[str(o)] = s
    for s, p, o in g1:
        if p == OBO.LANG_0000004:  # Part 2B Code
            g1s.add((s, RDFS.label, o))
            uri[str(o)] = s

    print("Assertions in LANG terms", len(uri))

    #   Construct a dictionary for translating LOC IRI to LANG IRI

    g2 = Graph()

    for s, p, o in g:
        if p == SKOS.notation:  # the three letter codes for the languages are skos:notations in the LOC data
            if str(o) in uri.keys():  # look up the code in the dictionary constructed from LANG terms
                new_uri[s] = uri[str(o)]
            else:
                print('key in LOC', str(o), 'not found in lang terms')  # not founds appear to be due deprecated
                # language codes.  LANG has all languages, but not all deprecated codes for non-existent languages.

    # Construct a graph to contain the new assertions.  Each assertion will be of the form
    #
    # <LANG_IRI> rdfs:label "label text"@language
    #
    # where language is either fr or de

    for s, p, o in g:
        if p == SKOS.prefLabel:
            if hasattr(o, 'language') and (o.language == 'fr' or o.language == 'de'):
                if s in new_uri.keys():
                    g2.add((new_uri[s], RDFS.label, o))  # translate the LOC IRI to the LANG IRI

    print(len(g2), 'labels to add')
    g2.serialize("iso-639-i18n.nt", format="nt")
    return


if __name__ == "__main__":
    main()
