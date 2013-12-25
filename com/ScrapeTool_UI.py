# coding=utf-8
import gui
import sys
import config
from Utilities.myLogger import logger
import Scraping_Main
from gui import dialog
import os

# --- here goes your event handlers ---

arrondissement_list = [u'', u'Aalst', u'Antwerpen', u'Arlon', u'Ath', u'Bastogne', u'Brugge', u'Bruxelles / Brussel',
                       u'Charleroi', u'Dendermonde', u'Diksmuide', u'Dinant', u'Eeklo', u'Gent', u'Halle-Vilvoorde',
                       u'Hasselt', u'Huy', u'Ieper', u'Kortrijk', u'Leuven', u'Liège', u'Maaseik', u'Marche-en-Famenne',
                       u'Mechelen', u'Mons', u'Mouscron', u'Namur', u'Neufchâteau', u'Nivelles', u'Oostende',
                       u'Oudenaarde', u'Philippeville', u'Roeselare', u'Sint-Niklaas', u'Soignies', u'Thuin', u'Tielt',
                       u'Tongeren', u'Tournai', u'Turnhout', u'Verviers', u'Veurne', u'Virton', u'Waremme']


def load(evt):
    mywin['statusbar'].text = 'The Bedrijvengids-belgie.be Scraping Tool. Powered by K Team !!!'
    setDefaultOutputDir(evt)


def setDefaultOutputDir(evt):
    mywin['txtOutputDir'].value = config.get_main_dir() + "\\Output"


def browseOutputDir(evt):
    outputDir = dialog.choose_directory(message="Choose an Output Directory", path=mywin['txtOutputDir'].value)
    if outputDir is not None:
        mywin['txtOutputDir'].value = outputDir


def num_of_search_criteria_enetered(evt):
    search_criteria_enetered = 0
    if not mywin['cboArrondissement'].text.strip() == "":
        search_criteria_enetered += 1
        config.Arrondissement = mywin['cboArrondissement'].text.strip()
    if not mywin['txtNaam'].value.strip() == "":
        search_criteria_enetered += 1
        config.Naam = mywin['txtNaam'].value.strip()
    if not mywin['txtRubriek'].value.strip() == "":
        search_criteria_enetered += 1
        config.Rubriek = mywin['txtRubriek'].value.strip()
    if not mywin['txtPostcode'].value.strip() == "":
        search_criteria_enetered += 1
        config.Postcode = mywin['txtPostcode'].value.strip()
    if not mywin['txtGemeente'].value.strip() == "":
        search_criteria_enetered += 1
        config.Gemeente = mywin['txtGemeente'].value.strip()
    return search_criteria_enetered


def doScrape(evt):
    if num_of_search_criteria_enetered(evt) < 2:
        gui.alert("Enter at least two search criteria")
        return
    if not os.path.isdir(mywin['txtOutputDir'].value):
        os.makedirs(mywin['txtOutputDir'].value)
    config.outputDir = mywin['txtOutputDir'].value

    try:
        if mywin['chkRunInBrowser'].value:
            gui.alert("You have chosen to execute scraping in browser.\nPlease do no touch your mouse or keyboard during scraping.")
        else:
            if not gui.confirm("Scraping will run in background. Please be patient.\nDo you want to proceed?"):
                return
        config.RunInBrowser = mywin['chkRunInBrowser'].value
        # gui.alert("Scraping results. Please wait.")
        mywin.minimized = True
        ret_value = Scraping_Main.doScrape()
        mywin.minimized = False
        if ret_value == 1:
            gui.alert("Scraping Done !!!")
        elif ret_value == "NO_RESULTS":
            gui.alert("Your search query returned zero results !!!")
        else:
            gui.alert("There were some problems with the scraping. Please report to developer.")
    except:
        logger.exception(sys.exc_info())
    finally:
        mywin.minimized = False
    pass

# --- gui2py designer generated code starts ---

#======== MAIN WINDOW ========#
gui.Window(name=u'Scrape_Tool', title=u'Bedrijvengids-belgie.be Scraping Tool', aximize_box=False,
           resizable=False, height='400px', left='173', top='58', width='550px', bgcolor=u'#E0E0E0', fgcolor=u'#000000',
           image=config.get_main_dir() + '/Resources/tile.bmp', tiled=True, )

