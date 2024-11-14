import argparse
import copy
import json
import os
import sys

from util import load_json, write_as_json, normalize_text


SENS      = 'sentences'
MENS      = 'mentions'
ENTS      = 'entities'

SEC_ID      = 'section_id'
SEN_ID      = 'sentence_id'
MEN_IDS     = 'mention_ids'
ENT_ID      = 'entity_id'
MEM_MEN_IDS = 'member_mention_ids'

TEXT      = 'text'
SPAN      = 'span'
ENT_TYPE  = 'entity_type'
GENERIC   = 'generic'
SPEC_AMB  = 'ref_spec_amb'
HIE_AMB  = 'ref_hie_amb'


def read_and_write(
        data: dict,
        output_tsv_path: str,
) -> None:

    fw = open(output_tsv_path, 'w', encoding='utf-8')
    for doc_id, doc in data.items():
        sentences = doc[SENS]
        mentions  = doc[MENS]

        for sen_id, sen in sentences.items():
            sec_id      = sen[SEC_ID]
            full_sen_id = f'{sec_id}:{sen_id}'
            sen_text    = sen[TEXT]

            mention_info_list = []
            for men_id in sen[MEN_IDS]:
                men      = mentions[men_id]
                men_type = men[ENT_TYPE]
                men_text = men[TEXT]
                span     = men[SPAN]
                ent_id   = men[ENT_ID]
                gen      = GENERIC  if GENERIC  in men and men[GENERIC]  else ''
                spec_amb = SPEC_AMB if SPEC_AMB in men and men[SPEC_AMB] else ''
                hie_amb  = HIE_AMB  if HIE_AMB  in men and men[HIE_AMB]  else ''
                mention_info_list.append(f'{men_id},{span[0]}:{span[1]},{men_type},{men_text},{ent_id},{gen},{spec_amb},{hie_amb}')

            mention_info = ';'.join(mention_info_list)
            fw.write(f'{doc_id}\t{full_sen_id}\t{sen_text}\t{mention_info}\n')

    fw.close()
    print(f'[Info] Saved: {output_tsv_path}', file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_json_dir', required=True)
    parser.add_argument('-o', '--output_tsv_dir', required=True)
    args = parser.parse_args()

    for root, dirs, files in os.walk(top=args.input_json_dir):
        for file_name in files:
            if not file_name.endswith('.json'):
                continue

            file_id = file_name.split('.json')[0]
            json_path = os.path.join(args.input_json_dir, file_name)
            data = load_json(json_path)

            tsv_path = os.path.join(args.output_tsv_dir, f'{file_id}.tsv')
            read_and_write(data, tsv_path)


if __name__ == '__main__':
    main()
