from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.tag import pos_tag
from nltk.parse import DependencyGraph
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

#tokenizajca tekstu

tekst = "To jest przykładowy tekst. Zawiera kilka zdań i fraz. Słoń patrzy na słońce. Chrząsz brzmi w trzcinie w Szczebrzeszynie."

sentence = sent_tokenize(tekst)
print(f"zdania: {sentence}")

words = word_tokenize(tekst)
print(f"słowa: {words}")

#rozpoznawanie części mowy
tagged_words = pos_tag(words)
print(f"tagi części mowy: {tagged_words}")

#analiza składniowa
# dep_graph = DependencyGraph("".join(words),top_relation_label='root')
# print("Analiza składniowa")
# print(dep_graph.tree())

stemer = SnowballStemmer("english")
lematier = WordNetLemmatizer()

word = "developping"
print(f'Stemer: {word}')

lemmat_w = lematier.lemmatize(word)
print(f"Lematyzacja: {lemmat_w}")
