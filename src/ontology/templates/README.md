# Templates files for handling ISO-639 data

Data from the ISO 639 Reference Authority is downloaded here and processed using two
steps.  These steps are executed by the `Makefile`

1. Data from ISO 639 + a header file are processed by a python program to 
create a template file for the OBO robot ontology tool.

1. The robot ontology tool uses the template file to 
create a terms in OWL format that are used in further processing.

## Files

* `iso-639-3.tab` Raw data for languages. Includes data for ISO 639 1, 2, and 3

* `iso-639-header.tsv` Added by the template egenerator to create a file ready
for robot.  The format of this file is determined by the robot template tool.

* `iso-639-template-generator.py` Python script.  Reads `iso-639-3.tab` and
`iso-639-header.tsv` and writes `iso-639-template.tsv`

* `iso-639-template.tsv` Created by `iso-639-template-generator.py`. Input to
`robot`

* `iso-639-terms.owl` The resulting lang ontology terms file.  This file is used as
input in further processing by the ontology development tool kit.

* `Makefile` A robot script to convert the template into terms. Reads
`iso-639-template.tsv` Produces
`iso-639-terms.owl`
