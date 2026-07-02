"""
Validation utilities for the ABAP keyword database.
"""

from __future__ import annotations

from collections import Counter

from .models import Category, Keyword


class ValidationError(Exception):
    """Raised when the keyword database is invalid."""


class KeywordValidator:
    """
    Validates a collection of Keyword objects.
    """

    def validate(self, keywords: list[Keyword]) -> None:
        """
        Execute all validation rules.

        Raises
        ------
        ValidationError
            If one or more validation errors are found.
        """

        errors: list[str] = []

        errors.extend(self._validate_empty_keyword(keywords))
        errors.extend(self._validate_duplicates(keywords))
        errors.extend(self._validate_categories(keywords))

        if errors:
            raise ValidationError(
                "\n".join(errors)
            )

    # -----------------------------------------------------------------

    def _validate_empty_keyword(
        self,
        keywords: list[Keyword],
    ) -> list[str]:

        errors: list[str] = []

        for keyword in keywords:

            if not keyword.keyword.strip():

                errors.append(
                    "Found an empty keyword."
                )

        return errors

    # -----------------------------------------------------------------

    def _validate_duplicates(
        self,
        keywords: list[Keyword],
    ) -> list[str]:

        counter = Counter(
            keyword.keyword
            for keyword in keywords
        )

        errors: list[str] = []

        for keyword, count in sorted(counter.items()):

            if count > 1:

                errors.append(
                    f'Duplicate keyword: "{keyword}" ({count} occurrences)'
                )

        return errors

    # -----------------------------------------------------------------

    def _validate_categories(
        self,
        keywords: list[Keyword],
    ) -> list[str]:

        errors: list[str] = []

        valid_categories = {
            category.value
            for category in Category
        }

        for keyword in keywords:

            if keyword.category.value not in valid_categories:

                errors.append(
                    f'Invalid category "{keyword.category.value}" '
                    f'for keyword "{keyword.keyword}".'
                )

        return errors

    # -----------------------------------------------------------------

    def summary(
        self,
        keywords: list[Keyword],
    ) -> dict[str, int]:
        """
        Returns keyword statistics grouped by category.
        """

        result: dict[str, int] = {}

        for keyword in keywords:

            category = keyword.category.value

            result[category] = result.get(category, 0) + 1

        return dict(sorted(result.items()))