# umieszczenie wierszy w liście lines i nastepnie wyświetlenie je na zewnatrz bloku with
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


# odczytywanie pliku wiersz po wierszu
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# otwieranie pliku za pomocą bezwględnej ścieżki dostępu przechowywanej w zmiennej
file_path = '/home/jacek/PycharmProjects/files_and_exceptions/text_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())


# otwieranie pliku znajdującego się w podfolderze lokalizacji z programem
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())


# otwieranie pliku w tej samej lokalizacji co program
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
