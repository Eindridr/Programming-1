import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Maroon
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Pick A Car:"
		self._label1.Click += self.Label1Click
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 Firebird",
			"1980 Subaru",
			"1975 Cutlass"]))
		self._comboBox1.Location = System.Drawing.Point(176, 13)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(222, 21)
		self._comboBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 308)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(120, 37)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(138, 308)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(126, 37)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(270, 308)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(123, 37)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(119, 37)
		self._label2.TabIndex = 5
		self._label2.Text = "Miles:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 136)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(119, 37)
		self._label3.TabIndex = 6
		self._label3.Text = "Gallons:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(13, 205)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(119, 37)
		self._label4.TabIndex = 7
		self._label4.Text = "MPG:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Maroon
		self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label5.Location = System.Drawing.Point(176, 64)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(217, 37)
		self._label5.TabIndex = 8
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Maroon
		self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label6.Location = System.Drawing.Point(176, 136)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(217, 37)
		self._label6.TabIndex = 9
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Maroon
		self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label7.Location = System.Drawing.Point(176, 205)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(217, 37)
		self._label7.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightCoral
		self.ClientSize = System.Drawing.Size(405, 357)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54A"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		miles = 1
		gallons = 1
		mpg = 1
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":
			miles = 286
			gallons = 9
			
		
			mpg = miles/float(gallons)
			mpg = round(mpg,10)
		
			self._label5.Text = str(miles)
			self._label6.Text = str(gallons)
			self._label7.Text = str(mpg)
		
		elif car == "1979 Firebird":
			miles = 412
			gallons = 40
			
		
			mpg = miles/float(gallons)
			mpg = round(mpg,10)
		
			self._label5.Text = str(miles)
			self._label6.Text = str(gallons)
			self._label7.Text = str(mpg)
		
		elif car == "1980 Subaru":
			miles = 361
			gallons = 18
			
		
			mpg = miles/float(gallons)
			mpg = round(mpg,10)
		
			self._label5.Text = str(miles)
			self._label6.Text = str(gallons)
			self._label7.Text = str(mpg)
		
		elif car == "1975 Cutlass":
			miles = 161
			gallons = 11
			
		
			mpg = miles/float(gallons)
			mpg = round(mpg,10)
		
			self._label5.Text = str(miles)
			self._label6.Text = str(gallons)
			self._label7.Text = str(mpg)

	def Button2Click(self, sender, e):
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()