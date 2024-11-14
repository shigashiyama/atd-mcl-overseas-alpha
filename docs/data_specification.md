# Data Specification

## Entity Type Tags

In the mention annotation step, each mention was manually assigned one of the entity type tags as `entity_type`. After the manual mention and coreference annoation, each entity was automatically assigned an entity type tag as `entity_type_merged` on the basis of its member mentions' entity types. Notably, `MIX` is assigned to an entity whose member mentions' entity types includes two or more of `LOC`, `FAC`, `LINE`, and `TRANS`.

|Tag                     |Description|
|--                      |--         |
|`LOC_NAME`/`LOC_NOM`    |Locations  |
|`FAC_NAME`/`FAC_NOM`    |Facilities |
|`LINE_NAME`/`LINE_NOM`  |Roads, warterways/rivers, or public transport lines|
|`TRANS_NAME`/`TRANS_NOM`|Public transport vehicles|
|`LOC_ORG`               |Location mentions that metonymically refer to organizations|
|`FAC_ORG`               |Facility mentions that metonymically refer to organizations|
|`LOC_OR_FAC`            |Nominal mentions that can refer to both location and facility|
|`DEICTIC`               |Deictic expressions that refer to some locations|

## Specificity Tags

In the coreference annoation step, specificity tags were assigned to the applicable mentions. These tags are assigned as entities' attributes in the JSON data (not mentions' attributes).

- `GENERIC`: This tag is assigned to a generic mention that does not refer to a real-world location, e.g., "(I like) temples."
- `SPEC_AMB`: This tag is assigned to a mention that refers to a specific real-world location, but there is some ambiguity about the detailed area to which it refers, e.g., "sea."
- `HIE_AMB`: This tag is assigned to an ambiguously described mention with multiple poetntial referents of higher and lower-level locations, e.g., "(We are heading to) Nara." Annotators were instructed to annotate with coreference and link information based on the hypothesis that such mentions refer to the lowest-level location among candidate referents, e.g., not Nara Prefecture but Nara City.

## Attributes of Document Object

Attributes annotated by a human annotator are written with "*".

Section
- `sentence_ids`: The IDs of sentences in the section.

Sentence
- `section_id`: The ID of section to which the sentence belongs.
- `span_in_orig_text`: The pair of the sentence's first and last character offsets in the original text in `*.tra.json`.
- `text`: The sentence text.
- `mention_ids`: The IDs of mentions occurring in the sentence.

Mention (mention ID starts with `M`)
- `sentence_id`: The ID of sentence in which the mention occurs.
- `entity_id`: The ID of entity to which the entity belongs.
- *`span`: The pair of the mention's first and last character offsets in the sentence.
- `text`: The mention text.
- *`entity_type`: The entity type of the mention.
- *`generic`: Whether `GENERIC` is assigned to the mention.
- *`ref_spec_amb`: Whether `SPEC_AMB` is assigned to the mention.
- *`ref_hie_amb`: Whether `HIE_AMB` is assigned to the mention.
