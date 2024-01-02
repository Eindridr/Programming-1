import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(150, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(69, 197)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(150, 197)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(231, 197)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(140, 52)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(120, 95)
		self._listBox1.TabIndex = 5
		self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(423, 252)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def ListBox1SelectedIndexChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		x = 0
		y = int(self._textBox1.Text)
		z = 0
		for num in range(0, y+1, +2):
			x += 2
			while x < y:
				x += 2
				self._listBox1.Items.Add(str(y) + "\t" + str(x))

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()