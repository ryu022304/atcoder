n = gets.chomp.to_i
costs = gets.chomp.split(' ').map(&:to_i)
route = [0]

costs.each_with_index do |cost,index|
  now = costs[index]
  pre_cost = index-1 < 0 ? 100001 : costs[index-1]
  pre2_cost = index-2 < 0 ? 100001 : costs[index-2]
  if pre_cost+pre2_cost > 200001
    next
  else
    p_cost = pre_cost < 100000 ? (costs[index-1]-now).abs + route[index-1] : 100000
    p2_cost = pre2_cost < 100000 ? (costs[index-2]-now).abs + route[index-2] : 100000
    if p_cost < p2_cost
      route << p_cost
    else
      route << p2_cost
    end
  end
end
puts route.pop
