import module as script
import requests

class TestParsing:
    stopword = 'afin a ailleurs oxford'
    localisation_numero = 'wer ewr 9 rue las cases'
    localisation = 'asd asd boulevard saint germain'
    majuscule = 'la super ville que je vois est Paris'



##
##unit tests for object parsing.
##

#unit tests for attributes
    def test_get_msg_stopword(self):
        question = script.parsing(self.stopword)
        assert question.new_sentence == ['oxford']

    def test_get_msg_localisation_numero(self):
        #msg = ('wer ewr 9 rue las cases')
        question = script.parsing(self.localisation_numero)
        assert question.placeToSearch == ['9','rue','las','cases']

    def test_get_msg_localisation(self):
        #msg = ('asd asd boulevard saint germain')
        question = script.parsing(self.localisation)
        assert question.placeToSearch == ['boulevard','saint','germain']

    def test_get_msg_majuscule(self):
        #msg = ('la super ville que je vois est Paris')
        question = script.parsing(self.majuscule)
        assert question.placeToSearch == ['Paris']

    ##unit test for method "google" for object parsing

    def test_google_url(self):
        #msg = ('wer ewr 9 rue las cases')
        question = script.parsing(self.localisation_numero)
        assert question.google() == 'https://maps.googleapis.com/maps/api/staticmap?center=9+rue+las+cases&zoom=14&size=400x400&markers=9+rue+las+cases&key=AIzaSyD5nqmDGFH1SUZxJAYVtFHP7RNjjFE9CHg'


    ##unit test for method "wiki" for object parsing

    def test_wiki_url(self):
        #msg = ('wer ewr 9 rue las cases')
        question = script.parsing(self.localisation_numero)
        assert question.wiki() == 'https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=9%20rue%20las%20cases&formatversion=2&prop=revisions&rvprop=content&format=json&formatversion=2'

