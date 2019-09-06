# Processing the BT Oasis Corpus
Utilities for Processing the [BT Oasis Corpus](http://groups.inf.ed.ac.uk/oasis/)
for the purpose of dialogue act (DA) classification.
The data has been randomly split, with the training set comprising 80% of the dialogues (508), and test and validation
sets 10% each (64). 50% of the training set is used as a development set (254).

## Scripts
The oasis_to_text.py script processes all dialogues into a plain text format.
Individual dialogues are saved into directories corresponding to the set they belong to (train, test, etc).
All utterances in a particular set are also saved to a text file.

The oasis_utilities.py script contains various helper functions for loading/saving the data.
 
The process_transcript.py includes functions for processing each dialogue.

The oasis_metadata.py generates various metadata from the processed dialogues and saves them as a dictionary to a pickle file.
The words, labels and frequencies are also saved as plain text files in the /metadata directory.

## Data Format
Utterance are tagged with the [SPAAC Annotation Scheme](SPAAC%20Annotation%20Scheme.pdf) for DA.

By default:
- Utterances are written one per line in the format *Speaker* | *Utterance Text* | *Dialogue Act Tag*.
- Setting the utterance_only_flag == True, will change the default output to only one utterance per line i.e. no speaker or DA tags.
- Utterances marked as *uninterpretable*, *unclassifiable*, *frag*, *decl* and *thirdParty* are removed.

### Example Utterances
b|i think i'm a bit behind on my payments|expressOpinion

a|right|ackn

a|um can you just bear with me|hold

## Dialogue Acts
Dialogue Act    |  Count
--- |  :---:
inform      | 3066
ackn        | 2015
reqInfo     | 1404
backch      | 1131
answ        | 844
init        | 797
thank       | 770
greet       | 529
accept      | 464
answElab    | 457
informIntent | 428
bye         | 412
direct      | 401
confirm     | 349
expressRegret | 255
hold        | 219
expressOpinion | 197
offer       | 157
echo        | 128
appreciate  | 111
refer       | 109
suggest     | 103
reqDirect   | 94
negate      | 91
exclaim     | 83
pardon      | 83
identifySelf | 73
expressPossibility | 71
raiseIssue  | 35
expressWish | 34
reqModal    | 26
complete    | 20
directElab  | 20
correct     | 19
refuse      | 16
informIntent-hold | 13
informCont  | 12
informDisc  | 12
selfTalk    | 10
correctSelf | 7
expressRegret-inform | 1
thank-identifySelf | 1

## Metadata
- Total number of utterances:  15067
- Max utterance length:  449
- Maximum dialogue length: 153
- Vocabulary size: 2230
- Number of labels: 42
- Number of dialogue in train set: 508
- Maximum length of dialogue in train set: 153
- Number of dialogue in test set: 64
- Maximum length of dialogue in test set: 61
- Number of dialogue in val set: 64
- Maximum length of dialogue in val set: 89
- Number of dialogue in dev set: 254
- Maximum length of dialogue in dev set: 153

### Keys and values for the metadata dictionary
- num_utterances = Total number of utterance in the full corpus.
- max_utterance_len = Number of words in the longest utterance in the corpus.
- max_dialogues_len = Number of utterances in the longest dialogue in the corpus.
- word_freq = Dictionary with {word : frequency} pairs.
- vocabulary = Full vocabulary - Gluon NLP [Vocabulary.](http://gluon-nlp.mxnet.io/api/modules/vocab.html#gluonnlp.Vocab)
- vocabulary_size = Number of words in the vocabulary.
- label_freq = Dictionary with {dialogue act label : frequency} pairs.
- labels = Full labels - Gluon NLP [Vocabulary.](http://gluon-nlp.mxnet.io/api/modules/vocab.html#gluonnlp.Vocab)
- num_labels = Number of labels used from the Oasis data.

Each data set also has:
- <*setname*>_num_dialogues = Number of dialogues in the set.
- <*setname*>_max_dialogues_len = Length of the longest dialogue in the set.