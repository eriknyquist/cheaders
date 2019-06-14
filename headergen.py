import re
import sys

class HeaderGenerator(object):
    function_regex = r'(static\s+)?([\w*]+[\s*]+[\w*]+\s*\([\s\w*,]+\)\s*\{)'
    matcher = re.compile(function_regex, re.MULTILINE)

    def __init__(self, filename):
        self._filename = filename

    def _get_nonstatic_function_declarations(self):
        function_sigs = []

        with open(self._filename, 'r') as fh:
            for static, rest in self.__class__.matcher.findall(fh.read()):
                # Ignore static functions
                if static != '':
                    continue
                
                function_sigs.append(rest.rstrip('{').strip() + ';')
        
        return function_sigs

    def generate(self):
        function_sigs = self._get_nonstatic_function_declarations()

        for s in function_sigs:
            print s + "\n\n"

h = HeaderGenerator(sys.argv[1])
h.generate()
