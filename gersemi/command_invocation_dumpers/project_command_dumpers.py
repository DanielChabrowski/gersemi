from .argument_aware_command_invocation_dumper import (
    ArgumentAwareCommandInvocationDumper,
)
from .command_with_property_value_pairs_dumper import (
    CommandWithPropertyValuePairsDumper,
)
from .multiple_signature_command_invocation_dumper import (
    MultipleSignatureCommandInvocationDumper,
)


class AddCustomCommandCommandDumper(MultipleSignatureCommandInvocationDumper):
    customized_signatures = {
        "OUTPUT": dict(
            options=["VERBATIM", "APPEND", "USES_TERMINAL", "COMMAND_EXPAND_LISTS"],
            one_value_keywords=[
                "MAIN_DEPENDENCY",
                "WORKING_DIRECTORY",
                "COMMENT",
                "DEPFILE",
                "JOB_POOL",
            ],
            multi_value_keywords=[
                "OUTPUT",
                "COMMAND",
                "ARGS",
                "DEPENDS",
                "BYPRODUCTS",
                "IMPLICIT_DEPENDS",
            ],
        ),
        "TARGET": dict(
            options=[
                "PRE_BUILD",
                "PRE_LINK",
                "POST_BUILD",
                "VERBATIM",
                "USES_TERMINAL",
                "COMMAND_EXPAND_LISTS",
            ],
            one_value_keywords=["TARGET", "WORKING_DIRECTORY", "COMMENT"],
            multi_value_keywords=["COMMAND", "ARGS", "BYPRODUCTS"],
        ),
    }


class AddCustomTargetCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = ["ALL", "VERBATIM", "USES_TERMINAL", "COMMAND_EXPAND_LISTS"]
    one_value_keywords = ["WORKING_DIRECTORY", "COMMENT", "JOB_POOL"]
    multi_value_keywords = ["COMMAND", "DEPENDS", "BYPRODUCTS", "SOURCES"]


class AddTestCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = ["COMMAND_EXPAND_LISTS"]
    one_value_keywords = ["NAME", "WORKING_DIRECTORY"]
    multi_value_keywords = ["COMMAND", "CONFIGURATIONS"]


class BuildCommandCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["CONFIGURATION", "TARGET", "PROJECT_NAME"]


class CreateTestSourcelistCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["EXTRA_INCLUDE", "FUNCTION"]


class DefinePropertyCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = [
        "GLOBAL",
        "DIRECTORY",
        "TARGET",
        "SOURCE",
        "TEST",
        "VARIABLE",
        "CACHED_VARIABLE",
        "INHERITED",
    ]
    one_value_keywords = ["PROPERTY"]
    multi_value_keywords = ["BRIEF_DOCS", "FULL_DOCS"]


class ExportCommandDumper(MultipleSignatureCommandInvocationDumper):
    customized_signatures = {
        "EXPORT": dict(one_value_keywords=["EXPORT", "NAMESPACE", "FILE"]),
        "TARGETS": dict(
            options=["APPEND", "EXPORT_LINK_INTERFACE_LIBRARIES"],
            one_value_keywords=["NAMESPACE", "FILE", "ANDROID_MK"],
            multi_value_keywords=["TARGETS"],
        ),
        "PACKAGE": dict(one_value_keywords=["PACKAGE"]),
    }


class IncludeExternalMsProjectCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["TYPE", "GUID", "PLATFORM"]


class LinkLibrariesCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["debug", "optimized", "general"]


class LoadCacheCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["READ_WITH_PREFIX"]
    multi_value_keywords = ["EXCLUDE", "INCLUDE_INTERNALS"]


class ProjectCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["VERSION", "DESCRIPTION", "HOMEPAGE_URL"]
    multi_value_keywords = ["LANGUAGES"]


class SourceGroupCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["REGULAR_EXPRESSION", "TREE", "PREFIX"]
    multi_value_keywords = ["FILES"]


class TargetCompileDefinitionsCommandDumper(ArgumentAwareCommandInvocationDumper):
    multi_value_keywords = ["INTERFACE", "PUBLIC", "PRIVATE"]


class TargetCompileFeaturesCommandDumper(ArgumentAwareCommandInvocationDumper):
    multi_value_keywords = ["INTERFACE", "PUBLIC", "PRIVATE"]


class TargetCompileOptionsCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = ["BEFORE"]
    multi_value_keywords = ["INTERFACE", "PUBLIC", "PRIVATE"]


class TargetIncludeDirectoriesCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = ["BEFORE", "SYSTEM"]
    multi_value_keywords = ["INTERFACE", "PUBLIC", "PRIVATE"]


class TargetLinkDirectoriesCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = ["BEFORE"]
    multi_value_keywords = ["INTERFACE", "PUBLIC", "PRIVATE"]


class TargetLinkOptionsCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = ["BEFORE"]
    multi_value_keywords = ["INTERFACE", "PUBLIC", "PRIVATE"]


class TargetPrecompileHeadersCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["REUSE_FROM"]
    multi_value_keywords = ["INTERFACE", "PUBLIC", "PRIVATE"]


class TargetSourcesCommandDumper(ArgumentAwareCommandInvocationDumper):
    multi_value_keywords = ["INTERFACE", "PUBLIC", "PRIVATE"]


class TryRunCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = [
        "COMPILE_OUTPUT_VARIABLE",
        "RUN_OUTPUT_VARIABLE",
        "OUTPUT_VARIABLE",
    ]
    multi_value_keywords = [
        "CMAKE_FLAGS",
        "COMPILE_DEFINITIONS",
        "LINK_OPTIONS",
        "LINK_LIBRARIES",
        "ARGS",
    ]


project_command_mapping = {
    "add_custom_command": AddCustomCommandCommandDumper,
    "add_custom_target": AddCustomTargetCommandDumper,
    "add_test": AddTestCommandDumper,
    "build_command": BuildCommandCommandDumper,
    "create_test_sourcelist": CreateTestSourcelistCommandDumper,
    "define_property": DefinePropertyCommandDumper,
    "export": ExportCommandDumper,
    "include_external_msproject": IncludeExternalMsProjectCommandDumper,
    "link_libraries": LinkLibrariesCommandDumper,
    "load_cache": LoadCacheCommandDumper,
    "project": ProjectCommandDumper,
    "source_group": SourceGroupCommandDumper,
    "set_source_files_properties": CommandWithPropertyValuePairsDumper,
    "set_target_properties": CommandWithPropertyValuePairsDumper,
    "set_tests_properties": CommandWithPropertyValuePairsDumper,
    "target_compile_definitions": TargetCompileDefinitionsCommandDumper,
    "target_compile_features": TargetCompileFeaturesCommandDumper,
    "target_compile_options": TargetCompileOptionsCommandDumper,
    "target_include_directories": TargetIncludeDirectoriesCommandDumper,
    "target_link_directories": TargetLinkDirectoriesCommandDumper,
    "target_link_options": TargetLinkOptionsCommandDumper,
    "target_precompile_headers": TargetPrecompileHeadersCommandDumper,
    "target_sources": TargetSourcesCommandDumper,
    "try_run": TryRunCommandDumper,
}
