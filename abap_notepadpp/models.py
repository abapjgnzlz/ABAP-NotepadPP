"""
Data models used by the ABAP-NotepadPP generator.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Category(str, Enum):
    """Supported keyword categories."""

    STATEMENT = "statement"
    CONTROL = "control"
    EXPRESSION = "expression"
    TYPE = "type"

    OPEN_SQL = "open_sql"

    CDS = "cds"

    RAP = "rap"

    AMDP = "amdp"

    ABAP_CLOUD = "abap_cloud"

    BUILTIN = "builtin"

    CLASS = "class"

    INTERFACE = "interface"

    ANNOTATION = "annotation"


@dataclass(slots=True)
class Keyword:
    """
    Represents one ABAP language element.
    """

    keyword: str

    category: Category

    since: str = ""

    group: str = ""

    description: str = ""

    deprecated: bool = False

    aliases: List[str] = field(default_factory=list)

    examples: List[str] = field(default_factory=list)

    references: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.keyword = self.keyword.strip().upper()

    @property
    def is_multiword(self) -> bool:
        """
        Returns True when the keyword contains spaces.

        Example:
            END-OF-DEFINITION
            MODIFY ENTITIES
            DEFINE VIEW ENTITY
        """
        return " " in self.keyword

    @property
    def word_count(self) -> int:
        return len(self.keyword.split())

    def to_dict(self) -> dict:
        """
        Export object as dictionary.
        """

        return {
            "keyword": self.keyword,
            "category": self.category.value,
            "since": self.since,
            "group": self.group,
            "description": self.description,
            "deprecated": self.deprecated,
            "aliases": self.aliases,
            "examples": self.examples,
            "references": self.references,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Keyword":
        """
        Creates a Keyword object from a dictionary.
        """

        return cls(
            keyword=data["keyword"],
            category=Category(data["category"]),
            since=data.get("since", ""),
            group=data.get("group", ""),
            description=data.get("description", ""),
            deprecated=data.get("deprecated", False),
            aliases=data.get("aliases", []),
            examples=data.get("examples", []),
            references=data.get("references", []),
        )
