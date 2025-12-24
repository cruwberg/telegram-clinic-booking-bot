from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import Booking
from keyboards.booking import specialists_kb, date_kb, time_kb
from config import ADMIN_ID

router = Router()

# Шаг 1: Начало записи
@router.message(F.text == "🩺 Записаться на приём")
async def start_booking(message: Message, state: FSMContext):
    await message.answer("Выберите специалиста:", reply_markup=specialists_kb())
    await state.set_state(Booking.specialist)

# Шаг 2: Выбор специалиста
@router.callback_query(F.data.startswith("spec_"))
async def choose_spec(call: CallbackQuery, state: FSMContext):
    await state.update_data(specialist=call.data.split("_")[1])
    await call.message.answer("Выберите дату:", reply_markup=date_kb())
    await state.set_state(Booking.date)

# Шаг 3: Выбор даты
@router.callback_query(F.data.startswith("date_"))
async def choose_date(call: CallbackQuery, state: FSMContext):
    await state.update_data(date=call.data.split("_")[1])
    await call.message.answer("Выберите время:", reply_markup=time_kb())
    await state.set_state(Booking.time)

# Шаг 4: Выбор времени
@router.callback_query(F.data.startswith("time_"))
async def choose_time(call: CallbackQuery, state: FSMContext):
    await state.update_data(time=call.data.split("_")[1])
    await call.message.answer("Введите ваше имя:")
    await state.set_state(Booking.name)

# Шаг 5: Ввод имени
@router.message(Booking.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(Booking.phone)

# Шаг 6: Ввод телефона и завершение
@router.message(Booking.phone)
async def finish_booking(message: Message, state: FSMContext):
    data = await state.get_data()
    text = (
        "🩺 Новая запись\n\n"
        f"Специалист: {data['specialist']}\n"
        f"Дата: {data['date']}\n"
        f"Время: {data['time']}\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {message.text}"
    )
    await message.bot.send_message(ADMIN_ID, text)
    await message.answer("✅ Ваша заявка отправлена! Администратор свяжется с вами.")
    await state.clear()
