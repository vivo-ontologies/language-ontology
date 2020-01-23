# Editing the Language Ontology

This project was created using the [ontology development kit](https://github.com/INCATools/ontology-development-kit). See the site for details.

For more details on ontology management, please see the [OBO tutorial](https://github.com/jamesaoverton/obo-tutorial) or the [Gene Ontology Editors Tutorial](https://go-protege-tutorial.readthedocs.io/en/latest/)

You may also want to read the [GO ontology editors guide](http://go-ontology.readthedocs.org/)

For development, build and release processes of the Language Ontology, please see [Language Ontology Development, Build, and Release Processes](https://github.com/vivo-community/language-ontology/wiki/Language-Ontology-Development,-Build,-and-Release-Processes) in the wiki of this repository.

## Requirements

 1. Protege (for editing)
 2. A git client (we assume command line git)
 3. [docker](https://www.docker.com/get-docker) (for managing releases)

## Editor's Version

The editor's version is [lang-edit.owl](lang-edit.owl)

**DO NOT EDIT lang.obo OR lang.owl in the top level directory, these are created automatically by the Makefile**

**DO NOT EDIT the template files.  See the README in [../templates](../templates) for a description of how the 
language classes are created from ISO-639-3 data.  They are not created by editing.** 

[../../lang.owl](../../lang.owl) is the release version and may be useful for inspection -- it contains all 
assertions.  lang-edit.owl does not include i18n, templated, or imported assertions.  This makes lang-edit small, 
and easy to work with, but "hides" some assertions that may be useful to see.

To edit, first make sure you have the repository cloned, see [the GitHub project](https://github.com/vivo-community/language-ontology) for details. The edit [lang-edit.owl](lang-edit.owl) using Protege or other editor.

You should discuss the git workflow you should use with the maintainer
of this repo, who should document it here. If you are the maintainer,
you can contact the odk developers for assistance. You may want to
copy the flow an existing project, for example GO: [Gene Ontology
Editors Tutorial](https://go-protege-tutorial.readthedocs.io/en/latest/).

In general, it is bad practice to commit changes to master. It is
better to make changes on a branch, and make Pull Requests.

## Imports

*Note: The Language Ontology currently imports two terms from BFO*

To add additional terms to import:

1. Add the ontology source to [./mirror](./mirror) if it not already there
1. Add the terms to be imported to the file [./imports/ontology-terms-complete.txt] where
ontology is the name of the ontology from which terms will be imported
1. Edit the Makefile to add the new ontology to the list of imports

## Design patterns

*Note: The Language Ontology does not currently use design patterns*

You can automate (class) term generation from design patterns by placing DOSDP
yaml file and tsv files under src/patterns. Any pair of files in this
folder that share a name (apart from the extension) are assumed to be
a DOSDP design pattern and a corresponding tsv specifying terms to
add.

Design patterns can be used to maintain and generate complete terms
(names, definitions, synonyms etc) or to generate logical axioms
only, with other axioms being maintained in editors file.  This can be
specified on a per-term basis in the TSV file.

Design pattern docs are checked for validity via Travis, but can be
tested locally using

`./run.sh make patterns`

In addition to running standard tests, this command generates an owl
file (`src/patterns/pattern.owl`), which demonstrates the relationships
between design patterns.

(At the time of writing, the following import statements need to be
added to `src/patterns/pattern.owl` for all imports generated in
`src/imports/*_import.owl`.   This will be automated in a future release.')

To compile design patterns to terms run:

`./run.sh make ../patterns/definitions.owl`

This generates a file (`src/patterns/definitions.owl`).  You then need
to add an import statement to the editor's file to import the
definitions file.


## Release Manager notes

*Note: The Language Ontology does not currently use travis*

You should only attempt to make a release AFTER the edit version is
committed and pushed, AND the travis build passes.

These instructions assume you have
[docker](https://www.docker.com/get-docker). This folder has a script
[run.sh](run.sh) that wraps docker commands.

to release:

first type

    git branch

to make sure you are on master

    cd src/ontology
    ./build.sh

If this looks good type:

    ./prepare_release.sh

This generates derived files such as lang.owl and lang.obo and places
them in the top level (../..).

Note that the versionIRI value automatically will be added, and will
end with YYYY-MM-DD, as per OBO guidelines.

Commit and push these files.

    git commit -a

And type a brief description of the release in the editor window

Finally type:

    git push origin master

__IMMEDIATELY AFTERWARDS__ (do *not* make further modifications) go here:

 * https://github.com/vivo-community/language-ontology/releases
 * https://github.com/vivo-community/language-ontology/releases/new

__IMPORTANT__: The value of the "Tag version" field MUST be

    vYYYY-MM-DD

The initial lowercase "v" is REQUIRED. The YYYY-MM-DD *must* match
what is in the `owl:versionIRI` of the derived lang.owl (`data-version` in
lang.obo). This will be today's date.

This cannot be changed after the fact, be sure to get this right!

Release title should be YYYY-MM-DD, optionally followed by a title (e.g. "january release")

You can also add release notes (this can also be done after the fact). These are in 
markdown format. In future ODK will have better tools for auto-generating release notes.

Then click "publish release"

__IMPORTANT__: NO MORE THAN ONE RELEASE PER DAY.

The PURLs are already configured to pull from github. This means that
BOTH ontology purls and versioned ontology purls will resolve to the
correct ontologies. Try it!

 * http://purl.obolibrary.org/obo/lang.owl <-- current ontology PURL
 * http://purl.obolibrary.org/obo/lang/releases/YYYY-MM-DD.owl <-- change to the release you just made

For questions on this contact Chris Mungall or email obo-admin AT obofoundry.org

# Travis Continuous Integration System

Check the build status here: [![Build Status](https://travis-ci.org/vivo-community/language-ontology.svg?branch=master)](https://travis-ci.org/vivo-community/language-ontology)

Note: if you have only just created this project you will need to authorize travis for this repo.

 1. Go to [https://travis-ci.org/profile/vivo-community](https://travis-ci.org/profile/vivo-community)
 2. click the "Sync account" button
 3. Click the tick symbol next to language-ontology

Travis builds should now be activated
