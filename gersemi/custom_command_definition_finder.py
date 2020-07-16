from lark import Discard
from lark.visitors import Interpreter, Transformer
from gersemi.ast_helpers import is_keyword
from gersemi.keywords import Keywords


class DropIrrelevantElements(Transformer):  # pylint: disable=too-few-public-methods
    def _discard(self, _):
        raise Discard

    NEWLINE = _discard
    line_comment = _discard
    bracket_comment = _discard
    non_command_element = _discard


is_parse_argv = is_keyword("PARSE_ARGV")


class CMakeInterpreter(Interpreter):
    def __init__(self, stack=None):
        self.stack = dict() if stack is None else stack
        self.found_commands = dict()

    @property
    def _inner_scope(self):
        return type(self)(stack=self.stack.copy())

    def _eval_variables(self, arg):
        for name, value in self.stack.items():
            arg = arg.replace(f"${{{name}}}", ";".join(value))
        return arg.split(";")

    def _set(self, arguments):
        name, *values = self.visit_children(arguments)
        self.stack[name] = [
            item for value in values for item in self._eval_variables(value)
        ]

    def _new_command(self, arguments):
        if len(arguments.children) > 0:
            name = arguments.children[0]
            return self.visit(name)
        raise RuntimeError

    def _cmake_parse_arguments(self, arguments):
        if is_parse_argv(arguments.children[0]):
            keywords = arguments.children[3:6]
        else:
            keywords = arguments.children[1:4]

        options, one_value_keywords, multi_value_keywords = [
            self._eval_variables(self.visit(item)) for item in keywords
        ]
        return Keywords(options, one_value_keywords, multi_value_keywords)

    def start(self, tree):
        return self.visit(tree.children[0])

    def file(self, tree):
        self.visit_children(tree)
        return self.found_commands

    def block(self, tree):
        subinterpreter = self._inner_scope
        block_begin, *body, _ = subinterpreter.visit_children(tree)
        name, *_ = block_begin
        if name is None:
            return

        keywords, *_ = body
        if len(keywords) > 0:
            self.found_commands[name.lower()] = keywords[0]

    def block_body(self, tree):
        return [
            item for item in self.visit_children(tree) if isinstance(item, Keywords)
        ][:1]

    def command_invocation(self, tree):
        identifier, arguments = tree.children
        command_interpreters = {
            "cmake_parse_arguments": self._cmake_parse_arguments,
            "function": self._new_command,
            "macro": self._new_command,
            "set": self._set,
        }
        return command_interpreters.get(identifier, lambda *args: None)(arguments)

    def _join(self, tree):
        return "".join(self.visit_children(tree))

    def complex_argument(self, tree):
        return f"({self.visit_children(tree)})"

    def _extract_first(self, tree):
        return tree.children[0]

    def quoted_argument(self, tree):
        return tree.children[0] if tree.children else ""

    bracket_argument = _join
    commented_argument = _join
    unquoted_argument = _extract_first


def find_custom_command_definitions(tree):
    tree = DropIrrelevantElements(visit_tokens=True).transform(tree)
    return CMakeInterpreter().visit(tree)