#!/bin/bash

ATD_ORIG_DIR=atd/data
ATD_MCO_DIR=atd-mcl-overseas-alpha

################################################################
# Restore full-data docs from original and meta data, 
# and save them as a json file for each doc.

# main
python src/restore_full_documents.py \
    -i1 $ATD_ORIG_DIR/oversea/with_schedules \
    -i2 $ATD_MCO_DIR/meta/main/json_per_doc \
    -o $ATD_MCO_DIR/full/main/json_per_doc

## agreement
python src/restore_full_documents.py \
    -i1 $ATD_ORIG_DIR/oversea/with_schedules \
    -i2 $ATD_MCO_DIR/meta/agreement/step1_mention_and_step2a_coreference/worker1/json_per_doc \
    -o $ATD_MCO_DIR/full/agreement/step1_mention_and_step2a_coreference/worker1/json_per_doc 

python src/restore_full_documents.py \
    -i1 $ATD_ORIG_DIR/oversea/with_schedules \
    -i2 $ATD_MCO_DIR/meta/agreement/step1_mention_and_step2a_coreference/worker2/json_per_doc \
    -o $ATD_MCO_DIR/full/agreement/step1_mention_and_step2a_coreference/worker2/json_per_doc 

python src/restore_full_documents.py \
    -i1 $ATD_ORIG_DIR/oversea/with_schedules \
    -i2 $ATD_MCO_DIR/meta/agreement/step2b_link/worker1/json_per_doc \
    -o $ATD_MCO_DIR/full/agreement/step2b_link/worker1/json_per_doc 

python src/restore_full_documents.py \
    -i1 $ATD_ORIG_DIR/oversea/with_schedules \
    -i2 $ATD_MCO_DIR/meta/agreement/step2b_link/worker2/json_per_doc \
    -o $ATD_MCO_DIR/full/agreement/step2b_link/worker2/json_per_doc 
