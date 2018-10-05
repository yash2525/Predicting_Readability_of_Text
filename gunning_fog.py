import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import cmudict

d = cmudict.dict()

non_dictionary_words = set()


def word_syllable_count(word):
    try:
        return len([x for x in d[word.lower()][0] if x[-1].isdigit()])
    except Exception:
        non_dictionary_words.add(word)
        return 1


def complex_word_count(text):
    return len([word_syllable_count(word)
                for word in divide_into_words(text) if word_syllable_count(word) > 2])


def divide_into_words(text):
    text = re.sub(r's\'|\'s|\-|"', ' ', text)
    words = word_tokenize(text)
    return [word for word in words if re.match(r'\w+', word)]


def sentence_count(text):
    return len(sent_tokenize(text))


def gunning_fog_grade(text):
    sentences, words, complex_words = sentence_count(text), len(
        divide_into_words(text)), complex_word_count(text)
    return 0.4 * ((words / sentences) + 100 * (complex_words / words))

def gunning_fog_grade_r(text):
	d=gunning_fog_grade(text)
	message=""
	if d<7:
		message = "6th Grader+"
	elif d<8:
		message = "7th Grader+"
	elif d<9:
		message = "8th Grader+"
	elif d<10:
		message = "9th Grader+"
	elif d<11:
		message = "10th Grader+"
	elif d<12:
		message = "11th Grader+"
	elif d<13:
		message = "12th Grader+"
	elif d<14:
		message = "Collage"
	else:
		message = "Collage Graduate"
	return [str(d),message]