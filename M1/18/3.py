# Многопоточность
# Общие ресурсы
# GIL - Global Interpreter Lock - блокирует выполнение нескольких поток
# Подходит для решения IO-задач
# Переключение между потоками занимает время

# Многопроцессность
# Раздельные ресурсы
# Подходит для решения вычислительных задач
# Переключение между процессами занимает ещё больше времени

# Асинхронность
# Блокирующие действия и неблокирующие
# Корутина (Coroutine) - задачи, которые могут выполняться асинхронно
# Пока выполняется какое-то действие (IO), можно поделать что-то другое
