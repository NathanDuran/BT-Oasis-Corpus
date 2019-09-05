class Dialogue:
    def __init__(self, conversation_id, num_utterances, utterances):
        self.conversation_id = conversation_id
        self.num_utterances = num_utterances
        self.utterances = utterances

    def __str__(self):
        return str("Conversation: " + self.conversation_id + "\n"
                   + "Number of Utterances: " + str(self.num_utterances))


class Utterance:
    def __init__(self, speaker, text, da_label):
        self.speaker = speaker
        self.text = text
        self.da_label = da_label

    def __str__(self):
        return str(self.speaker + " " + self.text + " " + self.da_label)


def process_transcript(turn_list, a_words_file, a_da_file, b_words_file, b_da_file, excluded_chars, excluded_tags):

    # Get the list of turns from the turn_list file
    speaker_turns = get_turns(turn_list)

    # Get the DA and word segment id's from the DA file
    a_turn_segments = get_da_and_word_segments(a_da_file)
    b_turn_segments = get_da_and_word_segments(b_da_file)
    segments = {**a_turn_segments, **b_turn_segments}

    # Loop over each turn and create utterances
    utterances = []
    for turn in speaker_turns:

        # Get the speaker
        speaker = speaker_turns[turn]

        # Loop over all utterance in this speakers turn
        if turn in segments.keys():
            segment = segments[turn]
            for utt in segment:

                # Get the utterances words from file
                if speaker is 'a':
                    words = get_words(a_words_file, utt['start_id'], utt['stop_id'])
                else:
                    words = get_words(b_words_file, utt['start_id'], utt['stop_id'])

                # If there are words i.e. not redacted/uninterpretable, concatenate to sentence
                if words:
                    text = " ".join(words)

                    # Check just in case excluded chars are in text
                    if any(char in excluded_chars for char in text):
                        print("Excluded char found!")

                    # Create an utterance
                    utterances.append(Utterance(speaker, text, utt['da']))

    # Create a dialogue
    conversation_id = list(speaker_turns.keys())[0].split('.')[0]
    num_utterance = len(utterances)
    dialogue = Dialogue(conversation_id, num_utterance, utterances)
    return dialogue


def get_turns(turn_list):
    """Gets the speaker turn order and ID's from the .idial.xml files."""
    turns = {}

    for line in turn_list:
        # Ignore lines that don't have a turn
        if '<turn_pointer' not in line:
            continue

        # Get the turns speaker and ID
        speaker = line.split('href=')[1].split('.')[1]
        turn_id = line.split('(')[1].split(')')[0]

        # Add to the map
        turns[turn_id] = speaker
    return turns


def get_da_and_word_segments(da_file):
    """Gets the DA and utterance word segment ID's from the .lturn.xml files."""

    turn_segments = {}
    for i in range(len(da_file)):
        line = da_file[i]

        # Ignore lines that don't start a turn
        if '<lturn' in line:

            # Get the turn id
            try:  # Subturn
                turn = line.split('id=')[1].split('>')[0].split(' ')[0].replace("'", "")
            except:  # Normal turn
                turn = line.split('id=')[1].split('>')[0].replace("'", "")

            segments = []
            # Loop and get utterance segments till we find another turn
            while '</lturn' not in line:
                i += 1
                line = da_file[i]

                if '<segment' in line:
                    segment = {}
                    # Get sp-act from segment
                    da = line.split(' ')[2].split('sp-act=')[1].replace("'", "")
                    segment['da'] = da
                    # Get type from segment
                    # type = line.split(' ')[1].split('type=')[1].replace("'", "")

                    # Get the start and end unit (word) id's for this utterance
                    next_line = da_file[i + 1]
                    start_id = next_line.split("(")[1].split(")")[0]
                    stop_id = next_line.split("(")[-1][:-1].split(")")[0]
                    segment['start_id'] = start_id
                    segment['stop_id'] = stop_id
                    segments.append(segment)

            turn_segments[turn] = segments
    return turn_segments


def get_words(words_file, start_id, stop_id):
    """Gets the words from word ID's from unit.xml files."""
    words = []

    for i in range(len(words_file)):
        line = words_file[i]
        # Ignore lines that don't have a word
        if line.split(" ")[0] not in ['<word', '<phonword']:
            continue
        line_id = line.split('id=')[1].split('>')[0].replace('"', '')

        # Find the first word
        if start_id == line_id:
            word = line.split('id=')[1].split('>')[1].split('<')[0]
            words.append(word)

            # Loop till we find the last word
            while stop_id != line_id:
                i += 1
                line = words_file[i]
                try:  # Valid ID
                    line_id = line.split('id=')[1].split('>')[0].replace('"', '')
                except:  # End of file
                    break
                # Ignore lines that don't have a word
                if line.split(" ")[0] not in ['<word', '<phonword']:
                    continue
                word = line.split('id=')[1].split('>')[1].split('<')[0]
                words.append(word)

    return words
