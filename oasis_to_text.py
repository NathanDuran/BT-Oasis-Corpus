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
excluded_tags = []
# Excluded characters for ignoring i.e. '=='
excluded_chars = {'<', '>', '(', ')', '#', '|', '=', '@'}

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
    if any(substring in file for substring in ['.x.', 'overlap', 'propernoun', 'digit']):
        os.remove(os.path.join(archive_dir, file))

# Get a list of all the unique transcript file id's
transcript_list = [file.split(".")[0] for file in os.listdir(archive_dir)]
transcript_list = list(set(transcript_list))
print(transcript_list)
print(len(transcript_list))
# Split into training, validation, test  and development sets
train_split, val_split, test_split, dev_split = split_sets(metadata_dir, transcript_list[:], train_set_split=0.8)
print(len(train_split))
print(len(val_split))
print(len(test_split))
print(len(dev_split))