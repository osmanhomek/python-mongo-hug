import hug
import sections
import cards

api = hug.get(on_invalid=hug.redirect.not_found)

api = hug.API(__name__)
hug.get('/getSections/{id}', api=api)(sections.getSections)
hug.get('/getUnviewedCards/{id}/{pid}', api=api)(cards.getUnviewedCards)
hug.get('/insViewedCard/{id}/{pid}', api=api)(cards.insViewedCard)