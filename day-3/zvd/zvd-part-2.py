import re, collections


in_file = open('input.txt', 'r')
out_file = open('output-2.txt', 'w')

claims = {}
claim_ids = set([])
overlaping_claims = set([])

for claim in in_file:
	# Get claim's data.
    claim_text = re.search(r"^#(\d*) @ (\d*),(\d*): (\d*)x(\d*)$", claim)
    claim_id, from_left, from_top, width, height = map(int, claim_text.groups())
    
    claim_ids.add(claim_id)
	
	# Iterate over claim's coordinates.
    for y in range(from_top, from_top + height):
        for x in range(from_left, from_left + width):
            claim_coord = str(x) + '-' + str(y)
            
		    # Add coordinates to the claim dictionary.
            if claim_coord not in claims:
            	claims[claim_coord] = set([claim_id])
            else:
            	# Check if current occupant of fabric hasn't been added to the
            	# overlaping claims array, yet.
            	if len(claims[claim_coord]) == 1:
            		for existing_claim in claims[claim_coord]:
            			break
            		overlaping_claims.add(existing_claim)
            	
            	claims[claim_coord].add(claim_id)
            	if claim_id not in overlaping_claims:
	            	overlaping_claims.add(claim_id)
            

out_file.write(str(claim_ids - overlaping_claims))

in_file.close()
out_file.close()

