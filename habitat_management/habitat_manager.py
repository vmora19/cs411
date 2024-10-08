from typing import Optional, List
from habitat_management.habitat import Habitat

class HabitatManager:

    def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
        pass

    def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass

    def get_habitat_by_id(habitat_id: int) -> Habitat:
        pass

    def get_habitat_details(habitat_id: int) -> dict:
        pass

    def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]:
        pass

    def get_habitats_by_size(size: int) -> List[Habitat]:
        pass

    def get_habitats_by_type(environment_type: str) -> List[Habitat]:
        pass

    def remove_habitat(habitat_id: int) -> None:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    def schedule_migration(migration_path: MigrationPath) -> None:
        pass

    def cancel_migration(migration_id: int) -> None:
        pass



    
