#!/usr/bin/python
#$Id: sendEmail.cpy,v 1.3 2004/06/07 19:23:33 andy Exp $
#Copyright: Enfold Systems
#License: http://www.enfoldsystems.com

mhost = context.MailHost
emailAddress = context.REQUEST.get('email_address')
administratorEmailAddress = context.email_from_address
comments = context.REQUEST.get('comments')

# the message format, %s will be filled in from data
message = """
From: %s
To: %s
Subject: Website Feedback

%s

URL: %s
"""

# format the message
message = message % (
    emailAddress, 
    administratorEmailAddress,
    comments,
    context.absolute_url())

print message
print unicode(message)
mhost.send(unicode(message))

screenMsg = "Comments sent, thank you."
state.setKwargs( {'portal_status_message':screenMsg} )
return state
