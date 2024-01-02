require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button2 = System::Windows::Forms::Button.new()
		@button1 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Silver
		@label1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(212, 26)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(384, 176)
		@label1.TabIndex = 9
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Purple
		@button2.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.HotPink
		@button2.Location = System::Drawing::Point.new(482, 205)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(114, 87)
		@button2.TabIndex = 12
		@button2.Text = "Hide"
		@button2.UseVisualStyleBackColor = false
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Purple
		@button1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.HotPink
		@button1.Location = System::Drawing::Point.new(212, 205)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(124, 87)
		@button1.TabIndex = 13
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(255, 192, 192)
		self.ClientSize = System::Drawing::Size.new(808, 319)
		self.Controls.Add(@button1)
		self.Controls.Add(@button2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Favorite Club"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "DnD Club"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

