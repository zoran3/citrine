from flask import Flask
from flask import jsonify
from flask import request
from datetime import datetime
import math
app = Flask(__name__)
from flask.json import JSONEncoder

class MiniJSONEncoder(JSONEncoder):
    """Minify JSON output."""
    item_separator = ','
    key_separator = ':'

app = Flask(__name__)
app.json_encoder = MiniJSONEncoder
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["JSON_SORT_KEYS"] = False
app.config["JSON_AS_ASCII"] = False

unit_word_hash = {
    "minute": str(60),
    "hour": str(3600),
    "day": str(86400),
    "degree": str(math.pi/180),
    "arcminute": str(math.pi/10800),
    "arcsecond": str(math.pi/648000),
    "hectare": str(10000),
    "litre": str(0.001),
    "tonne": str(1000)
}

unit_initials_hash = {
    "min": str(60),
    "ha": str(10000),
}

unit_initial_hash = {
    "h": str(3600),
    "d": str(86400),
    u'\xb0': str(math.pi/180),
    "'": str(math.pi/10800),
    '"': str(math.pi/648000),
    "L": str(0.001),
    "t": str(1000)
}

unit_name_word_hash = {
    "minute": "s",
    "hour": "s",
    "day": "s",
    "degree": "rad",
    "arcminute": "rad",
    "arcsecond": "rad",
    "hectare": 'm\N{SUPERSCRIPT TWO}',
    "litre": 'm\N{SUPERSCRIPT THREE}',
    "tonne": 'kg'
}

unit_name_initials_hash = {
    "min": "s",
    "ha": 'm\N{SUPERSCRIPT TWO}',
}

unit_name_initial_hash = {
    "h": "s",
    "d": "s",
    u'\xb0': "rad",
    "'": "rad",
    '"': "rad",
    "L": 'm\N{SUPERSCRIPT THREE}',
    "t": 'kg'
}

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

@app.route('/units/si')
def get_conversion_factor():
    units = request.args.get('units')
    units_val = keymap_replace(units, unit_word_hash)
    units_val = keymap_replace(units_val, unit_initials_hash)
    units_val = keymap_replace(units_val, unit_initial_hash)
    factor = '%.14f' % eval(units_val)
    unit_name =  keymap_replace(units, unit_name_word_hash)
    unit_name = keymap_replace(unit_name, unit_name_initials_hash)
    unit_name = keymap_replace(unit_name, unit_name_initial_hash)
    unit_name = keymap_replace(unit_name, {"ras": "rad"})
    
    return jsonify(
        unit_name = unit_name, 
        multiplication_factor = factor)
    

def keymap_replace(
        string: str, 
        mappings: dict,
        lower_keys=False,
        lower_values=False,
        lower_string=False,
    ) -> str:
    """Replace parts of a string based on a dictionary.

    This function takes a string a dictionary of
    replacement mappings. For example, if I supplied
    the string "Hello world.", and the mappings 
    {"H": "J", ".": "!"}, it would return "Jello world!".

    Keyword arguments:
    string       -- The string to replace characters in.
    mappings     -- A dictionary of replacement mappings.
    lower_keys   -- Whether or not to lower the keys in mappings.
    lower_values -- Whether or not to lower the values in mappings.
    lower_string -- Whether or not to lower the input string.
    """
    replaced_string = string.lower() if lower_string else string
    for character, replacement in mappings.items():
        replaced_string = replaced_string.replace(
            character.lower() if lower_keys else character,
            replacement.lower() if lower_values else replacement
        )
    return replaced_string
