from oasis_utilities import *
from process_transcript import *

# Oasis archive directory
archive_dir = 'oasis_archive'

# Processed data directory
data_dir = 'oasis_data'

# Metadata directory
metadata_dir = os.path.join(data_dir, 'metadata')

# If flag is set will only write utterances and not speaker or DA label
utterance_only_flag = False

# Excluded dialogue act tags i.e.
excluded_tags = ['uninterpretable', 'iuninterpretable', 'unclassifiable', 'frag', 'decl', 'thirdParty']
# Excluded characters for ignoring i.e. '=='
excluded_chars = {'<', '>', '(', ')', '#', '|', '=', '@', '*'}

# Files for all the utterances in the corpus and data splits
full_set_file = "full_set"
train_set_file = "train_set"
test_set_file = "test_set"
val_set_file = "val_set"
dev_set_file = "dev_set"

# Remove old files if they exist, so we do not append to old data
remove_file(data_dir, full_set_file, utterance_only_flag)
remove_file(data_dir, train_set_file, utterance_only_flag)
remove_file(data_dir, test_set_file, utterance_only_flag)
remove_file(data_dir, val_set_file, utterance_only_flag)
remove_file(data_dir, dev_set_file, utterance_only_flag)

# Clean up archive directory of unneeded files
for file in os.listdir(archive_dir):
    if any(substring in file for substring in ['.x.', 'overlap', 'propernoun', 'digit', 'lancs_bt']):
        os.remove(os.path.join(archive_dir, file))

# Get a list of all the unique transcript file id's
transcript_list = [file.split(".")[0] for file in os.listdir(archive_dir)]
transcript_list = list(set(transcript_list))
transcript_list.sort()

# Split into training, validation, test  and development sets
train_split, val_split, test_split, dev_split = split_sets(metadata_dir, transcript_list[:], train_set_split=0.8)

# Process each transcript
for transcript in transcript_list:

    # Get the turn list, words and DA files for both speakers
    turn_list = load_text_data(os.path.join(archive_dir, transcript + '.ldial.xml'))
    a_words_file = load_text_data(os.path.join(archive_dir, transcript + '.a.unit.xml'))
    a_da_file = load_text_data(os.path.join(archive_dir, transcript + '.a.lturn.xml'))
    b_words_file = load_text_data(os.path.join(archive_dir, transcript + '.b.unit.xml'))
    b_da_file = load_text_data(os.path.join(archive_dir, transcript + '.b.lturn.xml'))

    # Process the utterances and create a dialogue object
    dialogue = process_transcript(turn_list, a_words_file, a_da_file, b_words_file, b_da_file, excluded_chars, excluded_tags)

    # Append all utterances to full_set text file
    dialogue_to_file(os.path.join(data_dir, full_set_file), dialogue, utterance_only_flag, 'a+')

    # Determine which set this dialogue belongs to (training, test or validation)
    set_dir = ''
    set_file = ''
    if dialogue.conversation_id in train_split:
        set_dir = 'train'
        set_file = train_set_file
    elif dialogue.conversation_id in test_split:
        set_dir = 'test'
        set_file = test_set_file
    elif dialogue.conversation_id in val_split:
        set_dir = 'val'
        set_file = val_set_file

    # If only saving utterances use different directory
    if utterance_only_flag:
        set_dir = os.path.join(data_dir, set_dir + '_utt')
    else:
        set_dir = os.path.join(data_dir, set_dir)

    # Create the directory if is doesn't exist yet
    if not os.path.exists(set_dir):
        os.makedirs(set_dir)

    # Write individual dialogue to train, test or validation folders
    dialogue_to_file(os.path.join(set_dir, dialogue.conversation_id), dialogue, utterance_only_flag, 'w+')

    # Append all dialogue utterances to sets file
    dialogue_to_file(os.path.join(data_dir, set_file), dialogue, utterance_only_flag, 'a+')

    # If it is also in the development set write it there too
    if dialogue.conversation_id in dev_split:

        set_dir = 'dev'
        set_file = dev_set_file

        # If only saving utterances use different directory
        if utterance_only_flag:
            set_dir = os.path.join(data_dir, set_dir + '_utt')
        else:
            set_dir = os.path.join(data_dir, set_dir)

        # Create the directory if is doesn't exist yet
        if not os.path.exists(set_dir):
            os.makedirs(set_dir)

        # Write individual dialogue to dev folder
        dialogue_to_file(os.path.join(set_dir, dialogue.conversation_id), dialogue, utterance_only_flag, 'w+')

        # Append all dialogue utterances to dev set file
        dialogue_to_file(os.path.join(data_dir, set_file), dialogue, utterance_only_flag, 'a+')
