try:
    from tkinter.font import BOLD
    from dataclasses import dataclass
    from typing import (final , AnyStr)
    from tkinter.constants import (CENTER , BOTH , NORMAL)
    
except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Import Materials') from None

finally:
    ...
    
    




@final
@dataclass
class Materials:
    
    @final
    @dataclass(kw_only=True)
    class FontWeights:
        bold: str | AnyStr = BOLD
    
        
    @final
    @dataclass(kw_only=True)
    class Fonts:
        vani: str | AnyStr = 'Vani'
        
        
    @final
    @dataclass(kw_only=True)
    class States:
        normal: str | AnyStr = NORMAL
        
        
    @final
    @dataclass(kw_only=True)
    class Cursors:
        hand: str | AnyStr = 'hand2'
    
    
    @final
    @dataclass(kw_only=True)
    class Colors:
        dark : str | AnyStr = '#1C1C1C'
        blue : str | AnyStr = '#4169E1'
        green: str | AnyStr = '#32CD32'
        orange: str | AnyStr = '#FF4500'
        white : str | AnyStr = '#ffffff'
        black : str | AnyStr = '#000000'
        yellow: str | AnyStr = '#F1C40F'
        purple: str | AnyStr = '#6A5ACD'
        golden: str | AnyStr = '#B8860B'
        darkOrange : str | AnyStr = '#FF8C00'
        burlyWood : str | AnyStr = '#DEB887'
    
    
    @final
    @dataclass(kw_only=True)
    class Themes:
        DARK : str | AnyStr = 'Dark'
        LIGHT : str | AnyStr = 'Light'

    
    @final
    @dataclass(kw_only=True)
    class Alignments:
        both: str | AnyStr = BOTH
        center: str | AnyStr = CENTER