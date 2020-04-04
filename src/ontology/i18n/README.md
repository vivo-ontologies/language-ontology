# Internationalization (i18n)

In this folder we have files and tools related to adding i18n text to the
language ontology.

* `vocabularyiso639-2.ttl` is the Library of Congress linked data for iso639-2.  It cantains
french, genrman, and english labels for each of the iso-639 languages.  Note: 
we have no source for language labels for iso639-3.  If you have a source that
can be reused, please open an issue and let us know. 
* `iso-639-i18n-generator.py` is a small python program that reads the LOC linked
data, the LANG terms, and writes `iso-639-i18n.nt` a collecton of triples for
asserting the french and german labels for the language terms.  
* `iso-639-i18n.nt` assertions regarding the names of the languages in french and german.
This file is merged with other sources to create the language ontology. 
* `iso-639-i18n-CEFR-definitions.nt` hand edited triples specifying the CEFR capability
definitions in french, german, spanish, and italian.  Cut and Paste from the CEFR
web site.  CEFR does not provide definitions for the "plus" capabilities, such as B2+. In
each case, the defintion of the "non plus" capability is used with the word "PLUS" added
to the definition to create a label for the plus capability.
