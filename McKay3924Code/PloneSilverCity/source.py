# $Id: source.py,v 1.3 2003/12/10 01:25:48 zopezen Exp $
# Copyright: ClearWind Consulting Ltd

from SilverCity import LanguageInfo 
from StringIO import StringIO

# add in extra extensions
LanguageInfo.add_extension("python", "cpy")
LanguageInfo.add_extension("python", "vpy")
LanguageInfo.add_extension("html", "pt")
LanguageInfo.add_extension("html", "cpt")

def create_generator(source_file_name=None, generator_name=None):
    """ Make a generator from the given information
    about the object, such as its source and type """
    if generator_name:
        return LanguageInfo.find_generator_by_name(generator_name)()
    else:
        if source_file_name:
            try:
                h = LanguageInfo.guess_language_for_file(source_file_name)
                return h.get_default_html_generator()()
            except IOError:
                # this means silvercity tried to the file and failed
                raise ValueError, "Unknown extension for '%s', cannot create lexer" % source_file_name
                
        else:
            raise ValueError, "Unknown file type, cannot create lexer"

def list_generators():
    """ This returns a list of generators, a generator
    is a valid language, so these are things like perl,
    python, xml etc..."""
    lexers = LanguageInfo.get_generator_names_descriptions()
    return lexers

def generate_html(source_file, generator=None, source_file_name=None):
    """ From the source make a generator
    and then make the html """
    
    # SilverCity requires a file like object
    target_file = StringIO()
    generator = create_generator(source_file_name, generator)
    generator.generate_html(target_file, source_file)
    
    # return the html back
    return target_file.getvalue(), generator.name

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    fh = open(file, 'r').read()
    #print generate_html(file, generator="python")
    #print list_generators()
    l = LanguageInfo.guess_language_for_file(file)
    text = generate_html(fh, generator=l.language_name)

    template = open('template.html', 'r').read()
    template = template % text[0]

    out = open('out.html', 'w')
    out.write(template)
    
