from AppKit import *

PATH = '../source/Parametric-avar2/'

DEFAULT = 'RobotoAvar2-wght400.ufo'

SOURCES = [                        'RobotoAvar2-XOPQ2.ufo',            'RobotoAvar2-XOPQ310.ufo',
            'RobotoAvar2-XTRA244.ufo',            'RobotoAvar2-XTRA741.ufo',            'RobotoAvar2-YOPQ2.ufo',            'RobotoAvar2-YOPQ280.ufo',
            
        ]

asciiGlyphs = 'space exclam quotedbl numbersign dollar percent ampersand quotesingle parenleft parenright asterisk plus comma hyphen period slash zero one two three four five six seven eight nine colon semicolon less equal greater question at A B C D E F G H I J K L M N O P Q R S T U V W X Y Z bracketleft backslash bracketright asciicircum underscore grave a b c d e f g h i j k l m n o p q r s t u v w x y z braceleft bar braceright asciitilde'.split()
        
def checkSedebearings(fonts):
    
    for font in fonts:
        
        fontName1 = PATH + DEFAULT
        fontName2 = PATH + font
            
        font1 = OpenFont(fontName1, showInterface=False)
        font2 = OpenFont(fontName2, showInterface=False)

        strDifferences = ''


        for glyph in asciiGlyphs:
    
            if font1[glyph].leftMargin != font2[glyph].leftMargin:
                
                strDifferences += 'LEFT Sidebearing difference in :' + glyph + ',' + str(font1[glyph].leftMargin) + ' ' + str(font2[glyph].leftMargin) + '\n'
            
            if font1[glyph].rightMargin != font2[glyph].rightMargin:
        
                strDifferences += 'RIGHT Sidebearing difference in :' + glyph + ',' + str(font1[glyph].rightMargin) + ' ' + str(font2[glyph].rightMargin) + '\n'        
                    

        #font2.save()
        
        if len(strDifferences) == 0:
    
            #s = NSSpeechSynthesizer.alloc().init()
            #s.startSpeakingString_("Finished. There are no width differences in Google Sans Flex. Yay!")
            print( '🙂🙂🙂 No width differences betweeen ' + fontName1 + ' & ' +fontName2 )
        else:
            #s = NSSpeechSynthesizer.alloc().init()
            #s.startSpeakingString_("FUCK")
            print( '😡😡😡 Width differences betweeen ' + fontName1 + ' & ' +fontName2 )
            print(strDifferences)
        
        font1.close()
        font2.close()
            


checkSedebearings(SOURCES)







