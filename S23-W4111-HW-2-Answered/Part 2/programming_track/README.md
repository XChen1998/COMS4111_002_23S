# Homework and Project Tasks

## Homework 2

A post of Ed will document the format for submitting the programming track assignment for HW 2.

The tasks are the following. You simply implement the following methods.

- ```ArtistResource.get(primaryName, birthYear, deathYear)```: This returns a list of ```ArtistRsp```
models for entries in ```name_basics_all``` that match the pattern. A parameter may be None. Assume that
```primaryName``` is "Tom Hanks" and ```birthYear``` is "1960".  The result is a query of the
form
```
select * from name_basics_all where primaryName='Tom Hanks' and borthYear='1960'
```

- ```ArtistResource.delete(primaryName, birthYear, deathYear)```: Same pattern as ```get``` but deletes
the matching rows and returns the number of rows affected.


- ```ArtistResource.update(primaryName, birthYear, deathYear, newValues)```:
  - Same pattern as ```get``` but for matching rows.
  - Updates matching rows setting columns to fields in ```newValues```. ```newValues``` may have a subset
of the possible attributes.


- ```ArtistResource.post(newValues)```:
  - Creates a new resource.
  - ```newValues``` contains the column values for the new resource.


__Note:__ Students should focus on ```ArtistsResource``` and simply testing the methods. The professor
is working on making ```main.py``` and the ```pydantic``` information better.


