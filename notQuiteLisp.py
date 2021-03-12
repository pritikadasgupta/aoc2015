

#part 1:

#function to read and parse the data
def parse_input(data):
	return(data.strip())


#function to go up and down floors, based on the data

def compute_floor(inputs):
	santa_pos = 0
	for x in inputs:
		if(x=="("):
			santa_pos+=1
		else:
			santa_pos-=1
	return(santa_pos)



if __name__ == '__main__':
    
    # get input data
    data_path = 'input.txt'
    inputs = parse_input(open(data_path, 'r').read())
    
    ### PART I
    solution = compute_floor(inputs)
    print('PART I: solution = {}'.format(solution))
    
    ### PART II
    solution = find_basement_position(inputs)
    print('PART II: solution = {}'.format(solution))