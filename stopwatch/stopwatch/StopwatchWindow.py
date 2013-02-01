# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('stopwatch')

import gtk
import logging
logger = logging.getLogger('stopwatch')

from stopwatch_lib import Window
from stopwatch.AboutStopwatchDialog import AboutStopwatchDialog
from stopwatch.PreferencesStopwatchDialog import PreferencesStopwatchDialog

# See stopwatch_lib.Window.py for more details about how this class works
class StopwatchWindow(Window):
    __gtype_name__ = "StopwatchWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(StopwatchWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutStopwatchDialog
        self.PreferencesDialog = PreferencesStopwatchDialog

        # Code for other initialization actions should be added here.

