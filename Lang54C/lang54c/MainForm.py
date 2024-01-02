import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightCoral
		self._button1.Location = System.Drawing.Point(12, 281)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightCoral
		self._button2.Location = System.Drawing.Point(119, 281)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightCoral
		self._button3.Location = System.Drawing.Point(222, 280)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightCoral
		self._label1.Location = System.Drawing.Point(156, 222)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(141, 23)
		self._label1.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightCoral
		self._label2.Location = System.Drawing.Point(156, 255)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(141, 23)
		self._label2.TabIndex = 4
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightCoral
		self._textBox1.Location = System.Drawing.Point(108, 28)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightCoral
		self._label3.Location = System.Drawing.Point(9, 222)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(150, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Area:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightCoral
		self._label4.Location = System.Drawing.Point(9, 255)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(150, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Circ:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(309, 316)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = 3.14159
		Rad = int(self._textBox1.Text)
		Area = pi * Rad**2
		Circ = Rad * 2 * pi
		
		self._label1.Text = str(Area)
		self._label2.Text = str(Circ)

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._textBox1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()