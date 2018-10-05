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


def syllable_count(text):
    return sum(word_syllable_count(word) for word in divide_into_words(text))


def divide_into_words(text):
    text = re.sub(r's\'|\'s|\-|"', ' ', text)
    words = word_tokenize(text)
    return [word for word in words if re.match(r'\w+', word)]


def sentence_count(text):
    return len(sent_tokenize(text))


def flesch_kincaid_score(text):
    sentences, words, syllables = sentence_count(text), len(divide_into_words(
        text)), syllable_count(text)
    return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)


def flesch_kincaid_grade(text):
    sentences, words, syllables = sentence_count(text), len(divide_into_words(
        text)), syllable_count(text)
    return 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59

def flesch_kincaid_score_r(text):
	d=flesch_kincaid_score(text)
	message=""
	if d>=90:
		message = "Very easy to read. Easily understood by an average 11-year-old student.5th Grader+"
	elif d>=80:
		message = "Easy to read. Conversational English for consumers.6th Grader+"
	elif d>=70:
		message = "Fairly easy to read.7th Grader+"
	elif d>=60:
		message = "Plain English. Easily understood by 13- to 15-year-old students.8th & 9th grade+"
	elif d>=50:
		message = "Fairly difficult to read.10th to 12th grade+"
	elif d>=30:
		message = "Difficult to read.Collage student"
	else:
		message = "Very difficult to read. Best understood by university graduates."
	return [str(d),message]

def flesch_kincaid_grade_r(text):
	d=flesch_kincaid_grade(text)
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

