class CoffeMachine:
    def __init__(self, water_tank, trash):
        self.water_tank = water_tank
        self.trash = trash


class CoffeMachineBuilder():
    def __init__(self):
        self._coffe_machine = CoffeMachine

    def set_water_tank(self, water_tank_value):
        self._coffe_machine.water_tank = water_tank_value
        return self

    def set_trash(self, trash_value):
        self._coffe_machine.trash = trash_value
        return self

    def build(self):
        return self._coffe_machine


coffe_machine_builder = CoffeMachineBuilder()

coffe_machine = (coffe_machine_builder
                 .set_water_tank(2)
                 .set_trash(4)
                 .build())


