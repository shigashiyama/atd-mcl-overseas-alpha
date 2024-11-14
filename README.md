# ATD-MCL-Overseas (Alpha): Overseas Travelogues from Arukikata Travelogue Dataset with Geographic Entity Annotation

## How to Restore the ATD-MCL-Overseas Data

Requirements: Python >= 3.8.0

1. Obtain the Arukikata Travelogue Dataset (ATD) original data (`data.zip`) from the NII IDR site <https://www.nii.ac.jp/dsc/idr/arukikata/>.
1. Decompress `data.zip` and then move `data` directory to under `atd` directory (or create a symbolic link to `data` directory in `atd` directory).
1. Excute `bin/gen_full_data_json.sh`.
    - The restored data will be placed at `atd-mcl-overseas-alpha/full/main/json_per_doc`.
    - The data used for calculating inter-annotator aggreement scores will be placed at `atd-mcl-overseas-alpha/full/agreement`.
1. Excute `bin/gen_full_data_tsv.sh`.
    - The restored data will be placed at `atd-mcl-overseas-alpha/full/main/mention_tsv_per_doc`.

## Data Statistics

|Attribute          |Number |
|--                 |--     |
|Document           |     78|
|Section            |  1,309|
|Sentence           |  4,318|
|Chars              |112,591|
|Mention            |  5,116|
|Entity             |  2,263|

This can be obtained by excuting the following command.
- `python src/show_data_statistics.py -i atd-mcl-overseas-alpha/full/main/json_per_doc/`.

## Data Format

### JSON Data Format

The JSON data (`atd-mcl-overseas-alpha/full/main/json_per_doc`) holds full annotation information as follows.

- A document object value is assosiated with a key that represents the  document ID (e.g., `00019`). Each document object has the sets of `sections`, `sentences`, `mentions`, and `entities`.
   ~~~~
    {
      "00711": {
        "sections": {
          "001": {
          ...
          },
        },
        "sentences": {
          "001-01": {
          ...
          },
        },
        "mentions": {
          "M001": {
            ...
          },
        },
        "entities": {
          "E001": {
            ...
          }
        }
      }
    }
    ~~~~
- A section object under `sections` is as follows:
    ~~~~
    "sections": {
      "001": {
        "sentence_ids": [
          "001-01",
          "001-02",
          "001-03",
          "001-04",
          "001-05"
        ]
      },
    ...
    ~~~~
- A sentence object under `sentences` is as follows:
    - A sentence object may have one or more geographic entity mentions.
    - Some sentences with an ID that has a branch number (e.g., "026-01" and "026-02") indicate that a line of text in the original ATD data was split into those multiple sentences.
    ~~~~
    "sentences": {
      "001-01": {
        "section_id": "001",
        "span_in_orig_text": [
          0,
          33
        ],
        "text": "パラオではオプショナルツアーに参加しないとほとんど観光できません。",
        "mention_ids": [
          "M001"
        ]
      },
      ...
      "006-06": {
        "section_id": "006",
        "span_in_orig_text": [
          168,
          173
        ],
        "text": "オススメ!",
        "mention_ids": []
      }
    },
    ~~~~
- A mention object under `mentions` is as follows:
    - A mention object may be associated with an entity.
    ~~~~
    "mentions": {
      "M001": {
        "sentence_id": "001-01",
        "span": [
          0,
          3
        ],
        "text": "パラオ",
        "entity_type": "LOC_NAME",
        "entity_id": "E001"
      },
    ~~~~
- An entity object, which corresponds to a coreference cluster of one or more mentions, under `entities` is as follows:
    - An entity object is associated with one or more mentions.
    - `has_name` indicates whether at least one member mention's entity type is `*_NAME` or not.
    ~~~~
    "entities": {
      "E001": {
        "original_entity_id": "E001",
        "entity_type_merged": "LOC",
        "has_name": true,
        "member_mention_ids": [
          "M001",
          "M012",
          "M018"
        ]
      },
    ~~~~

### Mention TSV Data Format

The mention TSV data (`atd-mcl-overseas-alpha/full/main/mention_tsv_per_doc`) holds mention-related annotation information as follows.

- 1st column: document_id
- 2nd column: section_id:sentence_id
- 3rd column: Sentence `text`
- 4th column: Mention information with the following elements. Multiple mentions are enumerated with ";".
  - 1st element: mention_id
  - 2nd element: `span`
  - 3rd element: `entity_type`
  - 4th element: mention `text`
  - 5th element: `entity_id`
  - 6th element: `generic`
  - 7th element: `ref_spec_amb`
  - 8th element: `ref_hie_amb`

Example:
~~~~
00711	002:002-01	日本で化粧品が発売されて有名になった、ミルキーウェイです。	M006,0:2,LOC_NAME,日本,E004,,,;M007,19:26,LOC_NAME,ミルキーウェイ,E005,,,
~~~~

## Detailed Data Specification

See `docs/data_specification`.

## Contact

- Shohei Higashiyama <shohei.higashiyama [at] nict.go.jp>

## Acknowledgements

The annotation data was constructed by [IR-Advanced Linguistic Technologies Inc.](https://ir-alt.co.jp/)

## Citation

TBA
