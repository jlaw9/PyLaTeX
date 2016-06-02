# -*- coding: utf-8 -*-

import os
import subprocess
import errno
from .base_classes import Environment, Command
from .package import Package
from .utils import dumps_list, rm_temp_dir, NoEscape

class Header(Command):
    r""" A class which describes the header that will be displayed at the top
        of every page of a document
    """
    def __init__(self, lhead=None, chead=None, rhead=None, lfoot=None,
            cfoot=None, rfoot=None, header_thickness=0,
            footer_thickness=0, header_height=12, footer_height=12):
        r""" Initializes the header and sets its attributes 
            
            Args
            ----
            lhead: str
                Left header
            chead: str
                Center header
            rhead: str
                Right header
            lfoot: str
                Left footer
            cfoot: str
                Center footer
            rfoot: str
                Right footer
            header_thickness: float
                Header underline thickness measured in pt
            footer_thickness: float
                Footer underline thickness measured in pt
            header_height: float
                Header height in pt
            footer_height: float
                Footer height in pt
        """

        self._latex_name = "fancyhf"

        packages = [Package("fancyhdr")]

        self.set_lhead(lhead)
        self.set_chead(chead)
        self.set_rhead(rhead)
        self.set_lfoot(lfoot)
        self.set_cfoot(cfoot)
        self.set_rfoot(rfoot)
        self.set_header_thickness(header_thickness)
        self.set_footer_thickness(footer_thickness)
        self.set_header_height(header_height)
        self.set_footer_height(footer_height)

        super().__init__(command=self._latex_name, packages=packages)

    def dumps(self):
        r""" Converts the header to a Latex string
            
            Returns
            -------
            str
                the value of the Latex string
        """

        head = super().dumps() + '{}\n'
        
        head += Command("pagestyle", arguments="fancy").dumps() + '\n'
        
        head += Command("renewcommand", arguments=[NoEscape(r'\headrulewidth'),
            self.header_thickness]).dumps() + '\n'

        head += Command("renewcommand", arguments=[NoEscape(r'\footrulewidth'),
            self.footer_thickness]).dumps() + '\n'
        
        head += Command("setlength", arguments=[NoEscape(r'\headheight'),
            self.header_height]).dumps() + '\n'

        head += Command("setlength", arguments=[NoEscape(r'\footheight'),
            self.footer_height]).dumps() + '\n'

        if self.lhead is not None:
            head += Command("lhead",arguments=NoEscape(self.lhead)).dumps() + '\n'
        if self.chead is not None:
            head += Command("chead",arguments=NoEscape(self.chead)).dumps() + '\n'
        if self.rhead is not None:
            head += Command("rhead",arguments=NoEscape(self.rhead)).dumps() + '\n'
        if self.lfoot is not None:
            head += Command("lfoot",arguments=NoEscape(self.lfoot)).dumps()+ '\n'
        if self.cfoot is not None:
            head += Command("cfoot",arguments=NoEscape(self.cfoot)).dumps() + '\n'
        if self.rfoot is not None:
            head += Command("rfoot",arguments=NoEscape(self.rfoot)).dumps() + '\n'

        return head


    def set_lhead(self, lhead):
        r""" Sets the left header of the document

            Args
            ----
            lhead: str
                Value to set for the left header
        """
        
        if lhead is not None:
            self.lhead = lhead.replace('\n', r'\linebreak')
        else:
            self.lhead = None


    def set_chead(self, chead):
        r""" Sets the center header of the document

            Args
            ----
            chead: str
                Value to set for the center header
        """

        if chead is not None:
            self.chead = chead.replace('\n', r'\linebreak')
        else:
            self.chead = None

    def set_rhead(self, rhead):
        r""" Sets the right header of the document

            Args
            ----
            rhead: str
                Value to set for the right header
        """
  
        if rhead is not None:
            self.rhead = rhead.replace('\n', r'\linebreak')
        else:
            self.rhead = None

    def set_lfoot(self, lfoot):
        r""" Sets the left footer of the document

            Args
            ----
            lfoot: str
                Value to set for the left footer
        """

        if lfoot is not None:
            self.lfoot = lfoot.replace('\n', r'\linebreak')
        else:
            self.lfoot = None

    def set_cfoot(self, cfoot):
        r""" Sets the center footer of the document

            Args
            ----
            cfoot: str
                Value to set for the center footer
        """
        if cfoot is not None:
            self.cfoot = cfoot.replace('\n', r'\linebreak')
        else:
            self.cfoot = None

    def set_rfoot(self, rfoot):
        r""" Sets the right footer of the document

            Args
            ----
            rfoot: str
                Value to set for the right footer
        """
        if rfoot is not None:
            self.rfoot = rfoot.replace('\n', r'\linebreak')
        else:
            self.rfoot = None

    def set_header_thickness(self, thickness):
        r""" Sets the thickness of the line under the header

            Args
            ----
            thickness: float
                Value to set for the header thickness in pt
        """

        self.header_thickness = str(thickness) + 'pt'
        
    def set_footer_thickness(self, thickness):
        r""" Sets the thickness of the line over the footer

            Args
            ----
            thickness: float
                Value to set for the footer thickness in pt
        """

        self.footer_thickness = str(thickness) + 'pt'

    def set_header_height(self, height):
        r""" Sets the height of the header

            Args
            ----
            height: float
                Value to set for the header height in pt
        """

        self.header_height = str(height) + 'pt'

    def set_footer_height(self, height):
        r""" Sets the height of the footer

            Args
            ----
            height: float
                Value to set for the footer height in pt
        """

        self.footer_height = str(height) + 'pt'


