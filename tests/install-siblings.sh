#/bin/bash

pbrx install-siblings -c ../requirements/upper-constraints.txt $(find ../.. -mindepth 2 -maxdepth 2)
