import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("Prog58t.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._pictureBox1.BeginInit()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Maroon
		self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button1.Location = System.Drawing.Point(12, 115)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Maroon
		self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button2.Location = System.Drawing.Point(229, 115)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button3.Location = System.Drawing.Point(445, 115)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# pictureBox1
		# 
		self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
		self._pictureBox1.Location = System.Drawing.Point(-11, 153)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(550, 431)
		self._pictureBox1.TabIndex = 3
		self._pictureBox1.TabStop = False
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 44)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(233, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(287, 44)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(233, 20)
		self._textBox2.TabIndex = 6
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Maroon
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label1.Location = System.Drawing.Point(0, 0)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(75, 42)
		self._label1.TabIndex = 0
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Maroon
		self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label2.Location = System.Drawing.Point(108, 0)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(75, 42)
		self._label2.TabIndex = 1
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Maroon
		self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label3.Location = System.Drawing.Point(217, 0)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(75, 42)
		self._label3.TabIndex = 2
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Maroon
		self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label4.Location = System.Drawing.Point(328, 0)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(75, 42)
		self._label4.TabIndex = 3
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Maroon
		self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label5.Location = System.Drawing.Point(433, 0)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(75, 42)
		self._label5.TabIndex = 4
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(12, 70)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(508, 42)
		self._groupBox1.TabIndex = 7
		self._groupBox1.TabStop = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightCoral
		self.ClientSize = System.Drawing.Size(532, 147)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog58t"
		self._pictureBox1.EndInit()
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Giv = float(self._textBox2.Text)
		Due = float(self._textBox1.Text)
		Dol = str(Giv - Due)
		self._label1.Text = str(Dol)
		Qrt = Dol // .25
		self._label2.Text = str(Qrt)
		Dime = Dol // .10
		self._label3.Text = str(Dime)
		Nic = Dol // .05
		self._label4.Text = str(Nic)
		Pen = Dol // .01
		self._label5.Text = str(Pen)