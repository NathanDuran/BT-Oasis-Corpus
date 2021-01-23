# Processing the BT Oasis Corpus
Utilities for Processing the [BT Oasis Corpus](http://groups.inf.ed.ac.uk/oasis/)
for the purpose of dialogue act (DA) classification.
The data has been randomly split, with the training set comprising 80% of the dialogues (508), and test and validation
sets 10% each (64).

## Scripts
The oasis_to_text.py script processes all dialogues into a plain text format.
Individual dialogues are saved into directories corresponding to the set they belong to (train, test, etc).
All utterances in a particular set are also saved to a text file.

The utilities.py script contains various helper functions for loading/saving the data.
 
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
Dialogue Act                   |        Labels        |  Count   |    %     |   Train Count   | Train %  |   Test Count    |  Test %  |    Val Count    |  Val %  
--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
Inform                         |        inform        |   3066   |  20.35   |      2422       |  20.06   |       307       |  20.77   |       337       |  22.27  
Acknowledge                    |         ackn         |   2015   |  13.37   |      1621       |  13.42   |       192       |  12.99   |       202       |  13.35  
Request Inform                 |       reqInfo        |   1404   |   9.32   |      1141       |   9.45   |       139       |   9.40   |       124       |   8.20  
Backchannel                    |        backch        |   1131   |   7.51   |       902       |   7.47   |       120       |   8.12   |       109       |   7.20  
Answer                         |         answ         |   844    |   5.60   |       677       |   5.61   |       92        |   6.22   |       75        |   4.96  
Initialise                     |         init         |   797    |   5.29   |       626       |   5.18   |       82        |   5.55   |       89        |   5.88  
Thank                          |        thank         |   770    |   5.11   |       621       |   5.14   |       74        |   5.01   |       75        |   4.96  
Greet                          |        greet         |   529    |   3.51   |       432       |   3.58   |       51        |   3.45   |       46        |   3.04  
Accept                         |        accept        |   464    |   3.08   |       373       |   3.09   |       43        |   2.91   |       48        |   3.17  
Answer Elaborate               |       answElab       |   457    |   3.03   |       376       |   3.11   |       42        |   2.84   |       39        |   2.58  
Inform Intention               |     informIntent     |   428    |   2.84   |       341       |   2.82   |       47        |   3.18   |       40        |   2.64  
Bye                            |         bye          |   412    |   2.73   |       335       |   2.77   |       36        |   2.44   |       41        |   2.71  
Direct                         |        direct        |   401    |   2.66   |       323       |   2.67   |       39        |   2.64   |       39        |   2.58  
Confirm                        |       confirm        |   349    |   2.32   |       284       |   2.35   |       21        |   1.42   |       44        |   2.91  
Express Regret                 |    expressRegret     |   255    |   1.69   |       213       |   1.76   |       18        |   1.22   |       24        |   1.59  
Hold                           |         hold         |   219    |   1.45   |       178       |   1.47   |       21        |   1.42   |       20        |   1.32  
Express Opinion                |    expressOpinion    |   197    |   1.31   |       144       |   1.19   |       26        |   1.76   |       27        |   1.78  
Offer                          |        offer         |   157    |   1.04   |       129       |   1.07   |       12        |   0.81   |       16        |   1.06  
Echo                           |         echo         |   128    |   0.85   |       107       |   0.89   |        7        |   0.47   |       14        |   0.93  
Appreciate                     |      appreciate      |   111    |   0.74   |       90        |   0.75   |       11        |   0.74   |       10        |   0.66  
Refer                          |        refer         |   109    |   0.72   |       81        |   0.67   |       19        |   1.29   |        9        |   0.59  
Suggest                        |       suggest        |   103    |   0.68   |       81        |   0.67   |       10        |   0.68   |       12        |   0.79  
Request Direct                 |      reqDirect       |    94    |   0.62   |       74        |   0.61   |       12        |   0.81   |        8        |   0.53  
Negate                         |        negate        |    91    |   0.60   |       73        |   0.60   |        3        |   0.20   |       15        |   0.99  
Exclaim                        |       exclaim        |    83    |   0.55   |       68        |   0.56   |       10        |   0.68   |        5        |   0.33  
Pardon                         |        pardon        |    83    |   0.55   |       68        |   0.56   |        6        |   0.41   |        9        |   0.59  
Identify Self                  |     identifySelf     |    73    |   0.48   |       60        |   0.50   |        5        |   0.34   |        8        |   0.53  
Express Possibility            |  expressPossibility  |    71    |   0.47   |       56        |   0.46   |        8        |   0.54   |        7        |   0.46  
Raise Issue                    |      raiseIssue      |    35    |   0.23   |       30        |   0.25   |        4        |   0.27   |        1        |   0.07  
Express Wish                   |     expressWish      |    34    |   0.23   |       28        |   0.23   |        2        |   0.14   |        4        |   0.26  
Request Modal                  |       reqModal       |    26    |   0.17   |       20        |   0.17   |        2        |   0.14   |        4        |   0.26  
Complete                       |       complete       |    20    |   0.13   |       13        |   0.11   |        6        |   0.41   |        1        |   0.07  
Direct Elaborate               |      directElab      |    20    |   0.13   |       14        |   0.12   |        3        |   0.20   |        3        |   0.20  
Correct                        |       correct        |    19    |   0.13   |       15        |   0.12   |        2        |   0.14   |        2        |   0.13  
Refuse                         |        refuse        |    16    |   0.11   |       12        |   0.10   |        1        |   0.07   |        3        |   0.20  
Inform Intent Hold             |  informIntent-hold   |    13    |   0.09   |       11        |   0.09   |        0        |   0.00   |        2        |   0.13  
Inform Continue                |      informDisc      |    12    |   0.08   |       11        |   0.09   |        1        |   0.07   |        0        |   0.00  
Inform Discontinue             |      informCont      |    12    |   0.08   |       10        |   0.08   |        2        |   0.14   |        0        |   0.00  
Self Talk                      |       selfTalk       |    10    |   0.07   |        7        |   0.06   |        2        |   0.14   |        1        |   0.07  
Correct Self                   |     correctSelf      |    7     |   0.05   |        7        |   0.06   |        0        |   0.00   |        0        |   0.00  
Express Regret Inform          | expressRegret-inform |    1     |   0.01   |        1        |   0.01   |        0        |   0.00   |        0        |   0.00  
Thank Identify Self            |  thank-identifySelf  |    1     |   0.01   |        1        |   0.01   |        0        |   0.00   |        0        |   0.00  

![Label Frequencies](oasis_data/metadata/BT-Oasis%20Label%20Frequency%20Distributions.png)

## Metadata
- Total number of utterances: 15067
- Max utterance length: 449
- Mean utterance length: 9.66
- Total Number of dialogues: 636
- Max dialogue length: 153
- Mean dialogue length: 23.69
- Vocabulary size: 2230
- Number of labels:42
- Number of speakers: 2

Train set
- Number of dialogues: 508
- Max dialogue length: 153
- Mean dialogue length: 23.77
- Number of utterances: 12076

Test set
- Number of dialogues: 64
- Max dialogue length: 92
- Mean dialogue length: 23.27
- Number of utterances: 1489

Val set
- Number of dialogues: 64
- Max dialogue length: 78
- Mean dialogue length: 23.47
- Number of utterances: 1502

### Keys and values for the metadata dictionary
- num_utterances = Total number of utterance in the full corpus.
- max_utterance_len = Number of words in the longest utterance in the corpus.
- mean_utterance_len = Average number of words in utterances.
- num_dialogues = Total number of dialogues in the corpus.
- max_dialogues_len = Number of utterances in the longest dialogue in the corpus.
- mean_dialogues_len = Average number of utterances in dialogues.
- word_freq = [Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) with Word and Count columns.
- vocabulary = List of all words in vocabulary.
- vocabulary_size = Number of words in the vocabulary.
- label_freq = [Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) containing all data in the Dialogue Acts table above.
- labels = List of all DA labels.
- num_labels = Number of labels used from the Oasis data.
- speakers = List of all speakers.
- num_speakers = Number of speakers in the Oasis data.
 
Each data set also has:
- <*setname*>_num_utterances = Number of utterances in the set.
- <*setname*>_num_dialogues = Number of dialogues in the set.
- <*setname*>_max_dialogue_len = Length of the longest dialogue in the set.
- <*setname*>_mean_dialogue_len = Mean length of dialogues in the set.