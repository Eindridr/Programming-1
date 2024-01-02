require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button2 = System::Windows::Forms::Button.new()
		@button1 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		@label7 = System::Windows::Forms::Label.new()
		@label8 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Purple
		@button2.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.HotPink
		@button2.Location = System::Drawing::Point.new(640, 104)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(114, 87)
		@button2.TabIndex = 17
		@button2.Text = "Hide"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Purple
		@button1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.HotPink
		@button1.Location = System::Drawing::Point.new(60, 104)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(125, 87)
		@button1.TabIndex = 16
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Silver
		@label1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(212, 21)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(384, 34)
		@label1.TabIndex = 15
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.Silver
		@label2.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(212, 55)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(384, 34)
		@label2.TabIndex = 18
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.Silver
		@label3.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(212, 89)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(384, 34)
		@label3.TabIndex = 19
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.Silver
		@label4.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(212, 123)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(384, 34)
		@label4.TabIndex = 20
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::Color.Silver
		@label5.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(212, 157)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(384, 34)
		@label5.TabIndex = 21
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::Color.Silver
		@label6.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label6.Location = System::Drawing::Point.new(212, 191)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(384, 34)
		@label6.TabIndex = 22
		@label6.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		@label7.BackColor = System::Drawing::Color.Silver
		@label7.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label7.Location = System::Drawing::Point.new(212, 225)
		@label7.Name = "label7"
		@label7.Size = System::Drawing::Size.new(384, 34)
		@label7.TabIndex = 23
		@label7.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		@label8.BackColor = System::Drawing::Color.Silver
		@label8.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label8.Location = System::Drawing::Point.new(212, 259)
		@label8.Name = "label8"
		@label8.Size = System::Drawing::Size.new(384, 34)
		@label8.TabIndex = 24
		@label8.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(808, 309)
		self.Controls.Add(@label8)
		self.Controls.Add(@label7)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "My Schedule"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Spanish 2"
		@label2.Text = "English 9/10 Honors"
		@label3.Text = "Computer Programming"
		@label4.Text = "Global Studies"
		@label5.Text = "Geometry"
		@label6.Text = "Art 1"
		@label7.Text = "Freshman Seminar"
		@label8.Text = "Chemistry"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
		@label6.Text = ""
		@label7.Text = ""
		@label8.Text = ""
	end
end

