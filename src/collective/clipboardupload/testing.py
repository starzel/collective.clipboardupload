from Products.CMFCore.utils import getToolByName
from plone.testing import z2
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import PLONE_FIXTURE


class ClipboarduploadtLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.clipboardupload
        self.loadZCML(package=collective.clipboardupload)

    def setUpPloneSite(self, portal):
        workflowTool = getToolByName(portal, 'portal_workflow')
        workflowTool.setDefaultChain('simple_publication_workflow')

COLLECTIVE_CLIPBOARDUPLOAD_FIXTURE = ClipboarduploadtLayer()
COLLECTIVE_CLIPBOARDUPLOAD_ROBOT_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_CLIPBOARDUPLOAD_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER),
    name="collective.clipboardupload:Robot")
COLLECTIVE_CLIPBOARDUPLOAD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_CLIPBOARDUPLOAD_FIXTURE,),
    name="collective.clipboardupload:Functional")
