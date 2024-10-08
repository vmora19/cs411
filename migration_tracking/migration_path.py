from typing import Optional

class MigrationPath:

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass
