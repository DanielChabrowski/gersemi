import pytest
from gersemi.exceptions import ASTMismatch
from gersemi.sanity_checker import check_code_equivalence
from .tests_generator import generate_input_output_tests


def test_formatter(formatter, case):
    assert formatter.format(case.given) == case.expected


def test_formatter_idempotence(formatter, case):
    formatted_once = formatter.format(case.given)
    formatted_twice = formatter.format(formatted_once)
    assert formatted_once == formatted_twice


def test_abstract_syntax_tree_equivalence(parser, formatter, case):
    try:
        check_code_equivalence(parser, case.given, case.expected)
    except ASTMismatch:
        pytest.fail("ASTs mismatch")
        raise


pytest_generate_tests = generate_input_output_tests(
    where="formatter", input_extension=".in", output_extension=".out",
)
