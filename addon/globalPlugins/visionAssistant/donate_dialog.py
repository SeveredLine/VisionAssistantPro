# donate_dialog.py
import addonHandler
import gui
import wx

addonHandler.initTranslation()

class DonationDialog(gui.nvdaControls.MessageDialog):
	TON_ADDRESS = "UQDoOOOoDYPP8eqWXVsjVyYzulY72JLZK1grPS_O2DbgVNsc"
	USDT_ADDRESS = "TBCEdrBaYfUKKW8ZXjHxUuHrijFjWcNBsi"

	def __init__(self, parent, title, message):
		super().__init__(parent, title, message, dialogType=gui.nvdaControls.MessageDialog.DIALOG_TYPE_WARNING)

	def _addButtons(self, buttonHelper):
		# Translators: Label for the button to copy the TON cryptocurrency wallet address.
		tonBtn = buttonHelper.addButton(self, label=_("Copy TON Address"), name="TON_ADDRESS")
		# Translators: Label for the button to copy the USDT (TRC20 network) wallet address.
		usdtBtn = buttonHelper.addButton(self, label=_("Copy USDT (TRC20) Address"), name="USDT_ADDRESS")
		
		tonBtn.Bind(wx.EVT_BUTTON, self.onCopyAction)
		usdtBtn.Bind(wx.EVT_BUTTON, self.onCopyAction)
		
		# Translators: Button to dismiss the donation dialog without taking any action.
		cancelBtn = buttonHelper.addButton(self, id=wx.ID_CANCEL, label=_("Maybe Later"))
		cancelBtn.Bind(wx.EVT_BUTTON, lambda evt: self.EndModal(wx.CANCEL))

	def onCopyAction(self, evt):
		try:
			import api
			donateBtn = evt.GetEventObject()
			address = getattr(self, donateBtn.Name)
			api.copyToClip(address)
			
			# Translators: Success message shown after a wallet address is copied to the clipboard.
			copy_msg = _("Address copied to clipboard! If you'd like, you can now proceed to your wallet and donate any amount you can. Your support is greatly appreciated!")
			# Translators: Title for the success message box.
			copy_title = _("Success")
			wx.MessageBox(copy_msg, copy_title, wx.OK | wx.ICON_INFORMATION)
		except:
			pass
		self.EndModal(wx.OK)

def requestDonations(parentWindow):
	addon = addonHandler.getCodeAddon()
	addon_summary = addon.manifest['summary']
	
	# Translators: Title of the donation request dialog.
	title = _("Support the Future of {name}").format(name=addon_summary)
	
	# Translators: The main message of the donation dialog. 
	message = _(
		"{name} is a project born from a personal vision to bridge the gap between AI and true accessibility. "
		"The initial concept and many of the features you enjoy were created from my own ideas to solve real challenges and provide a new level of digital independence.\n\n"
		"I take great pride in thinking through every detail and turning both my own innovations and your valuable requests into reality. "
		"Ensuring this tool remains fast, stable, and constantly evolving is a continuous creative journey that I am passionate about pursuing.\n\n"
		"If this assistant has brought value to your daily life, your support is a wonderful way to show appreciation for the original work and the dedication behind it. "
		"It provides the extra motivation to keep the inspiration alive and ensures we can continue to push the boundaries together. "
		"Thank you for being part of this mission!"
	).format(name=addon_summary)
	
	return DonationDialog(parentWindow, title, message).ShowModal()