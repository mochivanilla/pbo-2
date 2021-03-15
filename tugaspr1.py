# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 0, 128, 128 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.panelhellowx = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelhellowx.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.panelhellowx.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.panelhellowx, wx.ID_ANY, u"\"HELLO WX\"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )


		self.panelhellowx.SetSizer( bSizer2 )
		self.panelhellowx.Layout()
		bSizer2.Fit( self.panelhellowx )
		bSizer1.Add( self.panelhellowx, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.panelnama = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelnama.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self.panelnama, wx.ID_ANY, u"Nama : Raras Dwistian Nuari", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer3.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


		self.panelnama.SetSizer( bSizer3 )
		self.panelnama.Layout()
		bSizer3.Fit( self.panelnama )
		bSizer1.Add( self.panelnama, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.panelnim = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelnim.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self.panelnim, wx.ID_ANY, u"NIM : 192410101060", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer4.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


		self.panelnim.SetSizer( bSizer4 )
		self.panelnim.Layout()
		bSizer4.Fit( self.panelnim )
		bSizer1.Add( self.panelnim, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.panelfoto = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self.panelfoto, wx.ID_ANY, wx.Bitmap( u"../../../Downloads/pbo2-removebg-preview.png", wx.BITMAP_TYPE_ANY ), wx.Point( -1,-1 ), wx.Size( 400,400 ), 0 )
		self.m_bitmap1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer5.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


		self.panelfoto.SetSizer( bSizer5 )
		self.panelfoto.Layout()
		bSizer5.Fit( self.panelfoto )
		bSizer1.Add( self.panelfoto, 1, 0, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


