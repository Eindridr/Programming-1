import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Maroon
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label1.Location = System.Drawing.Point(2, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(119, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Maroon
		self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button1.Location = System.Drawing.Point(71, 117)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._textBox1.Location = System.Drawing.Point(129, 11)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._textBox2.Location = System.Drawing.Point(129, 47)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Maroon
		self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label2.Location = System.Drawing.Point(2, 45)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(119, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Pay Periods Per Year:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Maroon
		self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label3.Location = System.Drawing.Point(2, 81)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(119, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Salary Per Pay Period:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Maroon
		self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label4.Location = System.Drawing.Point(129, 81)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Salmon
		self.ClientSize = System.Drawing.Size(230, 152)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg153"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		Salary = float(self._textBox1.Text)
		PP = int(self._textBox2.Text)
		SalaryPPP = Salary/PP
		self._label4.Text = str(round(SalaryPPP, 2))
		
		