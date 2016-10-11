import hug
import sections
import cards

api = hug.get(on_invalid=hug.redirect.not_found)

api = hug.API(__name__)
hug.get('/getSections', api=api)(sections.getSections)
hug.get('/getCards', api=api)(cards.getCards)
