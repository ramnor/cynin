###############################################################################
#cyn.in is an open source Collaborative Knowledge Management Appliance that 
#enables teams to seamlessly work together on files, documents and content in 
#a secure central environment.
#
#cyn.in v2 an open source appliance is distributed under the GPL v3 license 
#along with commercial support options.
#
#cyn.in is a Cynapse Invention.
#
#Copyright (C) 2008 Cynapse India Pvt. Ltd.
#
#This program is free software: you can redistribute it and/or modify it under
#the terms of the GNU General Public License as published by the Free Software 
#Foundation, either version 3 of the License, or any later version and observe 
#the Additional Terms applicable to this program and must display appropriate 
#legal notices. In accordance with Section 7(b) of the GNU General Public 
#License version 3, these Appropriate Legal Notices must retain the display of 
#the "Powered by cyn.in" AND "A Cynapse Invention" logos. You should have 
#received a copy of the detailed Additional Terms License with this program.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of 
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
#Public License for more details.
#
#You should have received a copy of the GNU General Public License along with 
#this program.  If not, see <http://www.gnu.org/licenses/>.
#
#You can contact Cynapse at support@cynapse.com with any problems with cyn.in. 
#For any queries regarding the licensing, please send your mails to 
# legal@cynapse.com
#
#You can also contact Cynapse at:
#802, Building No. 1,
#Dheeraj Sagar, Malad(W)
#Mumbai-400064, India
###############################################################################
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ubify.policy.config import spacesdefaultaddablenonfolderishtypes


class SidepanelConversation(BrowserView):
    """Contains backend code for the Side Panel 
    """

    template = ViewPageTemplateFile('sidepanel_conversation_ff.pt')

    def __call__(self):
        self.alloweditemtypes = spacesdefaultaddablenonfolderishtypes + ('StatuslogItem',)
        return self.template()

    def isCurrentUser(self,userid):
        from AccessControl import getSecurityManager
        currentuserid = getSecurityManager().getUser().getId()
        if currentuserid.lower() == userid.lower():
            return True
        else:
            return False

    def isUserStatuslogExists(self,mtool,userid):
        result = False
        try:
            homeFolder = mtool.getHomeFolder(userid)
            objSLog = getattr(homeFolder,'statuslog')
            if objSLog <> None:
                result = True
        except AttributeError:
            pass
        return result
