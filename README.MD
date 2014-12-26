
# Scribe

## Listing.

```python
scribe -watch
```
Returns a list of things you have to watch

```python
scribe -viewing
```
Returns the list of things you are viewing

```python
scribe -finished
```
Returns a list of things you finished (Showoff!)

## Manipulating.

```python
scribe -add [-Ww, -Vv, -Ff] <name> <opt:episodes>
```
Adds specific anime to said list if it doesn't exist already

```python
scribe -remove [-Ww, -Vv, -Ff] <name>
```
Removes specific anime from said list if it exists.

```python
scribe -view <name> 
```
Moves name from the -watch to the -viewing list.

```python
scribe -finish <name>
```
Moves name from the -viewing to the -finished list.

## Syncing.

```python
scribe -username <username>
```
Stores your www.myanimelist.net username.

```python
scribe -password <password>
```
Stores your www.myanimelist.net password.
----------
Do this at own risk! We will prompt you for your password each sync if left empty.
