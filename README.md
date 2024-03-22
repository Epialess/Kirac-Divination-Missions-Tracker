# Objective
This project aims to keep count of the cards given from multiple Kirac missions for the game "Path of Exile" in the patch 3.22 Ancestor solo-self-found league. I would target the mission "Drops a full stack of divination cards" from Kirac, a non-playable character, in hopes of obtaining high-value cards such as Enlightened, Seven Years Bad Luck, or even a Mageblood (one of the best items in the game) from the Apothecary set. This was done in red and yellow tier crimson temple maps with 0% quantity gear and I would immediately leave the map once I've completed the mission.

This program, "kiracMagebloodPls.py", lets the user add cards to a list as well as show the order in which they've obtained them (options 1 and 2). The results are put in the file "kiricList.txt". The first string of each line shows the mission number, starting from 0, and the second shows the card set that was obtained. If the user makes a mistake in adding an entry, option 3 will delete the latest entry from the text file.

Finally, option 4 calculates and counts the total number of each card set and its percentage of occurrence in the total pool of missions. The results are put in the file "kiricStats.txt".

Another method of obtaining the number of card set occurrences is using the bash script “kiracCount.sh”, however, the percentages and cards that are not obtained will not show up on the screen. 

## Results
Taken directly from kiricStats.txt:
```
Card                          # of Sets      Percentage
Lucky Deck                        1                0.82
The Opulent                       30              24.59
Lingering Remnants                4                3.28
The Encroaching Darkness          5                4.10
The Journalist                    27              22.13
The Blazing Fire                  34              27.87
The Trial                         2                1.64
The Gambler                       19              15.57
Her Mask                          0                0.00
Hope                              0                0.00
Seven Years Bad Luck              0                0.00
The Dragon's Heart                0                0.00
The Enlightened                   0                0.00
The Life Thief                    0                0.00
The Lord of Celebration           0                0.00
The Tinkerer's Table              0                0.00
The Apothecary                    0                0.00

Total                            122                100
```
With a total of 122 Kirac missions, I did not hit any high-value card sets sadly. :( 