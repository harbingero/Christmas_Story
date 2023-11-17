import os
import re
import random

overwrite = True
writing = False
deviate = 5
story_file_name = "Twas_a_Christmas_Story.txt"
homeDir = "C:\\Users\\jgask\\Documents\\Personal\\Christmas2023"
stories = os.listdir(homeDir)
punctuation = [',', '.', "'", ';', '!', '-', '’', '“', '?', '”', '"', ':', '…', '(', ')', '[', ']', 'è']
re_punctuation = '[\.,\';!-’\"?\":…\(\)\[\]è]' #work on setting up no punctuation at the end of a word for the word game.
punc = '[\.,\';!/\[\]]'
letters = "[a-zA-Z0-9\\s]"
line_count = 0
story_lines = []
story_sum = 0
story_collection = []
final_story_location = os.path.join(os.getcwd(), story_file_name)
neglected_lines = []
final_story_length = 0
noun = []
verb = []
adverb = []
pronoun = []
spill = []
number_list = []

for i in range(0, 1000):
    number_list.append(i)

for story in stories:
    story_line_count = 0
    file = os.path.join(homeDir, story)
    with open(file, "r", encoding="utf8") as f:
        for line in f:
            if len(line.rstrip()) > 0:
                line_count += 1
                story_line_count += 1
                story_collection.append(line.rstrip())
    story_lines.append(story_line_count)
for count in story_lines:
    story_sum += count
story_average = story_sum//len(story_lines)
deviation = story_average//deviate
final_deviation = random.randint(0-deviation, deviation)
project_lines = story_average - final_deviation

if final_story_location and overwrite:
    with open(final_story_location, "w") as f:
        pass

with open(final_story_location, "r") as f:
    for line in f:
        final_story_length += 1


def random_line(total_lines):
    line_number = random.randint(0, total_lines-1)
    return line_number

#Writes the story if the variable at the top is True
if writing:
    while final_story_length < project_lines:
        append_line_number = random_line(line_count)
        if append_line_number not in neglected_lines:
            neglected_lines.append(append_line_number)
            final_story_length += 1
            with open(final_story_location, "a", encoding="utf8") as f:
                f.write(story_collection[append_line_number].lstrip() + "\n")

word_list = []
for line in story_collection:
    appendable_word = ""
    for letter in line.lstrip():
        if letter == " ":
            word_list.append(appendable_word)
            appendable_word = ""
        else:
            appendable_word += letter


def request_numberical_input(word, types):
    numeral = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    console_request = ""
    restart = False
    check = ""
    total_checks = 5
    for number in range(len(types)):
        console_request += "Type " + str(number) + " for " + str(types[number]) + ".  "
    console_request = "The word is '" + word + "'.\n" + console_request
    if len(types) < total_checks:
        print("\t\tRead which numbers are which word.  You they are not standard.")
    while len(check) < 1:
        check = input(console_request)
    if check not in numeral:
        restart = True
    if len(check) < 1:
        restart = True
    if -1 > int(check) > len(types):
        restart = True
    if restart:
        request_numberical_input(word, types)
    if not restart:
        return check


testing_number = 20
tested_itterations = 0
noun = ['child', 'peace', 'angels', 'hours', 'Hill', 'vale', 'vigil', 'moon', 'world', 'Angels', 'forebodings', 'alarm', 'Villagers', 'doors', 'wind', 'snow', 'cold', 'fingers', 'fire', 'night']
verb = ['Sleep', 'will', 'slumber', 'watch', 'Breathes', 'close', 'disarm', 'harm', 'Let', 'open', 'follow,', 'draw', 'shall', 'stamping']
adverb = ['gently', 'will']
pronoun = ['will', 'your', 'yours', 'we']
spill = ['All', 'the', 'my', 'through', 'While', 'thy', 'of', 'pure', 'holy', 'ever', 'all', 'no', 'this', 'in', 'to', 'from', 'away', 'by', 'we', 'you', 'For', 'one', 'Sudden']
actively_tested = 85
attempts = 2
for word in word_list:
    if tested_itterations < actively_tested:
        tested_itterations += 1
        continue
    total_types = []
    type_names = []
    temp_word = re.sub("[^0-9a-zA-Z]+", "*", )
    if word not in noun and word not in spill:
        total_types.append(noun)
        type_names.append("noun")
    if word not in verb and word not in spill:
        total_types.append(verb)
        type_names.append("verb")
    if word not in adverb and word not in spill:
        total_types.append(adverb)
        type_names.append("adverb")
    if word not in pronoun and word not in spill:
        total_types.append(pronoun)
        type_names.append("pronoun")
    if word not in spill:
        total_types.append(spill)
        type_names.append("spill")
    if len(total_types) > 1:
        total_types[int(request_numberical_input(word, type_names))].append(word)
    actively_tested += 1
    print("noun =", noun)
    print("verb =", verb)
    print("adverb =", adverb)
    print("pronoun =", pronoun)
    print("spill =", spill)
    print("actively_tested =", actively_tested)
    if len(noun) > testing_number * attempts:
        break
print(attempts + 1)






#I am attempting to create a list of characters that are just punctuation
# for story in stories:
#     file = os.path.join(homeDir, story)
#     with open(file, "r", encoding="utf8") as f:
#         for line in f:
#             for letter in line.rstrip():
#                 if not re.search(letters, letter):
#                     if letter not in punctuation:
#                         punctuation.append(letter)
# print(punctuation)
