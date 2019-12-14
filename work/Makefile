all:  template terms
template:
	python3 iso-639-template-generator.py
terms:
	robot template -vvv --prefix "LANG: http://purl.obolibrary.org/obo/LANG_" --merge-before  --input lang-iterms-annotation-header.owl --template iso-639-template.tsv --output lang-terms.owl
