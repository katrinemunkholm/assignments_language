#!/usr/bin/bash

# activate the environment
source ./env/bin/activate
# run the code
python src/Lyrics_search.py "$@"

# close the environment
deactivate