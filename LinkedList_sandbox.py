# Escribe debajo el codigo de la clase LinkedList y sus respectivos metodos     
# Recuerda importar la clase Node en este script

from Node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node


    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)  
        self.head_node = new_node 
        
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node() 
        while current_node is not None:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node() 
        return string_list
    
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()  # Se ajusta el puntero al segundo nodo
            current_node = None 
            return

        while current_node is not None:
            next_node = current_node.get_next_node()
            
            if next_node is not None and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())  
                next_node = None  
                return
            
            current_node = next_node  