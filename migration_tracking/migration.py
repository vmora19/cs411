from typing import Any

class Migration:

    def __init__(self, migration_id: int):      
        self.migration_id = migration_id

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass

    def get_migrations() -> list[Migration]:
        pass
