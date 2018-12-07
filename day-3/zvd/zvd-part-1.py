import re


in_file = open('input-1.txt', 'r')
out_file = open('output-1.txt', 'w')

fabric = []
multi_claims = []

for claim in in_file:
    claim_text = re.search(r"^#(\d*) @ (\d*),(\d*): (\d*)x(\d*)$", claim)
    claim_id = int(claim_text.group(1))
    from_left = int(claim_text.group(2)) + 1
    from_top = int(claim_text.group(3)) + 1
    width = int(claim_text.group(4))
    height = int(claim_text.group(5))

    for y in range(from_top, from_top + height):
        for x in range(from_left, from_left + width):
            claim_coord = str(x) + '-' + str(y)
            for curr_coord in fabric:
                if curr_coord == claim_coord:
                    for multi_claim in multi_claims:
                        if multi_claim['left'] <= x <= multi_claim['left'] + multi_claim['width']:
                            break
                        elif x == multi_claim['left'] - 1:
                            multi_claim['left'] = x
                            multi_claim['width'] += 1
                        elif x == multi_claim['left'] + multi_claim['width'] + 1:
                            multi_claim['width'] += 1
                    else:
                        multi_claims.append({
                            'left': x,
                            'top': y,
                            'width': 1,
                            'height': 1
                        })
                    break
            else:
                fabric.append(claim_coord)

print(fabric)

in_file.close()
out_file.close()
