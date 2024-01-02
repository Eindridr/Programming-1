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
		self.SuspendLayout()
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(411, 213)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(114, 87)
		@button2.TabIndex = 5
		@button2.Text = "Hide"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(141, 213)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(125, 87)
		@button1.TabIndex = 4
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Silver
		@label1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(141, 34)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(384, 176)
		@label1.TabIndex = 3
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(667, 335)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Test"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Winter Gilbertson"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

