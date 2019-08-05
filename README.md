### Convert Units REST Service
The web service is a single endpoint which converts any properly formatted unit string to their SI counterparts.

# Example Usage
~~~
METHOD: GET
PATH: /units/si
PARAMS: units - A unit string*
RETURNS: conversion - A conversion object**
~~~

\*A valid unit string is a string containing any number of units multiplied or divided, potentially containing parentheses. Valid
examples include degree , degree/minute , (degree/(minute\*hectare)) , ha\*°