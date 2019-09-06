import itertools
import gluonnlp as nlp
from oasis_utilities import *
# Initialise Spacy tokeniser
tokeniser = nlp.data.SpacyTokenizer('en')

# Dictionary for metadata
metadata = dict()

# Processed data directory
data_dir = 'oasis_data'

# Metadata directory
metadata_dir = os.path.join(data_dir, 'metadata')

# Load full_set text file
maptask_text = load_text_data(os.path.join(data_dir, 'full_set.txt'))

# Split into labels and utterances
utterances = []
labels = []
for line in maptask_text:
    utterances.append(line.split("|")[1])
    labels.append(line.split("|")[2])

# Count total number of utterances
num_utterances = len(utterances)

metadata['num_utterances'] = num_utterances
print("Total number of utterances: ", num_utterances)

# Calculate max utterance length in tokens
max_utterance_len = 0
tokenised_utterances = []
for utt in utterances:

    # Tokenise utterance
    tokenised_utterance = tokeniser(utt)
    if len(tokenised_utterance) > max_utterance_len:
        max_utterance_len = len(tokenised_utterance)

    tokenised_utterances.append(tokenised_utterance)

metadata['max_utterance_len'] = max_utterance_len
print("Max utterance length: ", max_utterance_len)
assert num_utterances == len(tokenised_utterances)

# Count the word frequencies and generate vocabulary
word_freq = nlp.data.count_tokens(list(itertools.chain(*tokenised_utterances)))
vocabulary = nlp.Vocab(word_freq)
vocabulary_size = len(word_freq)

metadata['word_freq'] = word_freq
metadata['vocabulary'] = vocabulary
metadata['vocabulary_size'] = vocabulary_size
print("Words:")
print(word_freq)
print(vocabulary)
print(vocabulary_size)

# Write vocabulary and word frequencies to file
with open(os.path.join(metadata_dir, 'vocabulary.txt'), 'w+') as file:
    for i in range(4, len(vocabulary)):
        file.write(vocabulary.to_tokens(i) + " " + str(word_freq[vocabulary.to_tokens(i)]) + "\n")

# Count the label frequencies and generate labels
label_freq = nlp.data.count_tokens(labels)
labels = nlp.Vocab(label_freq)
num_labels = len(label_freq)

metadata['label_freq'] = label_freq
metadata['labels'] = labels
metadata['num_labels'] = num_labels
print("Labels:")
print(label_freq)
print(labels)
print(num_labels)

# Write labels and frequencies to file
with open(os.path.join(metadata_dir, 'labels.txt'), 'w+') as file:
    for i in range(4, len(labels)):
        file.write(labels.to_tokens(i) + " " + str(label_freq[labels.to_tokens(i)]) + "\n")

# Count sets number of dialogues and maximum dialogue length
max_dialogues_len = 0
sets = ['train', 'test', 'val', 'dev']
for i in range(len(sets)):

    # Load data set list
    set_list = load_text_data(os.path.join(metadata_dir, sets[i] + '_split.txt'))

    # Count the number of dialogues in the set
    set_num_dialogues = len(set_list)
    metadata[sets[i] + '_num_dialogues'] = set_num_dialogues
    print("Number of dialogue in " + sets[i] + " set: " + str(set_num_dialogues))

    # Count max number of utterances in sets dialogues
    set_max_dialogues_len = 0
    for dialogue in set_list:

        # Load dialogues utterances
        utterances = load_text_data(os.path.join(data_dir, sets[i], dialogue + '.txt'), verbose=False)

        # Check set and global maximum dialogue length
        if len(utterances) > set_max_dialogues_len:
            set_max_dialogues_len = len(utterances)

        if set_max_dialogues_len > max_dialogues_len:
            max_dialogues_len = set_max_dialogues_len

    metadata[sets[i] + '_max_dialogues_len'] = set_max_dialogues_len
    print("Maximum length of dialogue in " + sets[i] + " set: " + str(set_max_dialogues_len))

metadata['max_dialogues_len'] = max_dialogues_len
print("Maximum dialogue length: " + str(max_dialogues_len))

# Save data to pickle file
save_data_pickle(os.path.join(metadata_dir, 'metadata.pkl'), metadata)
