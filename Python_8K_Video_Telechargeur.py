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
    return sg.Window('Téléchargeur de vidéos 8K', icon='.py/PlusTard', size=(800, 600), finalize=False, layout=[
        [sg.Column([[sg.Text('Téléchargeur de vidéos 8K', font='_ 20')]], element_justification='center', expand_x=True)],
        [sg.Column([[sg.Text('                                             par AprentiUnity', font='_ 15')]], element_justification='center', expand_x=True)],
        [sg.Text()],
        [sg.Text("Enregistrer dans : "), sg.InputText(key='-TXT2-')],
        [sg.Text("Lien de la vidéo :  "), sg.InputText(key='-TXT1-'), sg.Button('Rechercher')],
        [sg.Text('Titre :                        ' + titre, key='-TXTMAJ1-')],
        [sg.Text('Auteur :                        ' + auteur, key='-TXTMAJ2-')],
        [sg.Text('Publié le :                     ' + str(publication), key='-TXTMAJ3-')],
        [sg.Text('Nombre de vues :          ' + str(vues), key='-TXTMAJ4-')],
        [sg.Text('Mots Clef :                   ' + motscleftxt, key='-TXTMAJ5-')],
        [sg.Text('Longeur (en secondes) : ' + str(temps), key='-TXTMAJ6-')],
        [sg.Text('Description : \n' + description, size=(110, 16), key='-TXTMAJ7-')],
        [sg.Column([[sg.Button('Télécharger')]], justification='center')]
    ])

fenetre = fenetre_ouvert()

while True:
    event, values = fenetre.read()
    if event == "Rechercher":
        lien = yt(values['-TXT1-'])
        titre = lien.title
        fenetre['-TXTMAJ1-'].update('Titre :                           ' + titre)
        auteur = lien.author
        fenetre['-TXTMAJ2-'].update('Auteur :                        ' + auteur)
        publication = lien.publish_date
        fenetre['-TXTMAJ3-'].update('Publié le :                     ' + str(publication))
        vues = lien.views
        fenetre['-TXTMAJ4-'].update('Nombre de vues :         ' + str(vues))
        motsclef = lien.keywords
        motscleftxt = "".join(motsclef)
        fenetre['-TXTMAJ5-'].update('Mots Clef :                   ' + motscleftxt)
        temps = lien.length
        fenetre['-TXTMAJ6-'].update('Longeur (en secondes) : ' + str(temps))
        description = lien.description
        fenetre['-TXTMAJ7-'].update('Description : \n' + description)

    if event == "Télécharger":
        lienmr = lien.streams.get_highest_resolution()
        if not os.path.exists(values["-TXT2-"]):
            os.makedirs(values["-TXT2-"])
        lienmr.download(values["-TXT2-"])

    if event == sg.WIN_CLOSED:
        break
