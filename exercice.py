# Fonction pour lister les todos - à réaliser
def lister_todos():
	print('Fonctionnalité "lister les todos" à venir')
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
