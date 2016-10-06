#$Id: validEmail.vpy,v 1.2 2004/06/07 19:23:33 andy Exp $
#Copyright: Enfold Systems
#License: http://www.enfoldsystems.com

email = context.REQUEST.get('email_address', None)

if not email:
    state.setError('email_address', 'An email address is required', new_status='failure')

# further validate the email address, new feature added in 2.0.3
if hasattr(context.portal_util, "validateSingleEmailAddress"):
    if not context.portal_util.validateSingleEmailAddress(email):
        state.setError('email_address', 'The email address is not valid', new_status='failure')

if state.getErrors():
    state.set(portal_status_message='Please correct the errors shown.')
    
return state
