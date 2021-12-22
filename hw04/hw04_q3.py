# Shivali Mukherji
# mukhe105
# CSCI 1133 Section 070
# Assignment 4

PUN_CHARS = '[(.,;:\")]/]!?\n'
IGNORE_FILE = 'data/ignore_words.txt'

def remove_punctuation_and_lower(word):

  ''' removing punctuations in string using loop + punc. '''

  clean_str = ''
  for char in word:
    if char in PUN_CHARS:
      clean_str = clean_str + char
  return clean_str.lower()


def get_ignored_word_list(ignore_words_filename):

  ''' get the list of ignored words from the file, remove any punctuations. '''

  ignored_list = []
  ignored_file = open(ignore_words_filename, "r")
  lines_from_ignored_file = ignored_file.readlines()
  for word in lines_from_ignored_file:
      ignored_list.append(remove_punctuation_and_lower(word))
  return ignored_list


def get_words_from_file(source_filename, ignored_words_list=[]):

  ''' get all the words from the source file excluding the ignored words. '''

  print('Getting words from:',source_filename)
  words_from_file = []
  with open(source_filename, "r") as src_fh:
    for line in src_fh:
      sentence = remove_punctuation_and_lower(line.strip())
      words_in_line = sentence.split()
      for word in words_in_line:
        if word not in ignored_words_list:
          words_from_file.append(word)
    src_fh.close()
    print(source_filename, ' contains: ', len(words_from_file), ' words')
    return words_from_file


def get_word_frequency(word_list):

  ''' makes a dictionary where the key is a word from the list word_list. '''

  print("Getting word frequency")
  word_frequency = {}
  uniq_words = set(word_list)
  print('Unique words: ', len(uniq_words))
  tracker = 1
  # Count the frequency of the words in word list
  for word in uniq_words:
    word_count = word_list.count(word)
    word_frequency[word] = word_count
    tracker += 1
    if tracker % 10000 == 0:
      print('Completed ', tracker, ' words')
  return word_frequency


def save_popular_words(word_frequency, destination_file, k=10):
  ''' gets top k most popular words based on the word_frequency
dictionary, and writes the name of the words and their frequencies in a file named
destination_file. '''

  print('Saving popular words to:',destination_file)
  # Sort word-frequency in descending order
  high_frequency_words = [(word_frequency[key], key) for key in word_frequency]
  high_frequency_words.sort(reverse=True)
  print('Reverse order sorting done, begin to write top: ', k)
  with open(destination_file, "w") as dst_fh:
        for index, value in enumerate(high_frequency_words):
            if k > 0:
                word_freq_pair = value[1] + ',' + str(value[0]) + '\n'
                dst_fh.write(word_freq_pair)
                k -= 1
  dst_fh.close()


def main():
    type_arr = ['Fake', 'True']

    for type in type_arr:
        source_file = f'data/{type}.csv'
        dest_file = f'data/{type}_words.csv'
        popular_words_file = f'data/{type}_popular_words.txt'
        
        #Process the source file and store every word on a single line dest_file
        #excluding the words in ignore_file
        ignored_words_list = get_words_from_file(IGNORE_FILE)
        word_list = get_words_from_file(source_file, ignored_words_list)
        word_frequency = get_word_frequency(word_list)

        #Save the top k most popular words
        save_popular_words(word_frequency, popular_words_file)
        
main()














