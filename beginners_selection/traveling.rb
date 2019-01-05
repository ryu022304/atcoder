n = gets.chomp.to_i

routes = []
n.times do
  routes << gets.chomp.split(' ').map(&:to_i)
end
now = 0
times = 0
x = 0
y = 0
routes.each do |route|
  dest = (route[1]-x).abs + (route[2]-y).abs
  move = (route[0] - now).abs
  if dest > move || dest == 0 || (dest.odd? && move.even?) || (dest.even? && move.odd?)
    break
  else
    times += 1
    now += dest
    x = route[1]
    y = route[2]
  end
end

if times == n
  puts 'Yes'
else
  puts 'No'
end
