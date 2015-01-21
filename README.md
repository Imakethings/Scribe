Scribe is a commandline application for [myAnimeList][1].

# Getting started with scribe.

Download the tarbal or clone this repository and run ``` make ```. This should only take a few seconds becaus we're not *that* big. That's it! You're ready to start using **scribe**.

## Commands

Scribe has litte yet difficult commands and things tend to get pretty big with all the parameters available. You can make it as advanced as you want in one line and make every search or add unique.

---------

### Verify

You're going to have to verify yourself to the application. You can do this by executing ``` $ scribe --set-username <value> ``` and ``` $ scribe --set-password <value> ```. These are both to be set to prevent having to enter either every time. Unfortunately there is no way to make authenticating safer because *myAnimeList* doesn't support anything yet. (We hope this will change one day)

---------

You should then be good to try and test your credentials by running

```bash
$ scribe --verify
```

If everything went according to plan you should see

> The user *username* has succesfully verified. (*id*)

### Search

I tried making search easy yet very effective. A raw call would be: ``` --search <value> ```. This doesn't of course do very much, let's add the title and the synopsis: ``` -ld --search <value> ```. I would like to limit the search results to 3 and I only need a brief description of the anime. We easily add it this way: ``` --ld -n 3 -w 70 --search <value> ```. 

---------

Parameter|value|
---------|-----|
-i|Id|
-l|Title|
-e|English|
-c|Score|
-t|Type|
-p|Episodes|
-y|Synonyms|
-u|Status|
-r|Start date|
-f|End date|
-d|Synopsis|
-g|Image|

Parameter|argument|description|
---------|--------|-----------|
-w  |**int**| How many results we should show. |
-n  |**int**| The length of the synopsis.|

### Add
