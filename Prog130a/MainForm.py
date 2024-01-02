import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightCoral
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(193, 239)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(89, 47)
		self._button3.TabIndex = 15
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightCoral
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(98, 239)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(89, 47)
		self._button2.TabIndex = 14
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightCoral
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(3, 239)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 47)
		self._button1.TabIndex = 13
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.LightCoral
		self._listBox1.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 40
		self._listBox1.Location = System.Drawing.Point(3, 29)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(279, 204)
		self._listBox1.TabIndex = 12
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(3, 3)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(279, 20)
		self._textBox1.TabIndex = 16
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(287, 288)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog130a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num = self.textBox1.Text
		if num % 2 == 0:
			num = num / 2
		else:
			num = (num * 3) + 1
		msg = num
		self._listBox1.Items.Add(msg)