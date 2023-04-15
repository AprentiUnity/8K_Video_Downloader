import PySimpleGUI as sg
import webbrowser
from pytube import YouTube as yt
from pytube import Playlist as pl
from pytube import Channel as ch
import os

sg.theme('DarkBlue1')

titre = ''
titrepl = ''
titrec = ''
auteur = ''
publication = ''
vues = 0
vuespl = 0
vuesc = 0
motsclef = []
motscleftxt = ''
temps = 0
description = ''
contenu = []
contenutxt = ''
contenuc = []
contenutxtc = ''
dertitrec = ''

def fenetre_ouvert():
    return sg.Window('Téléchargeur de vidéos 8K', icon='.py/PlusTard', size=(800, 640), finalize=False, layout=[
        [sg.TabGroup([[
            sg.Tab('Télécharger une vidéo', layout=[
                [sg.Column([[sg.Text('Téléchargeur de vidéos 8K', font='_ 20')]], element_justification='center', expand_x=True)],
                [sg.Column([[sg.Text('                                             par ApprentiUnity', font='_ 15')]], element_justification='center', expand_x=True)],
                [sg.Text()],
                [sg.Text("Enregistrer dans : "), sg.InputText(key='-TXT2-'), sg.FolderBrowse('  Parcourir  ', initial_folder=os.getcwd())],
                [sg.Text("Lien de la vidéo :  "), sg.InputText(key='-TXT1-'), sg.Button('Rechercher')],
                [sg.Text('Titre :                        ' + titre, key='-TXTMAJ1-')],
                [sg.Text('Auteur :                     '), sg.Text(auteur, text_color="#0000EE", enable_events=True, key='-TXTMAJ2-')],
                [sg.Text('Publié le :                     ' + str(publication), key='-TXTMAJ3-')],
                [sg.Text('Nombre de vues :          ' + str(vues), key='-TXTMAJ4-')],
                [sg.Text('Mots Clef :                   ' + motscleftxt, key='-TXTMAJ5-')],
                [sg.Text('Longeur (en secondes) : ' + str(temps), key='-TXTMAJ6-')],
                [sg.Column([[sg.Text('Description : \n' + description, size=(110, 256), key='-TXTMAJ7-')]], scrollable=True, vertical_scroll_only=True, size=(740, 196))],
                [sg.Column([[sg.Button('Télécharger')]], justification='center')]
            ]),
            sg.Tab('Télécharger une playlist', layout=[
                [sg.Column([[sg.Text('Téléchargeur de vidéos 8K', font='_ 20')]], element_justification='center', expand_x=True)],
                [sg.Column([[sg.Text('                                             par ApprentiUnity', font='_ 15')]], element_justification='center', expand_x=True)],
                [sg.Text()],
                [sg.Text("Enregistrer dans : "), sg.InputText(key='-TXT4-'), sg.FolderBrowse('  Parcourir  ', initial_folder=os.getcwd())],
                [sg.Text("Lien de la playlist :  "), sg.InputText(key='-TXT3-'), sg.Button('Rechercher')],
                [sg.Text('Titre :                        ' + titrepl, key='-TXTMAJ8-')],
                [sg.Text('Nombre de vues :          ' + str(vuespl), key='-TXTMAJ9-')],
                [sg.Column([[sg.Text('Cette playlist contient : \n' + contenutxt, size=(110, 256), key='-TXTMAJ10-')]], scrollable=True, vertical_scroll_only=True, size=(740, 308))],
                [sg.Column([[sg.Button('Télécharger')]], justification='center')]
            ]),
            sg.Tab('Télécharger une chaîne', layout=[
                [sg.Column([[sg.Text('Téléchargeur de vidéos 8K', font='_ 20')]], element_justification='center', expand_x=True)],
                [sg.Column([[sg.Text('                                             par ApprentiUnity', font='_ 15')]], element_justification='center', expand_x=True)],
                [sg.Text()],
                [sg.Text("Enregistrer dans : "), sg.InputText(key='-TXT6-'), sg.FolderBrowse('  Parcourir  ', initial_folder=os.getcwd())],
                [sg.Text("Lien de la chaîne :  "), sg.InputText(key='-TXT5-'), sg.Button('Rechercher')],
                [sg.Text('Nom de la chaine :                 ' + titrec, key='-TXTMAJ11-')],
                [sg.Text('Titre de sa dernière video :                 ' + dertitrec, key='-TXTMAJ12-')],
                [sg.Text('Nombre de vues de sa dernière video :          ' + str(vuesc), key='-TXTMAJ13-')],
                [sg.Text('Cette chaîne contient : \n' + contenutxtc, size=(110, 21), key='-TXTMAJ14-')],
                [sg.Column([[sg.Button('Télécharger')]], justification='center')]
            ]),
            sg.Tab('A propos', layout=[
                [sg.Column([[sg.Text('Téléchargeur de vidéos 8K', font='_ 20')]], element_justification='center', expand_x=True)],
                [sg.Column([[sg.Text('                                             par ApprentiUnity', font='_ 15')]], element_justification='center', expand_x=True)],
                [sg.Text()],
                [sg.Text("Version 2.1 [Beta 04.2023]")],
                [sg.Text("Changelog", text_color="#0000EE", enable_events=True, key="-LINKCHANGELOG-")],
                [sg.Text("Signaler un problème", text_color="#0000EE", enable_events=True, key="-LINKISSUE-")],
                [sg.Text("Repo Github", text_color="#0000EE", enable_events=True, key="-LINKGITHUB-")],
            ])
        ]])]
    ])

