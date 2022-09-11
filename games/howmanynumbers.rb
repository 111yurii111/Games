a = ''
b = 0
s = 0
c = 0
system('clear')
while true
  c = rand(10)
  a = a.to_s + c.to_s
  puts c
  sleep 1.5
  system('clear')
  puts 'Number: '
  b = gets.chomp
  if a.to_s != b
    break
  end
  s += 1
  system('clear')
end
puts "Corect number is #{a}"
puts 'Your score is ', s
