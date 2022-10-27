import rpyc

# Create connection to server
connection = rpyc.connect("localhost", 18861)

# Run command: connect.root.squareroot(num) to retrieve the square root of num
num = 9
sqrt_num = connection.root.squareroot(num)

print(sqrt_num)
