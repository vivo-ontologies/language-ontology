all:  template terms
template:
	python3 iso-639-template-generator.py
terms:
	robot template --prefix "lang: http://purl.obolibrary.org/obo/LANG_" --prefix "oio: http://www.geneontology.org/formats/oboInOwl#" --template iso-639-template.tsv --output iso-639-terms.owl
