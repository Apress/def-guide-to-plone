#!/usr/bin/python
#$Id: import.py,v 1.1 2004/06/07 19:23:33 andy Exp $
#Copyright: Enfold Systems
#License: http://www.enfoldsystems.com

# this requires Python 2.3
import csv

# change this file name to be local on your computer
# note that you have to use the full path so this could be
# "/var/zope/Products/PloneBookExamples/Extensions/test.csv"
# or
# r"c:\Program Files\Plone2\Data\Products\PloneBookExamples\Extensions\test.csv"
fileName = "/var/zope.zeo/Extensions/test.csv"

def importUsers(self):
    reader = csv.reader(open(fileName, "r"))
    pm = self.portal_membership
    pr = self.portal_registration 
    pg = self.portal_groups
    out = []
    ignoreLine = 1
    
    for row in reader:
        # ignore blank lines
        if not row: continue

        if ignoreLine:
            continue
            ignoreLine = 0
        
        # check we have exactly 4 items 
        assert len(row) == 4
        id, name, email, groups = row

        password = pr.generatePassword()
   
        try: 
            pr.addMember(id = id,
                password = password,
                roles = ["Member",],
                properties = {
                    'fullname': name,
                    'username': id,
                    'email': email,
                    }
                )
            for groupId in groups.split(','):
                group = pg.getGroupById(groupId)
                group.addMember(id)
        
            out.append("Added user %s" % id)
                
        except ValueError:
            out.append("Skipped %s" % id)
            
    return "\n".join(out)            
