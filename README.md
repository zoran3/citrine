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

\*\*A valid conversion object is a JSON object containing two fields: unit_name and multiplication_factor .
unit_name is the unit string from the request, with all units converted to to their SI counterpart. Reducing units is not necessary,
so s/s is perfectly valid output. The parentheses should match the request unit string. multiplication_factor is a
floating point number (with 14 significant digits) that you can use to convert any input in the original units to the new SI units.

*Example Request:*

~~~
GET /units/si?units=(degree/minute)
~~~
~~~
{
   "unit_name": "(rad/s)",
   "multiplication_factor": .00029088820867
}
~~~

*Unit Conversion Factors*

This table denotes valid input and conversion factors for you to implement. Either values from the left two columns are valid input,
as are SI units themselves.

|Name|Symbol| Quantity |SI Conversion|
|----|------|----------|-------------|
|minute| min |time| 60s|
|hour| h |time |3600s|
|day| d| time| 86400s|
|degree| ° |unitless/plane angle| (π/180) rad|
|arcminute|'|unitless/plane angle| (π/10800) rad|
|arcsecond|"| unitless/plane angle| (π/648000) rad|
|hectare| ha| area| 10000 m2|
|litre| L| volume| 0.001 m3|
|tonne| t| mass| 1000 kg|

*Heroku Deployment*
~~~
git push heroku master
~~~
