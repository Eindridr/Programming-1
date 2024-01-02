import math
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
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightCoral
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(528, 413)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(241, 47)
		self._button3.TabIndex = 15
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightCoral
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(251, 413)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(271, 47)
		self._button2.TabIndex = 14
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightCoral
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(3, 413)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(242, 47)
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
		self._listBox1.Location = System.Drawing.Point(3, 3)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(766, 404)
		self._listBox1.TabIndex = 12
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(773, 461)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122i"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		cb = 0
		cbrt = 0
		heading = "Num\t\tCube\t\tCubeRt"
		self._listBox1.Items.Add(heading)		
		for num in range(25, -1, -1):
			cb = num**3
			cbrt = num**0.3333333
			cbrt = round(cbrt, 5)
			if num is 0:
				msg = str(num) + "\t\t" + str(cb) + "\t\t" + str(cbrt)
			else:
				msg = "-" + str(num) + "\t\t" + "-" + str(cb) + "\t\t" + "-" + str(cbrt)
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()