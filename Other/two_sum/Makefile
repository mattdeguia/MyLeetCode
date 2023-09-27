# The provided Makefile contains rules to build two programs: two_sum and vectors_tutorial.
# It also includes a rule to clean up the compiled files.


# This line specifies the default target for the Makefile.
# When you run make without specifying a target, it will execute the commands for all.
# In this case, it will build both two_sum and vectors_tutorial.
all: two_sum vectors_tutorial

# Here, we are making a target named "two_sum", which depends on the two_sum.cpp file.
# It means that if two_sum.cpp is modified or missing, the commands associated with this target will be executed.
# The "two_sum" at the end of the "g++" line is the name we give the executable file we want to make
# The "-Wall" is a flag that will enable all warnings when running the makefile
two_sum: two_sum.cpp
	g++ -std=c++11 two_sum.cpp -Wall -o two_sum

# This line defines a target called vectors_tutorial, which depends on the vectors_tutorial.cpp file.
# The "-std=c++11" is a flag used to enable all warnings for c++11 extensions
vectors_tutorial: vectors_tutorial.cpp
	g++ -std=c++11 vectors_tutorial.cpp -Wall -o vectors_tutorial

# This line defines a target called clean.
# This target is not dependent on any files.
# It is used to perform a cleanup operation.
clean:
	rm -f two_sum vectors_tutorial a.out *.o