from typing import Any, Optional

class Animal:

    def __init__(self, animal_id: int):      
        self.animal_id = animal_id
    
    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass
