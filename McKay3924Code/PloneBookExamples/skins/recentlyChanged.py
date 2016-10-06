##parameters=objects
now = DateTime()
difference = 5 # as in 5 days
result = []

for object in objects:
  diff = now - object.bobobase_modification_time()
  if diff < difference:
    dct = {"object":object,"diff":int(diff)}
    result.append(dct)

return result