from warehouse import Printer, Xerox, Scanner, Warehouse, InvalidAmount

printer_one = Printer('Epson', 'XP440', 'laser')
printer_two = Printer('Epson', 'XP400', 'laser')
xerox_one = Xerox('Xerox', 'PL00', 'very fast')
xerox_two = Xerox('Xerox', 'PL34', 'very fast')
scanner_one = Scanner('Canon', 'CL00', 1200)
scanner_two = Scanner('Canon', 'CL002', 1000)

warehouse = Warehouse()

warehouse.add_item(printer_one)
warehouse.add_item(printer_one)
warehouse.add_item(printer_two)

warehouse.add_item(xerox_one)
warehouse.add_item(xerox_two)
warehouse.add_item(xerox_two)

warehouse.add_item(scanner_one)
warehouse.add_item(scanner_two)
warehouse.add_item(scanner_one)

print(f'Warehouse after adding items: {warehouse.items}')

warehouse.obtain_item(printer_one)
warehouse.obtain_item(xerox_two)
warehouse.obtain_item(scanner_two)

try:
    warehouse.obtain_item(scanner_one)
    warehouse.obtain_item(scanner_one)
    warehouse.obtain_item(scanner_one)
except InvalidAmount as err:
    print(err)

print(f'Warehouse after obtaining items: {warehouse.items}')
