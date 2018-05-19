# Currently does it all.  Could be optimized. Lots of redundant code.

import csv
import pprint
import copy
import os

FilePaths = {}
FilePaths['GamePaths'] = {
    'ColorPalettes' :   '../../Necropolis_Data/StreamingAssets/data/TUNING/ColorPalettes.csv',
    'Items'         :   '../../Necropolis_Data/StreamingAssets/data/TUNING/Items.csv',
    'LootTables'    :   '../../Necropolis_Data/StreamingAssets/data/TUNING/Loot Tables.csv',
    'Strings'       :   '../../Necropolis_Data/StreamingAssets/data/text/Strings.csv',
    'WorldLocs'     :   '../../Necropolis_Data/StreamingAssets/data/text/World Locations.csv'}

FilePaths['ModPaths'] = {
    'ColorPalettes' :   'ColorPalettes.csv',
    'Items'         :   'Items.csv',
    'LootTables'    :   'Loot Tables.csv',
    'Strings'       :   'Strings.csv',
    'WorldLocs'     :   'World Locations.csv'}
################################################################################
#-------------------------------------------------------------------------------
# GENERIC READER
#-------------------------------------------------------------------------------
def CheckFiles(incolors, file, modFile):
    print('\n Checking ' + file + '...')
    colors = copy.deepcopy(incolors)
    with open(file, 'r', newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)

        # For ITEMS and LOOTTABLES. Same as for LOOTTABLES.
        if file == FilePaths['GamePaths']['Items'] or file == FilePaths['GamePaths']['LootTables']:
            for row in reader:
                for color in colors:
                    if color['ID'].replace('patchAdd_','') in row[1]:
                        colors.remove(color)
                        break
                    elif color['ID'].replace('patchOver_','') in row[1]:
                        colors.remove(color)
                        break
                    else:
                        pass

        # For STRINGS.
        if file == FilePaths['GamePaths']['Strings']:
            for row in reader:
                for color in colors:
                    color['Has Location'] = 'false'
                for color in colors:
                    # Check for World Location IDs (for unused palettes)
                    if color['Text Identity'].strip() in row[0].strip():
                        color['Has Location'] = 'true'
                    else:
                        pass
                    # Check for Color IDs
                    if color['ID'].replace('patchAdd_','') in row[0]:
                        colors.remove(color)
                        break
                    elif color['ID'].replace('patchOver_','') in row[0]:
                        colors.remove(color)
                        break
                    else:
                        pass

        #For WORLDLOCS
        if file == FilePaths['GamePaths']['WorldLocs']:
            for row in reader:
                for color in colors:
                    if color['Text Identity'] in row[0]:
                        colors.remove(color)
                        break
                    else:
                        pass
        WriteFiles(colors, modFile)

#-------------------------------------------------------------------------------
# GENERIC WRITER
#-------------------------------------------------------------------------------
def WriteFiles(colors, file):
    print('\n Writing ' + file + '...')
    with open('outf.csv', 'w', newline='') as outf:
        writer = csv.writer(outf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if file == FilePaths['ModPaths']['Items']:
            for color in colors:
                writer.writerow(['ColorSwatch', color['ID'], '2', '', '', color['Price'], '', '', '', '', '', '', '', '','ColorSwatch'])

        if file == FilePaths['ModPaths']['LootTables']:
            for color in colors:
                if 'patchAdd_' in color['ID']:
                    writer.writerow(['patchAdd_ColorSetAll', color['ID'].replace('patchAdd_','')])
                    writer.writerow(['patchAdd_ColorSet'+color['Floor'], color['ID'].replace('patchAdd_','')])
                if 'patchOver_' in color['ID']:
                    writer.writerow(['patchAdd_ColorSetAll', color['ID'].replace('patchOver_','')])
                    writer.writerow(['patchAdd_ColorSet'+color['Floor'], color['ID'].replace('patchOver_','')])

        if file == FilePaths['ModPaths']['Strings']:
            for color in colors:
                if color['Has Location'] == 'false':
                    writer.writerow(['patchOver_'+color['Text Identity'], color['Identified Name'].replace('Colors of ','')])
                else:
                    pass
                writer.writerow([color['ID']+'/Name (Identified)', color['Identified Name']])
                writer.writerow([color['ID']+'/Description (Identified)', color['Description']])
                writer.writerow([color['ID']+'/Icon (Identified)', 'im-icon-item-component'])
                writer.writerow([color['ID']+'/Icon (Unidentified)', 'im-icon-item-component'])

        if file == FilePaths['ModPaths']['WorldLocs']:
            for color in colors:
                writer.writerow(['patchAdd_' + color['Text Identity'], color['Identified Name'].replace('Colors of ', '')])

    if os.path.isfile(file):
        os.remove(file)
    os.replace(outf.name, file)

################################################################################
#-------------------------------------------------------------------------------
# Collects new colors into list of dictionaries
#-------------------------------------------------------------------------------
# Gets list of new colors, stripping out entries that already exist in
# FilePaths['GamePaths']['ColorPalettes']

def GetColors(file, modFile):
    print('\n Getting Colors...')
    
    with open(modFile, newline='', encoding='utf8') as csvfile_M:
        colors_M = []
        reader_M = csv.DictReader(csvfile_M)
        print('readingM1')
        for row in reader_M:
            if row['ID'] != '':
                print('readingM2')
                colors_M.append(row)

                
    with open(file, newline='', encoding='utf8') as csvfile_G:
        colors_G = []
        reader_G = csv.DictReader(csvfile_G)
        print('readingG1')
        for row in reader_G:
            if row['ID'] != '':
                print('readingG2')
                colors_G.append(row)
    
    print('it worked')
    for entry in colors_G:
        for color in colors_M:
            if color['ID'].replace('patchAdd_','') == entry['ID'] or\
            color['ID'].replace('patchOver_','') == entry['ID'] or\
            color['Identified Name'] == entry['Identified Name']or\
            color['Text Identity'] == entry['Text Identity']:
                colors_M.remove(color)
                print('This color already exists')
##
##    pp = pprint.PrettyPrinter(indent=2)
##    pp.pprint(colors_M[0].keys())
    
    return colors_M

## Rewrite the ColorPalettes file
def FixColorPalettes(colors, file):
    print('\n Rewriting ' + file + '...')
    # improving this would require rewriting the file without already used names
    with open('outf.csv', 'w', newline='') as outf:
        writer = csv.writer(outf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(colors[0].keys())
        for color in colors:
           writer.writerow(color.values())
    if os.path.isfile(file):
       os.remove(file)
    os.replace(outf.name, file)

# Finds all the new color palettes
inputColors = GetColors(FilePaths['GamePaths']['ColorPalettes'], FilePaths['ModPaths']['ColorPalettes'])
# Checks game csv files and writes their respective mod csv files
for path in FilePaths['GamePaths']:
    if path != 'ColorPalettes':
        CheckFiles(inputColors, FilePaths['GamePaths'][path], FilePaths['ModPaths'][path])
# Rewrites mod Color Palettes csv without any paletes that might modify game defaults
FixColorPalettes(inputColors, FilePaths['ModPaths']['ColorPalettes'])
print('\n Done')
