from custom_errors import NotDefinedLibraryManagerError
import os_manager


class Folders():
    OS_MODULE = 'os'

    def __init__(self, module):
        if module == self.OS_MODULE:
            self.manager = os_manager.OsManager()
        else:
            raise NotDefinedLibraryManagerError

    def retrieve_mp3_files(self, path):
        return set(
            entry for entry in self.manager.get_entities(path)
            if entry.is_file() and entry.name.endswith('.mp3')
        )

    def copy_file(self, source, destination, file_name):
        if not self.manager.exists(source):
            return None

        if not self.manager.exists(destination):
            self.manager.create_dir(destination)

        destination_file_path = self.manager.join(
                destination,
                file_name,
            )

        newPath = self.manager.copy(source, destination_file_path)

        return newPath

    def join(self, path_1, path_2):
        return self.manager.join(path_1, path_2)

    def exists(self, path):
        return self.manager.exists(path)

    def remove_dir(self, path):
        self.manager.remove_dir(path)

    def splitext(self, file_name):
        return self.manager.splitext(file_name)
