#!/bin/bash

ATD_ORIG_DIR=atd/data
ATD_MCO_DIR=atd-mcl-overseas-alpha

################################################################
# Convert json files to tsv files

# main
python src/convert_json_to_tsv.py \
       -i $ATD_MCO_DIR/full/main/json_per_doc \
       -o $ATD_MCO_DIR/full/main/mention_tsv_per_doc
