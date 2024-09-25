from functions.create_table import create_table
from functions.drop_table import drop_table
from functions.insert_row import insert_one_row

# Nome do banco de dados
database_name = 'er_model'

# Criação das tabelas com base no relacionamento ER
create_table(database_name, 'Client', '''
    Client_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Address TEXT NOT NULL
''')

create_table(database_name, '`Order`', '''
    Order_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Order_date TEXT NOT NULL,
    Client_ID INTEGER NOT NULL,
    FOREIGN KEY (Client_ID) REFERENCES Client (Client_ID)
''')

create_table(database_name, 'Products', '''
    Product_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_name TEXT NOT NULL
''')

create_table(database_name, 'Order_Items', '''
    Order_Item_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Order_ID INTEGER NOT NULL,
    Product_ID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    Price REAL NOT NULL,
    FOREIGN KEY (Order_ID) REFERENCES `Order` (Order_ID),
    FOREIGN KEY (Product_ID) REFERENCES Products (Product_ID)
''')

# Inserindo dados de exemplo
insert_one_row(database_name, 'Client', 'Name, Email, Address', ('John Doe', 'johndoe@example.com', '123 Main St'))
insert_one_row(database_name, 'Products', 'Product_name', ('Laptop',))
insert_one_row(database_name, '`Order`', 'Order_date, Client_ID', ('2024-09-25', 1))
insert_one_row(database_name, 'Order_Items', 'Order_ID, Product_ID, Quantity, Price', (1, 1, 2, 999.99))

drop_table(database_name, 'Client')
drop_table(database_name, '`Order`')
drop_table(database_name, 'Products')
drop_table(database_name, 'Order_Items')

print("Operações realizadas com sucesso!")