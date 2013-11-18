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
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from ubify.viewlets.config import *

class SpaceRecentUpdatesViewlet(ViewletBase):

    render = ViewPageTemplateFile('space_items.pt')

    def update(self):
        self.title = "Recent Updates"
        self.display = False
        self.results = None

        self.plone_view = getMultiAdapter((self.context, self.request),name='plone')
        portal_state = getMultiAdapter((self.context, self.request),name=u'plone_portal_state')
        portal = portal_state.portal()
        portal_catalog = portal.portal_catalog

        path =  '/'.join(self.context.getPhysicalPath())

        self.limit_display = space_recent_updates_limit

        query = {'path':{'query':path},'sort_on':'modified','sort_order':'descending'}

        self.results = portal_catalog.searchResults(query)[:self.limit_display]

        #self.results = [b.getObject() for b in self.results]
