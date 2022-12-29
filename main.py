from tkinter import *
from tkinter import messagebox  #para importar popup
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():   
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #compreção de lista: [new item for item in list]
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers #junta as 3 listas em uma variavel só
    shuffle(password_list) #embaralha a lista 

    password = "".join(password_list)  #juntar toda a lista e transformar em uma única string
    password_entry.insert(0, password) #para preencher o imput de password com a password gerada com a função.
    pyperclip.copy(password)  #essa biblioteca fará a mesma função de um ctrl+c e então é só colar onde o usuário quiser.
   

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get() #para apanhar a informação digitada pelo usuário utilizamos o .get
    email = email_entry.get()
    password = password_entry.get()
    new_dicio = {
        website:{
            "email": email,
            "password":password,
                    }
                }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Por favor, certifique-se de que não deixou nenhum campo em branco.") #para apresentar uma menssagem caso tenha campos em branco e não deixe salvar.
    
    else:
        try:  #se não ter um arquivo data.json já criado temos a excepction para resolver.  
            with open("data.json", "r") as data_file: #"r" modo de leitura
            
                #LENDO OS DADOS GRAVADOS:
                data = json.load(data_file)  #o modo .load é modo de leitura do ficheiro. Utilizamos para chamar os dados do arquivo json e utlizarmos como um dicioanrio python.
        
        except FileNotFoundError: #se encontrar a except descrita deve-se criar um novo arquivo:
            with open("data.json", "w") as data_file:
                json.dump(new_dicio, data_file, indent=4) #vide abaixo descrição deste modo.
        
        else: #se o arquivo estiver já criado e não ter except:
            #ADICIONANDO NOS DADOS GRAVADOS OS NOVOS DADOS:
            data.update(new_dicio) #o modo json.update é como o append
        
            with open("data.json", "w") as data_file: #"w" modo de escrita.
                #GRAVANDO OS DADOS ATUALIZADOS:
                json.dump(data, data_file, indent= 4)  #modo .dump é utilizado para escrever no arquivo. ex json.dump(onde/como?, e quais dados?, indent=numero de linhas? para melhor visualizar)
            
        finally: #ao final de tudo o código continuará aqui:
            website_entry.delete(0,END) #apaga oque foi digitado no campo do caracter 0 até o final. Para receber uma nova entrada sem que o usuário precise apagar.
            password_entry.delete(0,END)
            messagebox.showinfo(title="Password Manager", message="Salvo com sucesso.")  #para adionar popup informando o salvamento.


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40) #acochoamento de 20px

canvas = Canvas(height=200, width=200)  #criar tela
logo_image = PhotoImage(file="logo.png") #importa imagem para dentro da variavel
canvas.create_image(100,100 ,image=logo_image) #cria dentro do canvas uma imagem agora chamando a variavel com a imagem dentro. IMPORTANTE = sempre colocar a posição x e y no tuple.
canvas.grid(row=0, column=1)

#Etiquetas/Labels:
website_label = Label(text="Website:") #é necessário colocar de mod "text=" para poder colocar a str.
website_label.grid(row=1 , column=0)
email_label = Label(text="E-mail/Username:")
email_label.grid(row=2 , column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#ENTRADAS/Entrys:
website_entry = Entry(width=32) #tamanho da janela do imput/entrada
website_entry.grid(row=1, column=1, columnspan= 1)  #COLUMNSPAN= define até qual coluna vai a a linha
website_entry.focus()  #para cursor aparecer piscando dentro do campo de entrada de website
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan= 2)
email_entry.insert(0, "brunomart@gmail.com") #quando inicia o programa oq está inserido nesse campo já aparece previamente(talvez a última informação atualizada)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

#Botoões/Buttons:
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save) #command para adicionar ação do botão
add_button.grid(row=4, column=1, columnspan= 2)
search_button = Button(text="Search", width=15)
search_button.grid(row=1, column=2)




window.mainloop()