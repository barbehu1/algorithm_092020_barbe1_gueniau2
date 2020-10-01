class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.

    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass


class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement

    https://en.wikipedia.org/wiki/Fibonacci_heap

    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """

    class Node:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right

    root_list = None
    min_node = None

    total_nodes = 0

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        def find_min(self):
            return self.min_node

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """

heap = FibonacciHeap()
heap.insert(42)
heap.find_min()

print(heap)