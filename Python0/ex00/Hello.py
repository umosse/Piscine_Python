ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Modify list
ft_list[1] = "World!"

# Modify tuple
country = "France!"
ft_tuple_list = list(ft_tuple)
ft_tuple_list[1] = country
ft_tuple = tuple(ft_tuple_list)

# Modify set
city = "Paris!"
ft_set.discard("tutu!")
ft_set.add(city)

# Modify dict
campus = "42Paris!"
ft_dict.update({"Hello" : campus})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)