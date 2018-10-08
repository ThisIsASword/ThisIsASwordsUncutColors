ThisIsASword's Uncut Colors for Necropolis

You must have Partiality and Abraxis Toolkit installed for this mod to work.

Just drop this folder into your "Mods" folder in:
(Windows)
C:\Program Files (x86)\Steam\steamapps\common\Necropolis

(OSX)
/Users/<your user name>/Library/Application Support/Steam/steamapps/common/Necropolis

##########################################################################
If this version includes the ColorPaletteWriter.py script, in order to use it you'll need to install the latest version of Python 3 if you don't already have it.

You can find that here:
https://www.python.org/downloads/release/python-2715/

Just download the MSI installer if you use Windows or macOS installer for OSX for ease of use.

NOTE: The ColorPaletteWriter.py script is not essential for the mod to work. It's just there in case you want an easy way to add your own color palettes to the game, otherwise you can ignore it.

-------------------------------------------------------------------------
Using the Writer Script:
##################################################################
##### NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE #####
At the moment there is no way to remove color palettes once you've
unlocked them. So if you make a color palette then decide you
don't want it anymore, removing its entry from the CSV file will
leave you with a color palette called "???" for each you remove.
You can change the color values for a palette even after you've 
purchased it in game with no problems though so until further
notice, try to avoid making a bunch of things you might hate in
the future.
##################################################################

Making your own color pack is fairly straightforward.

First, make a new folder in the mods folder and name it whatever you like. 

Copy ColorPalettes.csv and ColorPaletteWriter.py into the new folder.

Open ColorPalettes.csv in Open Office, Excel, or whatever spreadsheet software suits you. Make sure to specificy that separator is set to comma and the text delimiter is set to double quote.

Delete every row below the second row. You'll delete the second row eventually but in the beginning it's just there to show you the conventions to follow when filling out the fields.

ID: Prefix with "patchAdd_Colors_" then add a to-the-point version of the name of the color palette. ex: for Colors of The Elusive Bladderfish write "patchAdd_Colors_ElusiveBladderfish". This is how Abraxis knows what to add to the game and where.

Identified Name: Typically just "Colors of " and then whatever name you're giving that color palette.

Primary, Secondary, Eye Color, and Pattern Color: Each of these takes a 6 character hex value which you can easily produce with a google search of "Hex Color Picker". Make sure you have a "#" in front of the 6 characters or things will get weird and non-functional.

Pattern Opacity: If the number is 0, you won't see any pattern.  If it's 1 the pattern will be totally opaque. Anywhere in between will make it look varying degrees of faded. Anywhere above one starts to have the interesting side-effect of making light colors glow. At Opacity of 5 it was like looking at the character model through a bright, thick fog. So that's cool.

Text Identity: Always prefix with "WORLDLOC_" followed by a to-the-point version of the color palette name in allcaps with no spaces or funny characters.

Description: Get creative.

Floor: Which floor the Old Man will sell the color palette.

Price: How many tokens of favor the color palette will cost. I've had weird results with making it less than 2 so I recommend just sticking with the standard two.

Tag: In this version this column doesn't serve any real purpose but in updated versions I may use it for marking colors that are acquired by means other than purchasing from the Old Man. Until further notice, just say "normal".

Finally, save the csv file in the same format it started in (csv), close it, run Necropolis, and your color palette will be for sale on the floor you specified. Although if you just put it in the starting area (Floor: 0), nobody will judge you.
