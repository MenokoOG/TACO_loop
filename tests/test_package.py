import re

import taco_loop


def test_version_is_semver() -> None:
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", taco_loop.__version__)