#======== HEADER LABELS ========#
gui.Label(id=281, name='label_211_281', height='17', left='50', top='40', width='254', transparent=True,
          font={'size': 9, 'family': 'sans serif', 'face': u'Arial'}, parent=u'Scrape_Tool',
          text=u'Welcome to Bedrijvengids-belgie.be Scraping Tool', )

gui.Label(id=1001, name='label_1001', height='17', left='50', top='80', width='131', parent=u'Scrape_Tool',
          text=u'Arrondissement:', transparent=True, )

gui.ComboBox(id=1003, name=u'cboArrondissement', height='23', left='170', sizer_align='center', top='80', width='250',
             bgcolor=u'#FFFFFF', editable=True, enabled=True, fgcolor=u'#000000', parent=u'Scrape_Tool',
             transparent=True, readonly=True, items=arrondissement_list)

gui.Label(id=1002, name='label_1002', height='17', left='50', top='120', width='131', parent=u'Scrape_Tool',
          text=u'Naam', transparent=True, )

gui.TextBox(id=1004, name=u'txtNaam', height='23', left='170', sizer_align='center', top='120', width='250',
            bgcolor=u'#FFFFFF', editable=True, enabled=True, fgcolor=u'#000000', parent=u'Scrape_Tool',
            transparent=True)

gui.Label(id=1005, name='label_1005', height='17', left='50', top='160', width='131', parent=u'Scrape_Tool',
          text=u'of Branche(Rubriek)', transparent=True, )

gui.TextBox(id=1006, name=u'txtRubriek', height='23', left='170', sizer_align='center', top='160', width='250',
            bgcolor=u'#FFFFFF', editable=True, enabled=True, fgcolor=u'#000000', parent=u'Scrape_Tool',
            transparent=True,)

gui.Label(id=1007, name='label_1007', height='17', left='50', top='200', width='131', parent=u'Scrape_Tool',
          text=u'Postcode/Gemeente', transparent=True, )

gui.TextBox(id=1008, name=u'txtPostcode', height='23', left='170', sizer_align='center', top='200', width='80',
            bgcolor=u'#FFFFFF', editable=True, enabled=True, fgcolor=u'#000000', parent=u'Scrape_Tool',
            transparent=True,)

gui.TextBox(id=1009, name=u'txtGemeente', height='23', left='255', sizer_align='center', top='200', width='165',
            bgcolor=u'#FFFFFF', editable=True, enabled=True, fgcolor=u'#000000', parent=u'Scrape_Tool',
            transparent=True,)

gui.TextBox(id=1006, name=u'txtOutputDir', height='23', left='50', sizer_align='center', top='270', width='400',
            bgcolor=u'#FFFFFF', editable=True, enabled=True, fgcolor=u'#000000', parent=u'Scrape_Tool',
            transparent=True,)

gui.CheckBox(name=u'chkRunInBrowser', left='50', top='310',
             parent=u'Scrape_Tool', label=u'Run In Browser?')

gui.Button(label=u'Browse Output Directory', name=u'btnBrowseOutputDir', left='50', top='240', fgcolor=u'#000000',
           parent=u'Scrape_Tool', transparent=True, )


# #======== DO ORDER SCRAPE BUTTON ========#
gui.Button(label=u'Scrape Results', name=u'btnScrape', height='39', left='185', top='327', width='292',
           fgcolor=u'#000000', font={'size': 11, 'family': 'sans serif', 'face': u'Tahoma'}, parent=u'Scrape_Tool',
           transparent=True, )

gui.StatusBar(name='statusbar', parent=u'Scrape_Tool', )

gui.Image(name='image_148', height='40', left='440', top='5', width='100', fgcolor=u'#000000',
          filename=config.get_main_dir() + '/Resources/python-powered.bmp', parent=u'Scrape_Tool', stretch=False,
          transparent=False, border='static')

# --- gui2py designer generated code ends ---

# get a reference to the Top Level Window:
mywin = gui.get("Scrape_Tool")

# assign your event handlers:
mywin.onload = load
mywin['btnScrape'].onclick = doScrape
mywin['btnBrowseOutputDir'].onclick = browseOutputDir

if __name__ == "__main__":
    # myLogger.setupLogging()
    mywin.show()
    gui.main_loop()