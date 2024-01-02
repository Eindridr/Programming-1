require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label5 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@button2 = System::Windows::Forms::Button.new()
		@button1 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::Color.Silver
		@label5.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(12, 141)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(518, 34)
		@label5.TabIndex = 30
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.Silver
		@label4.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(12, 107)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(518, 34)
		@label4.TabIndex = 29
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.Silver
		@label3.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(12, 73)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(518, 34)
		@label3.TabIndex = 28
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.Silver
		@label2.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(12, 39)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(518, 34)
		@label2.TabIndex = 27
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Purple
		@button2.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.HotPink
		@button2.Location = System::Drawing::Point.new(416, 213)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(114, 87)
		@button2.TabIndex = 26
		@button2.Text = "Hide"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Purple
		@button1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.HotPink
		@button1.Location = System::Drawing::Point.new(12, 213)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(125, 87)
		@button1.TabIndex = 25
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Silver
		@label1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(12, 5)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(518, 34)
		@label1.TabIndex = 24
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(793, 312)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Phone Numbers"
		self.ResumeLayout(false)
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		@label1.Text = "Pizza Hut: 608 754 7090"
		@label2.Text = "Play Station: 877 971 7669"
		@label3.Text = "Panda Garden: 608 754 5535"
		@label4.Text = "Kwik Trip: 608 754 8803"
		@label5.Text = "McDonalds: 608 752 7521"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
	end
end

