"""
Repository for loading ABAP keywords from YAML files.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import yaml

from .config import KEYWORDS_DIR
from .models import Keyword


class KeywordRepository:
    """
    Loads all keyword definitions from the keywords directory.
    """

    def __init__(self, directory: Path | None = None):

        self.directory = directory or KEYWORDS_DIR

    def load(self) -> list[Keyword]:
        """
        Load every *.yml and *.yaml file.
        """

        keywords: list[Keyword] = []

        for file in self._yaml_files():

            keywords.extend(self._load_file(file))

        keywords.sort(key=lambda k: k.keyword)

        return keywords

    def _yaml_files(self) -> Iterable[Path]:

        patterns = ("*.yml", "*.yaml")

        files: list[Path] = []

        for pattern in patterns:
            files.extend(self.directory.rglob(pattern))

        return sorted(files)

    def _load_file(self, file: Path) -> list[Keyword]:

        with file.open(
            "r",
            encoding="utf-8",
        ) as stream:

            data = yaml.safe_load(stream)

        if data is None:
            return []

        if not isinstance(data, list):

            raise TypeError(
                f"{file} must contain a YAML list."
            )

        result: list[Keyword] = []

        for row in data:

            if not isinstance(row, dict):

                raise TypeError(
                    f"Invalid record in {file}"
                )

            result.append(
                Keyword.from_dict(row)
            )

        return result

    def count(self) -> int:
        """
        Returns the number of loaded keywords.
        """

        return len(self.load())
