from airtravel import *

f = Flight("BA758", Aircraft(registration="G-EUPT", model="Airbus A139", num_rows=22, num_seats_per_row=6))

f.allocate_seat('1A', 'Abid Ali')
f.allocate_seat('1B', 'Sajid Ali')
f._seating
