from win10toast import ToastNotifier

# Создание объекта ToastNotifier
toaster = ToastNotifier()

while True:
 toaster.show_toast("Внимание!", "Пора размяться, вы слишком много сидете за компьютером!", duration=10)
