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
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox5 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Thistle
		@button1.Location = System::Drawing::Point.new(12, 299)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(132, 33)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Thistle
		@button2.Location = System::Drawing::Point.new(288, 299)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(132, 33)
		@button2.TabIndex = 1
		@button2.Text = "Exit"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.Thistle
		@button3.Location = System::Drawing::Point.new(150, 299)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(132, 33)
		@button3.TabIndex = 2
		@button3.Text = "Clear"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.LavenderBlush
		@label1.Location = System::Drawing::Point.new(12, 248)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(408, 23)
		@label1.TabIndex = 3
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.LavenderBlush
		@label2.Location = System::Drawing::Point.new(12, 271)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(408, 23)
		@label2.TabIndex = 4
		@label2.Click { |sender, e| self.Label2Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(56, 112)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 20)
		@textBox1.TabIndex = 5
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(56, 164)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(100, 20)
		@textBox3.TabIndex = 7
		# 
		# textBox5
		# 
		@textBox5.Location = System::Drawing::Point.new(56, 138)
		@textBox5.Name = "textBox5"
		@textBox5.Size = System::Drawing::Size.new(100, 20)
		@textBox5.TabIndex = 9
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.HotPink
		self.ClientSize = System::Drawing::Size.new(848, 344)
		self.Controls.Add(@textBox5)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prong58b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button3Click(sender, e)
		@label2.Text = ""
		@label1.Text = ""
		@textBox1.Text = ""
		@textBox5.Text = ""
		@textBox3.Text = ""
	end

	def Label2Click(sender, e)
		
	end

	def Button2Click(sender, e)
		Application.Exit
	end
end

