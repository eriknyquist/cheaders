import re
import sys
import datetime

print daetime.now().year

class HeaderGenerator(object):
    function_regex = ('(static\s+)?'
                      '([\w*]+[\s*]+[\w*]+\s*'
                      '\(([\w*]+[\s*]+[\w*]+,?\s*)+\)\s*\{)')

    matcher = re.compile(function_regex, re.MULTILINE)

    def __init__(self, filename):
        self._filename = filename

    def _get_nonstatic_function_declarations(self):
        function_sigs = []

        with open(self._filename, 'r') as fh:
            for match in self.__class__.matcher.findall(fh.read()):
                # Ignore static functions
                if match[0] != '':
                    continue
                
                # Strip opening brace and add semicolon
                function_sigs.append(match[1].rstrip('{').strip() + ';')
        
        return function_sigs

    def generate(self):
        function_sigs = self._get_nonstatic_function_declarations()

        for s in function_sigs:
            print s + "\n\n"

h = HeaderGenerator(sys.argv[1])
h.generate()
