require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox


class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@button3 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button1 = System::Windows::Forms::Button.new()
		@label4 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(260, 77)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(100, 20)
		@textBox2.TabIndex = 17
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(260, 13)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 20)
		@textBox1.TabIndex = 16
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(553, 245)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(278, 74)
		@button3.TabIndex = 15
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(269, 245)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(278, 71)
		@button2.TabIndex = 14
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(-15, 245)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(278, 71)
		@button1.TabIndex = 13
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = true
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.SandyBrown
		@label4.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(20, 189)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(745, 53)
		@label4.TabIndex = 12
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.SandyBrown
		@label3.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(20, 125)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(745, 52)
		@label3.TabIndex = 11
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(20, 61)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(303, 51)
		@label2.TabIndex = 10
		@label2.Text = "Width:"
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Comic Sans MS", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(20, -2)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(303, 57)
		@label1.TabIndex = 9
		@label1.Text = "Length:"
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.BurlyWood
		self.ClientSize = System::Drawing::Size.new(836, 322)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Lang54C"
		self.ResumeLayout(false)
		self.PerformLayout()
	end
end

