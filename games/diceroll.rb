system('clear')
puts 'Dice Rolling Simulator'
puts 'Roll The Dice: '
q = gets.chomp
x = 0
while 1 > x
s = Time.now
f = s + 1.5
while Time.now < f
system('clear')
a = rand(1..6)
b = rand(1..6)
if a == 1 or b == 1
  puts '-----'
  puts '|   |'
  puts '| o |'
  puts '|   |'
  puts '-----'
end
if a == 2 or b == 2
  puts '-----'
  puts '|o  |'
  puts '|   |'
  puts '|  o|'
  puts '-----'
end
if a == 3 or b == 3
  puts '-----'
  puts '| o |'
  puts '| o |'
  puts '| o |'
  puts '-----'
end
if a == 4 or b == 4
  puts '-----'
  puts '|o o|'
  puts '|   |'
  puts '|o o|'
  puts '-----'
end
if a == 5 or b == 5
  puts '-----'
  puts '|o o|'
  puts '| o |'
  puts '|o o|'
  puts '-----'
end
if a == 6 or b == 6
  puts '-----'
  puts '|o o|'
  puts '|o o|'
  puts '|o o|'
  puts '-----'
end

if a == 1 and b == 1
  puts '-----'
  puts '|   |'
  puts '| o |'
  puts '|   |'
  puts '-----'
end
if a == 2 and b == 2
  puts '-----'
  puts '|o  |'
  puts '|   |'
  puts '|  o|'
  puts '-----'
end
if a == 3 and b == 3
  puts '-----'
  puts '| o |'
  puts '| o |'
  puts '| o |'
  puts '-----'
end
if a == 4 and b == 4
  puts '-----'
  puts '|o o|'
  puts '|   |'
  puts '|o o|'
  puts '-----'
end
if a == 5 and b == 5
  puts '-----'
  puts '|o o|'
  puts '| o |'
  puts '|o o|'
  puts '-----'
end
if a == 6 and b == 6
  puts '-----'
  puts '|o o|'
  puts '|o o|'
  puts '|o o|'
  puts '-----'
end
sleep 0.1
end
sum = a + b
puts "Sum is #{sum}"
puts 'Roll The Dice: '
q = gets.chomp
if q == 'q'
  break
end
end
