n,k = gets.chomp.split(' ').map(&:to_i)
costs = gets.chomp.split(' ').map(&:to_i)
route = [0]

costs.each_with_index do |cost,index|
  now = costs[index]
  pre_cost_list = []
  1.upto(k) do |num|
    pre_cost_list << ((index - num < 0) ? 100001 : [costs[index-1],num])
  end
  if pre_cost_list.uniq[0] == 100001
    next
  end
  #p pre_cost_list
  p_cost_list = []
  pre_cost_list.each do |p_cost|
    if route[index-p_cost[1]].nil?
      next
    end
    p_cost_list << ((p_cost[0] < 100000) ? (costs[index-p_cost[1]]-now).abs + route[index-p_cost[1]] : 100000)
  end
  #p p_cost_list
  route << p_cost_list.min
end
#p route
puts route.pop
