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
    
    root_list = []
    min_node = 0

    total_nodes = 0

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        new_node = self.Node(value, left=None, right=None)
        if self.root_list is None:
            self.root_list.append(new_node.value)
            self.min_node = new_node.value
        else:
            self.root_list.append(new_node.value)
            if new_node.value < self.min_node:
                self.min_node = new_node.value
        self.total_nodes = self.total_nodes + 1

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        return min(self.root_list)

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        if fibonnaci_heap.find_min() < self.min_node:
            self.min_node = fibonnaci_heap.find_min()
        for value in fibonnaci_heap.root_list:
            self.root_list.append(value)

    def print_root_list(self):
        """
        Affiche la liste de nodes à la racine.
        """
        print(self.root_list)

    def print_total_nodes(self):
        """
        Affiche le nombre de nodes qu'a un arbre.
        """
        print("L'arbre a", self.total_nodes, "nodes.")

    def print_min_node(self):
        """
        Affiche le nombre de nodes qu'a un arbre.
        """
        print("Le minimum de cet arbre est", self.min_node)

heap = FibonacciHeap()
heap.insert(48)
heap.insert(34)
heap.print_total_nodes()
heap.print_root_list()
heap.print_min_node()

heap2 = FibonacciHeap()
heap2.insert(25)
heap2.print_root_list()

heap.print_root_list()