from aiogram.fsm.state import StatesGroup, State

class Booking(StatesGroup):
    specialist = State()
    date = State()
    time = State()
    name = State()
    phone = State()
