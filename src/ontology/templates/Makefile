all:  template terms
template:
	python3 iso-639-template-generator.py
terms:
	robot template --prefix "LANG: http://purl.obolibrary.org/obo/LANG_" --template iso-639-template.tsv --output lang-terms.owl
