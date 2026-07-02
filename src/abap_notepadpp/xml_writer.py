"""
XML writer for Notepad++ User Defined Language (UDL).

This module converts the internal keyword database into a Notepad++
User Defined Language XML file.
"""

from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET

from .models import Keyword


class XMLWriter:
    """
    Writes a Notepad++ UDL XML file.
    """

    def write(
        self,
        keywords: list[Keyword],
        output_file: Path,
    ) -> None:

        root = ET.Element(
            "NotepadPlus"
        )

        user_lang = ET.SubElement(
            root,
            "UserLang",
            name="ABAP S/4HANA 2023",
            ext="abap",
        )

        keyword_lists = ET.SubElement(
            user_lang,
            "KeywordLists",
        )

        statements = [
            keyword.keyword
            for keyword in keywords
        ]

        ET.SubElement(
            keyword_lists,
            "Keywords",
            name="Keywords1",
        ).text = " ".join(sorted(statements))

        ET.SubElement(
            user_lang,
            "Settings",
        )

        ET.SubElement(
            user_lang,
            "Styles",
        )

        tree = ET.ElementTree(root)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        tree.write(
            output_file,
            encoding="utf-8",
            xml_declaration=True,
        )