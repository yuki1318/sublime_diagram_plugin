from sublime_plugin import TextCommand
from sublime import message_dialog, error_message, version
try:
    from .diagram import setup, process, g_output
except ValueError:
    from diagram import setup, process, g_output

class DisplayDiagrams(TextCommand):
    def run(self, edit, output):
        g_output.g_output = output
        print("Processing diagrams in %r..." % self.view)
        if not process(self.view):
            error_message("No diagrams overlap selections.\n\n" \
                "Nothing to process.")

    def isEnabled(self):
        return True


if version()[0] == '2':
    setup()
else:
    def plugin_loaded():
        """Sublime Text 3 callback to do after-loading initialization"""
        try:
            setup()
        except Exception:
            error_message("Unable to load diagram plugin, check console "
                "for details.")
            raise
