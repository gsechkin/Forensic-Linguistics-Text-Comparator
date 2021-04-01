import math

def stem(s):
    """returns the stem of the string s
    """
    short_words = {'is': 'is', 'the': 'the','he': 'he', 'she': 'she', \
                   'my': 'my', }
    if s in short_words:
        return s
    if s[-1] == 's':
        s = s[:-1]
    special_cases = {'children': 'child', 'doing': 'do', 'did': 'do', \
                     'string': 'string', 'spring': 'spring'}
    if s in special_cases:
        return special_cases[s]
    if s[-1] == 'e':
        s = s[:-1]
    if s[-3:] == 'ing' and len(s) > 5:
        if s[-5:-3] == 'mm' or s[-5:-3] == 'tt':
            s = s[-4]
        else:
            s = s[:-3]
    if s[-1] == 'y':
        s = s[:-1] + 'i'
    elif s[-2:] == 'er' and len(s) > 4:
        if s[-4:-2] == 'mm' or s[-4:-2] == 'tt':
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-2:] == 'ed' and len(s) > 4:
        if s[-4:-2] == 'mm' or s[-4:-2] == 'tt':
            s = s[:-3]
        else:
            s = s[:-2]
    return s
        
    
def clean_text(txt):
    """takes a string as a parameter and returns a list containing the words
       in text after they have been cleaned individually
    """
    s = ''
    for c in txt:
        if c != '.' and c != ',' and c != '!' and c != '?':
            s += c
    s = s.lower().split()
    return s


def count_sentences(txt):
    """takes a string as a parameter and returns a list of the index of the 
       start of each setence
    """
    lst = [0]
    for i in range(len(txt)):
        if txt[i] == '.' or txt[i] == '?' or txt[i] == '!':
            if i + 2 < len(txt):
                lst += [i + 2]
    return lst
            

def find_sentence_length(s):
    """takes a string as a parameter and returns the number of words by 
       counting the spaces. If it reaches the end of the sentence, it forces
       the function to return count early
    """
    count = 1
    for c in s:
        if c == ' ':
            count += 1
        elif c == '.' or c == '?' or c == '!':
            return count
    return count

def count_commas(txt):
    """takes a string as a parameter and retusn the number of commas
    """
    
    count = 0
    for c in txt:
        if c == ',':
            count += 1
    return count

def count_colons(txt):
    """takes a string as a parameter and retusn the number of colons
    """
    
    count = 0
    for c in txt:
        if c == ':':
            count += 1
    return count

def count_semi_colons(txt):
    """takes a string as a parameter and retusn the number of semicolons
    """
    
    count = 0
    for c in txt:
        if c == ';':
            count += 1
    return count

def count_periods(txt):
    """takes a string as a parameter and retusn the number of periods
    """
    count = 0
    for c in txt:
        if c == '.':
            count += 1
    return count

def count_questions(txt):
    """takes a string as a parameter and retusn the number of question marks
    """
    count = 0
    for c in txt:
        if c == '?':
            count += 1
    return count

def count_parentheses(txt):
    """takes a string as a parameter and retusn the number of parentheses
    """
    count = 0
    for c in txt:
        if c == '(':
            count += 1
    return count

def count_dashes(txt):
    """takes a string as a parameter and retusn the number of dashes
    """
    count = 0
    for c in txt:
        if c == '-':
            count += 1
    return count

def count_exclamations(txt):
    """takes a string as a parameter and retusn the number of ! marks
    """
    count = 0
    for c in txt:
        if c == '!':
            count += 1
    return count

def compare_dictionaries(d1, d2):
    """takes two dictionaries as inputs and returns their log sim score
    """
    score = 0
    total = 0
    for key in d1:
       total += d1[key]
    for item in d2:
        if item in d1:
            score += d2[item] * math.log(d1[item]/total)
        else:
            score += d2[item] * math.log(0.5/total)
    return score
            

