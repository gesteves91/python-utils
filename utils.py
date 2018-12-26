def countElementsList(list):

  count = 0

  for element in list:
    count += 1
  
  return count

def calcultateSatisfaction(review_score):
  if review_score >= 95:
    return 1
  elif review_score < 95:
    return 0