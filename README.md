
Treasure Sort
=============

Overview
--------
A means of organizing treasure / loot lists for Dungeons & Dragons®. Motivated
by the lack of an organized table of treasure items with cooresponding costs in
the Out of the Abyss™ adventure. Items are scattered throughout the book with
descriptions and values which makes appropriately appraising them difficult for
the Game / Dungeon Master (GM/DM).

Key
---
* - Planned changes, modifications, improvements

Files
-----
1) treasureSort.py      Program

2) treasure.txt         Sample input / output

3) sortedTreasure.txt   Sample output

Usage
-----
1) Create a file called "treasure.txt" in the same directory as the program. 

2) Systematically flip through an adventure book or module. Write in the item
   name with relevent details, the gold cost associated with it, and the page
   number on which the info. can be found. Separate these details with ";" and
   no spaces. The gold cost should be written as the number followed by " gp".
   The page number should be written after "pg ".

   Ex.

     Small shrine to Lolth of zurkhwood and bone;50 gp;pg 14
     Silver chain headdress set w/ small onyx stones;50 gp;pg 14
     Spider-shaped onyx brooch;50 gp;pg 14
     50gp gemstone;50 gp;pg 29
     10gp gemstone;10 gp;pg 29
     Obsidian statuette of Lolth;100 gp;pg 29
     Gold ring;25 gp;pg 29
     Green-gold bracelet;25 gp;pg 36

   *Future versions will be written to accommodate a greater variety of input
    styling.

3) Execute treasureSort.py using Python3.

4) The program will create a new file (sortedTreasure.txt) which will be
   organized into a standard structure that can then be converted to a PDF,
   printed, or simply displayed.

   Ex.
   
     Silver chain headdress set w/ small onyx stones              50 gp    pg 14
     Small shrine to Lolth of zurkhwood and bone                  50 gp    pg 14
     Spider-shaped onyx brooch                                    50 gp    pg 14
     10gp gemstone                                                10 gp    pg 29
     Gold ring                                                    25 gp    pg 29
     50gp gemstone                                                50 gp    pg 29
     Obsidian statuette of Lolth                                 100 gp    pg 29
     Green-gold bracelet                                          25 gp    pg 36

   The list is sorted by (in order or significance) page number, then value, and
   lastly in alphabetical order of names. This output file is also dynamically
   generated to always align value and page numbers and grant only one line per
   item.

5) The program will also rewrite the treasure.txt file. It will maintain the
   standard structure, but will now be ordered in the same way as the
   sortedTreasure.txt file.

   Ex.

     Silver chain headdress set w/ small onyx stones;50 gp;pg 14
     Small shrine to Lolth of zurkhwood and bone;50 gp;pg 14
     Spider-shaped onyx brooch;50 gp;pg 14
     10gp gemstone;10 gp;pg 29
     Gold ring;25 gp;pg 29
     50gp gemstone;50 gp;pg 29
     Obsidian statuette of Lolth;100 gp;pg 29
     Green-gold bracelet;25 gp;pg 36

   This is done so that the user can return to the file and write in additional
   items that may have been previously overlooked.


Author & Contact
----------------
Glib Dolotov (gyd102@gmail.com)

Please use the above email to report bugs, suggest or request features, etc.