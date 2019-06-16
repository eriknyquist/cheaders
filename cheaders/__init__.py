__version__ = "1.0.0"

import re
import sys
import os
import datetime


class Generator(object):
    """
    Class to generate a header (.h) file file from a C (.c) file
    """

    function_regex = ('(static\s+)?'
                      '([\w*]+[\s*]+[\w*]+\s*'
                      '\(([\w*]+[\s*]+[\w*]+,?\s*)*\)\s*\{)')

    matcher = re.compile(function_regex, re.MULTILINE)

    def __init__(self, filename, author=None, header_filename=None):
        """
        :param str filename: name of C file to generate header file for.
        :param str author: author name.
        :param str header_filename: name of header file to generate. If unset,\
            a default filename will be generated based on the C file name.
        """

        self._filename = filename
        self._year = datetime.datetime.now().year
        self._author = author

        if header_filename is None:
            self._header_filename = os.path.splitext(filename)[0] + '.h'
        else:
            self._header_filename = header_filename

        self._header_basename = os.path.basename(self._header_filename)
        self._guard_macro = self._header_basename.replace('.', '_').upper()

    def _comment_header(self):
        ret = ("/*\n * %s\n *\n * (Description here)\n"
               % self._header_basename)

        if self._author is not None:
            ret += " *\n * %s (%s)\n" % (self._author, self._year)

        ret += " *\n */\n\n\n"
        return ret

    def _function_variable_names(self, declaration):
        ret = []
        paren_depth = 1
        i = len(declaration) - 3 # Skip semicolon and closing paren

        # Get parameter declarations between parens
        while paren_depth > 0:
            if declaration[i] == ")":
                paren_depth += 1
            elif declaration[i] == "(":
                paren_depth -= 1

            i -= 1

        paramtext = declaration[i + 2: -2].strip()
        if paramtext == '':
            return ret

        params = paramtext.split(',')

        # Get the variable name out of the parameter declaration
        for param in params:
            i = len(param) - 1
            while param[i] not in " *(\n\t\v":
                i -= 1

            ret.append(param[i + 1:].strip())

        return ret

    def _doxygen_comment(self, declaration):
        is_void = declaration.startswith('void')
        params = self._function_variable_names(declaration)

        ret = ("/**\n"
               " * (Description)\n"
               " *\n")

        if params:
            longest = len(max(params, key=len))
            spaces = max(10, longest + 2)

            fmt_string = " * @param   {:<%d}(description)\n" % spaces

            for param in params:
                ret += fmt_string.format(param)

        if not is_void:
            ret += " *\n * @return  (description)\n"

        return ret + (" */\n")

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

    @property
    def header_filename(self):
        """
        Auto-generated filename for generated header file
        """
        return self._header_basename

    def generate(self, doxygen_comments=False):
        """
        Generate text for header file.

        :param bool doxygen_comments: if True, generated function declarations\
            will include doxygen comments with parameter documentation.
        :return: generated text for header file
        :rtype: str
        """

        ret = self._comment_header()
        ret += "#ifndef {0}\n#define {0}\n\n\n".format(self._guard_macro)
        declarations = self._get_nonstatic_function_declarations()

        for d in declarations:
            if doxygen_comments:
                ret += self._doxygen_comment(d)

            ret += d + "\n\n\n"

        ret += "#endif /* %s */\n" % self._guard_macro
        return ret
