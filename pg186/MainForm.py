import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label9 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(172, 155)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Tickets Sold"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(5, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(167, 29)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the number of tickets sold for each class of seats"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(6, 52)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(81, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Class A:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(6, 69)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(81, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Class B:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(6, 86)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(81, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Class C:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(56, 52)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(56, 69)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(56, 86)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label13)
		self._groupBox2.Controls.Add(self._label12)
		self._groupBox2.Controls.Add(self._label10)
		self._groupBox2.Controls.Add(self._label11)
		self._groupBox2.Controls.Add(self._label9)
		self._groupBox2.Controls.Add(self._label5)
		self._groupBox2.Controls.Add(self._label6)
		self._groupBox2.Controls.Add(self._label7)
		self._groupBox2.Controls.Add(self._label8)
		self._groupBox2.Location = System.Drawing.Point(190, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(172, 155)
		self._groupBox2.TabIndex = 7
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Tickets Sold"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(6, 86)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(81, 23)
		self._label5.TabIndex = 3
		self._label5.Text = "Class C:"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(6, 69)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(81, 23)
		self._label6.TabIndex = 2
		self._label6.Text = "Class B:"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(6, 52)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(81, 23)
		self._label7.TabIndex = 1
		self._label7.Text = "Class A:"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(5, 16)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(167, 29)
		self._label8.TabIndex = 0
		self._label8.Text = "Enter the number of tickets sold for each class of seats"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(24, 181)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(144, 181)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(271, 181)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(5, 129)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(81, 23)
		self._label9.TabIndex = 7
		self._label9.Text = "Total Revenue:"
		# 
		# label11
		# 
		self._label11.Location = System.Drawing.Point(52, 69)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(110, 17)
		self._label11.TabIndex = 9
		# 
		# label10
		# 
		self._label10.Location = System.Drawing.Point(52, 52)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(110, 17)
		self._label10.TabIndex = 10
		# 
		# label12
		# 
		self._label12.Location = System.Drawing.Point(52, 86)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(110, 17)
		self._label12.TabIndex = 11
		# 
		# label13
		# 
		self._label13.Location = System.Drawing.Point(81, 129)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(91, 17)
		self._label13.TabIndex = 12
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(370, 216)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "pg186"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label10.Text = str(int(self._textBox1.Text)*15)
		self._label11.Text = str(int(self._textBox1.Text)*12)
		self._label12.Text = str(int(self._textBox1.Text)*9)
		self._label13.Text = str(int(self._label10.Text) + int(self._label11.Text) + int(self._label12.Text))


	def Button2Click(self, sender, e):
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()