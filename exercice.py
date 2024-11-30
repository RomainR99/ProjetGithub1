# Fonction pour lister les todos - à réaliser
def lister_todos():
	print('Fonctionnalité "lister les todos" à venir')
# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todos.append((titre, "À faire"))
    print(f"Todo '{titre}' ajouté avec le statut 'À faire'.")
# Menu principal
choix = ''
while choix != 'q':
	# Affichage des choix
	print('\n==== Menu principal ====')
	print('1: Lister les todos')
	print('========================')
	# Actions suivant le choix
	choix = input('=> Choix : ')
	match choix:
		case '1': lister_todos()