class TextModel:
    """blueprint for objects that model a body of text
    """
    def __init__(self, model_name):
        """constructor that accepts a string as a parameter and initializes
           names, words, and wordlength attributes
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation = {}
        
    
    def __repr__(self):
        """returns a string with the name of the model as well as the sizes of
           the dictonaries for each feature of the text
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths))\
        + '\n'
        s += '  number of punctuation types: ' + str(len(self.punctuation))
        return s
    def add_string(self, s):
        """analyzes the string txt and adds its pieces to all of the
           dictionaries in this text model
        """
        commas = count_commas(s)
        if ',' not in self.punctuation and commas > 0:
            self.punctuation[','] = commas
        elif ',' in self.punctuation:
            self.punctuation[','] += commas
            
        colons = count_colons(s)
        if ':' not in self.punctuation and colons > 0:
            self.punctuation[':'] = colons
        elif ':' in self.punctuation:
            self.punctuation[':'] += colons
            
        semi_colons = count_semi_colons(s)
        if ';' not in self.punctuation and semi_colons > 0:
            self.punctuation[';'] = semi_colons
        elif ';' in self.punctuation:
            self.punctuation[';'] += semi_colons
    
        periods = count_periods(s)
        if '.' not in self.punctuation and periods > 0:
            self.punctuation['.'] = periods
        elif '.' in self.punctuation:
            self.punctuation['.'] += periods
            
        questions = count_questions(s)
        if '?' not in self.punctuation and questions > 0:
            self.punctuation['?'] = questions
        elif '?' in self.punctuation:
            self.punctuation['?'] += questions
            
        parentheses = count_parentheses(s)
        if '(' not in self.punctuation and parentheses > 0:
            self.punctuation['('] = parentheses
        elif '(' in self.punctuation:
            self.punctuation['('] += parentheses
            
        dashes = count_dashes(s)
        if '-' not in self.punctuation and dashes > 0:
            self.punctuation['-'] = dashes
        elif '-' in self.punctuation:
            self.punctuation['-'] += dashes
            
        exclamations = count_exclamations(s)
        if '!' not in self.punctuation and exclamations > 0:
            self.punctuation['!'] = exclamations
        elif '!' in self.punctuation:
            self.punctuation['!'] += exclamations
        
        start_of_sent = count_sentences(s)
        for x in start_of_sent:
            sent_length = find_sentence_length(s[x:])
            if sent_length not in self.sentence_lengths:
                self.sentence_lengths[sent_length] = 1
            else:
                self.sentence_lengths[sent_length] += 1
            
        word_list = clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1
        
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        self.add_string(text)
        
    def save_model(self):
        """saves the TextModel object self by writing its various feature 
           dictionaries to files. There will be one file written for each 
           feature dictionary
        """
        filename = self.name + '_words'
        f = open(filename, 'w')     
        f.write(str(self.words))              
        f.close()
        
        filename2 = self.name + '_word_lengths'
        f = open(filename2, 'w')     
        f.write(str(self.word_lengths))              
        f.close()
        
        filename3 = self.name + '_stems'
        f = open(filename3, 'w')     
        f.write(str(self.stems))              
        f.close()
        
        filename4 = self.name + '_sentence_lengths'
        f = open(filename4, 'w')     
        f.write(str(self.sentence_lengths))              
        f.close()
        
        filename5 = self.name + '_punctuation'
        f = open(filename5, 'w')     
        f.write(str(self.punctuation))              
        f.close()
        
        
    def read_model(self):
        """reads the stored dictionaries for the called TextModel object from 
           the files and assigns them to the attributes of the called TextModel
        """
        filename = self.name + '_words'
        f = open(filename, 'r')    
        d_str = f.read()          
        f.close()
        d = dict(eval(d_str))
        self.words = d
        
        filename2 = self.name + '_word_lengths'
        f = open(filename2, 'r')    
        d2_str = f.read()          
        f.close()
        d2 = dict(eval(d2_str))
        self.word_lengths = d2
        
        filename3 = self.name + '_stems'
        f = open(filename3, 'r')    
        d3_str = f.read()          
        f.close()
        d3 = dict(eval(d3_str))
        self.stems = d3
        
        filename4 = self.name + '_sentence_lengths'
        f = open(filename4, 'r')    
        d4_str = f.read()          
        f.close()
        d4 = dict(eval(d4_str))
        self.sentence_lengths = d4
        
        filename5 = self.name + '_punctuation'
        f = open(filename5, 'r')    
        d5_str = f.read()          
        f.close()
        d5 = dict(eval(d5_str))
        self.punctuation = d5
        
    def similarity_scores(self, other):
        """computes and returns a list of log similarity scores measuring the 
           similarity of self and other – one score for each type of feature
        """
        lst = []
        word_score = compare_dictionaries(other.words, self.words)
        lst += [word_score]
        wls = compare_dictionaries(other.word_lengths, self.word_lengths)
        lst += [wls]
        stem_score = compare_dictionaries(other.stems, self.stems)
        lst += [stem_score]
        sls = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        lst += [sls]
        punc_score = compare_dictionaries(other.punctuation, self.punctuation)
        lst += [punc_score]

        return lst
    
    def classify(self, source1, source2):
        """compares the called TextModel object to two other sources and 
           determines which of the sources is closest to the called TextModel
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        for i in range(len(scores1)):
            scores1[i] = round(scores1[i], 2)
            scores2[i] = round(scores2[i], 2)
        
        print('scores for source1: ', scores1, '\n', \
              'scores for source2: ', scores2)
        num_larger1 = 0
        num_larger2 = 0
        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                num_larger1 += 1
            else:
                num_larger2 += 1
        if num_larger1 > num_larger2:
            print(self.name, 'is more likely to have come from source1')
        else:
            print(self.name, 'is more likely to have come from source2')
            
        
def test():
    """test function for classify"""
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2) 
    
def run_tests():
    """test function for the final part of the project"""
    source1 = TextModel('CS111 Syllabus')
    source1.add_file('CS111_Syllabus.txt')

    source2 = TextModel('AR Syllabus')
    source2.add_file('AR_Syllabus.txt')

    new1 = TextModel('WR120 Syllabus')
    new1.add_file('WR120_Syllabus.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('CS131 Syllabus')
    new2.add_file('CS131_Syllabus.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('My Paper 2 for WR120')
    new3.add_file('WR_Paper_2.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('CS111 PS9PR0')
    new4.add_file('ps9pr0.txt')
    new4.classify(source1, source2)
