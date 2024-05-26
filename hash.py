import csv

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def search_by_key(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def search_by_value(self, value):
        for bucket in self.table:
            for kvp in bucket:
                if kvp[1] == value:
                    return kvp[0]
        return None

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

    def load_from_csv(self, file_path):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if len(row) == 2:
                        self.insert(row[0], row[1])
        except FileNotFoundError:
            print("File not found.")

def main():
    hash_table = HashTable()

    while True:
        print("\n1. Inserte valores manualmente:")
        print("2. Buscar por clave:")
        print("3. Buscar por valor: ")
        print("4. Cargar datos desde archivo CSV: ")
        print("5. Mostrar tabla hash: ")
        print("6. Salir: ")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            key = input("Ingrese clave: ")
            value = input("Ingrese valor: ")
            hash_table.insert(key, value)
            print(f"Clave: {key}, Valor: {value}, Hash: {hash_table.hash_function(key)}")

        elif choice == '2':
            key = input("Ingrese la clave a bu1scar: ")
            result = hash_table.search_by_key(key)
            if result is not None:
                print(f"Valor encontrado: {result}")
            else:
                print("Clave no encontrada.")

        elif choice == '3':
            value = input("Ingrese el valor a buscar: ")
            result = hash_table.search_by_value(value)
            if result is not None:
                print(f"Clave encontrada: {result}")
            else:
                print("Valor no encontrado.")

        elif choice == '4':
            file_path = input("Ingrese la ruta del archivo CSV: ")
            hash_table.load_from_csv(file_path)
            print("Datos cargados desde el archivo CSV.")

        elif choice == '5':
            hash_table.display()

        elif choice == '6':
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
