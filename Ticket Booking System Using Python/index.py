print("\n\nMovie Ticket Booking System\n")
restart = ('Y')

while restart != ('N','NO','n','no'):
	print("Booking a Movie Ticket")
	print("Option 1 : Booking Ticket and print out")
	print("Option 2 : Exit")
	option = int(input("\nEnter your option : "))

	if option == 1:
		people = int(input("\nEnter no. of Ticket you want : "))
		name_l = []
		time_l = []
		movie_l = []
		for p in range(people):
			name = str(input("\nName : "))
			name_l.append(name)
			movie  = str(input("\nMovie Name : "))
			movie_l.append(movie)
			time = str(input("\nTime  : "))
			time_l.append(time)
			

		restart = str(input("\nDid you forgot someone? y/n: "))
		if restart in ('y','YES','yes','Yes'):
			restart = ('Y')
		else :
			x = 0
			print("\nTotal Ticket : ",people)
			for p in range(1,people+1):
				print("Ticket : ",p)
				print("Name : ", name_l[x])
				print("Movie name is : ", movie_l[x])
				print("Time is : ", time_l[x])
				x += 1
	elif option == 2:
		exit()



	
