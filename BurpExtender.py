"""
Burp Suite extension template for Python (Jython) using the Extender API.

Load in Burp: Extensions > Installed > Add > Select file > BurpExtender.py
Reload during development: Ctrl/Cmd + click the Loaded checkbox.

Notes:
- Burp runs this on Jython 2.7, so the code must stay Python 2.7-compatible.
- The `burp` module is provided by Burp; do not try to import it from a path.
"""

from burp import IBurpExtender, IContextMenuFactory, ITab
from javax.swing import JLabel, JMenuItem, JPanel


class BurpExtender(IBurpExtender, IContextMenuFactory, ITab):
    """Main extension class. Must be named BurpExtender."""

    def registerExtenderCallbacks(self, callbacks):
        # Step 1: keep references and set the extension name
        self._callbacks = callbacks
        callbacks.setExtensionName("My first extension")

        # Step 2: add a context menu item
        callbacks.registerContextMenuFactory(self)

        # Step 3: add a custom tab
        callbacks.addSuiteTab(self)

    # --- IContextMenuFactory ---

    def createMenuItems(self, invocation):
        item = JMenuItem("My first context menu", actionPerformed=self._on_menu_click)
        return [item]

    def _on_menu_click(self, event):
        self._callbacks.printOutput("Hello, world!")

    # --- ITab ---

    def getTabCaption(self):
        return "My extension tab"

    def getUiComponent(self):
        panel = JPanel()
        panel.add(JLabel("Hello, world!"))
        return panel
