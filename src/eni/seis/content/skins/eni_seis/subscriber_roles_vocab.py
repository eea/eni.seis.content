
## Script (Python) "subscriber_roles_vocab"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=key_based=False
##title=get subscriber roles vocabulary
##
terms = context.portal_vocabularies.getVocabularyByName(
    'subscriber_roles').items()
res = [(t[0], t[1].title) for t in terms]

return res
