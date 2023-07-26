from abc import ABC, abstractmethod

class MenuProgram(ABC):
    def run(self):
        running = True
        while running:
            self._print_menu()
            choice = self._get_option()
            self._do_task(choice)

            running == choice != 0
    
    def _get_option(self):
        choice = int(input("Enter your choice: "))
        return choice
    
    @abstractmethod
    def _print_menu(self):
        pass

    @abstractmethod
    def _do_task(self, choice):
        pass