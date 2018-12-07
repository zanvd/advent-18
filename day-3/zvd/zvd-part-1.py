import re


in_file = open('input.txt', 'r')
out_file = open('output-1.txt', 'w')

claims = {}

for claim in in_file:
	# Get claim's data.
    claim_text = re.search(r"^#(\d*) @ (\d*),(\d*): (\d*)x(\d*)$", claim)
    claim_id, from_left, from_top, width, height = map(int, claim_text.groups())

	# Iterate over claim's coordinates.
    for y in range(from_top, from_top + height):
        for x in range(from_left, from_left + width):
            claim_coord = str(x) + '-' + str(y)
            
		    # Add coordinates to the claim dictionary.
            if claim_coord not in claims:
            	claims[claim_coord] = set([claim_id])
            else:
            	claims[claim_coord].add(claim_id)
            

overlaping = sum([len(claim) > 1 for claim in claims.values()])

out_file.write(str(overlaping))

in_file.close()
out_file.close()

