from uzwords import uzbek_words
import random





def get_word(words = uzbek_words) :

    new_word = random.choice(words)
    return new_word

new_word = get_word()
print(new_word)



def new_word_list(new_word1 = new_word) :
    new_dic = []
    for harf in new_word1 :
        new_dic += harf
    return new_dic
word_list = new_word_list()
print(new_word_list())





























































