# Dictionary
from rich.console import Console

console = Console()


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

console.print(programming_dictionary)

# Mengambil item pada dict
console.print(programming_dictionary.get('Bug'))

# Menambahkan item baru pada dict
programming_dictionary["Loop"] = "Proses untuk melakukan sesuatu secara berulang"

console.print(programming_dictionary)

# Mengedit itemn
programming_dictionary["Bug"] = "Sebuah error yang terjadi ketika program di jalankan biasanya karena kesalahan logic"
console.print(programming_dictionary)

console.print(programming_dictionary.items())

# Loop 
for key, value in programming_dictionary.items():
    console.print(key, ':', value)