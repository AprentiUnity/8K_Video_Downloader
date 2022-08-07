import PySimpleGUI as sg
from pytube import YouTube as yt
import os

sg.theme('DarkBlue1')

titre = ''
auteur = ''
publication = ''
vues = 0
motsclef = []
motscleftxt = ''
temps = 0
description = ''


def fenetre_ouvert():
    return sg.Window('Téléchargeur de vidéos 8K', icon='.py/PlusTard', size=(800, 600), finalize=True, layout=[
        [sg.Column([[sg.Text('Téléchargeur de vidéos 8K', font='_ 20')]], element_justification='center', expand_x=True)],
        [sg.Column([[sg.Text('                                             par AprentiUnity', font='_ 15')]], element_justification='center', expand_x=True)],
        [sg.Text()],
        [sg.Text("Enregistrer dans : "), sg.InputText(key='-TXT2-')],
        [sg.Text("Lien de la vidéo : "), sg.InputText(key='-TXT1-'), sg.Button('Rechercher')],
        [sg.Text('Titre : ' + titre)],
        [sg.Text('Auteur : ' + auteur)],
        [sg.Text('Publié le : ' + str(publication))],
        [sg.Text('Nombre de vues : ' + str(vues))],
        [sg.Text('Mots Clef : ' + motscleftxt)],
        [sg.Text('Longeur (en secondes) : ' + str(temps))],
        [sg.Text('Description : \n' + description, size=(110, 16))],
        [sg.Column([[sg.Button('Télécharger')]], justification='center')]
    ])

while True:
    fenetre = fenetre_ouvert()
    event, values = fenetre.read()
    if event == "Rechercher":
        lien = yt(values['-TXT1-'])
        titre = lien.title
        auteur = lien.author
        publication = lien.publish_date
        vues = lien.views
        motsclef = lien.keywords
        motscleftxt = "".join(motsclef)
        temps = lien.length
        description = lien.description

    if event == "Télécharger":
        lienmr = lien.streams.get_highest_resolution()
        if not os.path.exists(values["-TXT2-"]):
            os.makedirs(values["-TXT2-"])
        lienmr.download(values["-TXT2-"])

    if event == sg.WIN_CLOSED:
        break

    fenetre.close()
