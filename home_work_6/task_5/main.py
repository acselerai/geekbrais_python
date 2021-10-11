from stationery import Stationery, Pen, Pencil, Handle

base_stationery = Stationery(title='Stationery')
pen = Pen(title='Pen')
pencil = Pencil(title='Pencil')
handle = Handle(title='Handle')

stationeries = [base_stationery, pen, pencil, handle]

for stationery in stationeries:
    print(f'{stationery.title} draws: {stationery.draw()}')