fenetre = fenetre_ouvert()

event, values = fenetre.read()
fenetre["-LINKCHANGELOG-"].set_cursor("hand2")
fenetre["-LINKCHANGELOG-"].Widget.bind("<Enter>", lambda _: fenetre["-LINKCHANGELOG-"].update(font=(None, 10, "underline")))
fenetre["-LINKCHANGELOG-"].Widget.bind("<Leave>", lambda _: fenetre["-LINKCHANGELOG-"].update(font=(None, 10)))
fenetre["-LINKISSUE-"].set_cursor("hand2")
fenetre["-LINKISSUE-"].Widget.bind("<Enter>", lambda _: fenetre["-LINKISSUE-"].update(font=(None, 10, "underline")))
fenetre["-LINKISSUE-"].Widget.bind("<Leave>", lambda _: fenetre["-LINKISSUE-"].update(font=(None, 10)))
fenetre["-LINKGITHUB-"].set_cursor("hand2")
fenetre["-LINKGITHUB-"].Widget.bind("<Enter>", lambda _: fenetre["-LINKGITHUB-"].update(font=(None, 10, "underline")))
fenetre["-LINKGITHUB-"].Widget.bind("<Leave>", lambda _: fenetre["-LINKGITHUB-"].update(font=(None, 10)))

while True:
    event, values = fenetre.read()
    print(event)
    if event == "Rechercher":
        lien = yt(values['-TXT1-'])
        titre = lien.title
        fenetre['-TXTMAJ1-'].update('Titre :                           ' + titre)
        auteur = lien.author
        fenetre['-TXTMAJ2-'].update(auteur)
        fenetre["-TXTMAJ2-"].set_cursor("hand2")
        fenetre["-TXTMAJ2-"].Widget.bind("<Enter>", lambda _: fenetre["-TXTMAJ2-"].update(font=(None, 10, "underline")))
        fenetre["-TXTMAJ2-"].Widget.bind("<Leave>", lambda _: fenetre["-TXTMAJ2-"].update(font=(None, 10)))
        publication = lien.publish_date
        fenetre['-TXTMAJ3-'].update('Publié le :                     ' + str(publication))
        vues = lien.views
        fenetre['-TXTMAJ4-'].update('Nombre de vues :         ' + str(vues))
        motsclef = lien.keywords
        motscleftxt = " ".join(motsclef)
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

    if event == "Rechercher1":
        lienpl = pl(values['-TXT3-'])
        titrepl = lienpl.title
        fenetre['-TXTMAJ8-'].update('Titre :                           ' + titrepl)
        vuespl = lienpl.views
        fenetre['-TXTMAJ9-'].update('Nombre de vues :         ' + str(vuespl))
        contenu = lienpl.video_urls
        contenutxt = "\n".join(contenu)
        fenetre['-TXTMAJ10-'].update('Cette playlist contient : \n' + contenutxt)

    if event == "Télécharger2":
        if not os.path.exists(values["-TXT4-"]):
            os.makedirs(values["-TXT4-"])
        for videopl in lienpl.videos:
            videoplmr = videopl.streams.get_highest_resolution()
            videoplmr.download(values["-TXT4-"])

    if event == "Rechercher4": #Cassé
        lienc = ch(values['-TXT5-'])
        print(lienc.videos)
        titrec = lienc.videos[0].author
        fenetre['-TXTMAJ11-'].update('Nom de la chaine :                           ' + titrec)
        dertitrec = lienc.videos[0].title
        fenetre['-TXTMAJ12-'].update('Titre de sa dernière video :                 ' + dertitrec)
        vuesc = lienc.videos[0].views
        fenetre['-TXTMAJ13-'].update('Nombre de vues de sa dernière video :         ' + str(vuesc))
        contenuc = lienc.video_urls
        contenutxtc = "\n".join(contenuc)
        fenetre['-TXTMAJ14-'].update('Cette chaîne contient : \n' + contenutxtc)

    if event == "Télécharger5":
        if not os.path.exists(values["-TXT6-"]):
            os.makedirs(values["-TXT6-"])
        for videoc in lienc.videos:
            videocmr = videoc.streams.get_highest_resolution()
            videocmr.download(values["-TXT6-"])

    if event == "-TXTMAJ2-":
        webbrowser.open(lien.channel_url)

    if event == "-LINKCHANGELOG-":
        webbrowser.open("https://github.com/AprentiUnity/8K_Video_Downloader/releases/tag/v2.1-beta")

    if event == "-LINKISSUE-":
        webbrowser.open("https://github.com/AprentiUnity/8K_Video_Downloader/issues/new")
    
    if event == "-LINKGITHUB-":
        webbrowser.open("https://github.com/AprentiUnity/8K_Video_Downloader")

    if event == sg.WIN_CLOSED:
        break
