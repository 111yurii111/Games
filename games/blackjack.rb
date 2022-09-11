system('clear')
puts 'Black Jack'
n = "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10 ", "10 ", "10 ", "10 ", "11 "
t = Time.now
f = t + 2
while Time.now < f
  system('clear')
  a = n.sample
  b = n.sample
  print a, b
  sleep 0.05
end
ab = a + b
s = a.to_i + b.to_i
puts ""
puts "Sum: #{s}"
print "One more card?(y or n): "
ask = gets.chomp

while ask == 'y'
  t = Time.now
  f = t + 2
  while Time.now < f
    system('clear')
    c = n.sample
    print ab, c
    sleep 0.05
  end
  ab = ab + c
  s = s + c.to_i
  puts ""
  puts "Sum: #{s}"
  if s > 21
    puts 'You lost!'
    break
  end
  print "One more card?(y or n):"
  ask = gets.chomp
end
if s <= 21
  x = 'a', 'a', 'b', 'b', 'c'
  z = x.sample
  if z == 'a'
    r1 = n.sample.to_i + n.sample.to_i
  end
  if z == 'b'
    r1 = n.sample.to_i + n.sample.to_i + n.sample.to_i
  end
  if z == 'c'
    r1 = n.sample.to_i + n.sample.to_i + n.sample.to_i + n.sample.to_i
  end
  puts "Robor 1: #{r1}"

  if z == 'a'
    r2 = n.sample.to_i + n.sample.to_i
  end
  if z == 'b'
    r2 = n.sample.to_i + n.sample.to_i + n.sample.to_i
  end
  if z == 'c'
    r2 = n.sample.to_i + n.sample.to_i + n.sample.to_i + n.sample.to_i
  end
  puts "Robor 2: #{r2}"
  if r1 or r2 <= 21

    if r1 > s
      puts 'You lost!'

    elsif r2 > s
      puts 'You lost!'
    else
      puts 'You won!'
    end
  end
end
