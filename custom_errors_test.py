from unittest import TestCase

from folders import (
    Folders,
    NotDefinedLibraryManagerError,
)

class TestNotDefinedLibraryManagerError(TestCase):
    def test_error_inivocation_without_text(self):
        error = NotDefinedLibraryManagerError()

        assert error
        assert str(error) == 'NotDefinedLibraryManagerError has been raised'

    def test_error_inivocation_with_text(self):
        error = NotDefinedLibraryManagerError('Error Message')

        assert error
        assert str(error) == 'NotDefinedLibraryManagerError, Error Message '