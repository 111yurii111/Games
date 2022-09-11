r = rand(10)
g = 0
s = 0
while g.to_i != r
  print 'Guess the number: '
  g = gets.chomp
  if g.to_i < r
    puts 'Wrong! Too low'
    s += 1
  end
  if g.to_i > r
    puts 'Wrong! Too high'
    s += 1
  end
end
puts 'Correct!!!'
puts "Score #{s}"
