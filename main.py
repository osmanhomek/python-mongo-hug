import hug
import sections
import cards

api = hug.get(on_invalid=hug.redirect.not_found)

api = hug.API(__name__)
hug.get('/getSections/{aid}', api=api)(sections.getSections)
hug.get('/getUnviewedCards/{uid}/{aid}/{sid}', api=api)(cards.getUnviewedCards)
hug.get('/getViewedCards/{uid}/{aid}/{sid}', api=api)(cards.getViewedCards)
hug.get('/insViewedCard/{uid}/{aid}/{sid}/{cid}', api=api)(cards.insViewedCard)

    