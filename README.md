### Convert Units REST Service
The web service is a single endpoint which converts any properly formatted unit string to their SI counterparts.

# Example Usage
~~~
METHOD: GET
PATH: /units/si
PARAMS: units - A unit string*
RETURNS: conversion - A conversion object**
~~~