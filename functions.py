from SPARQLWrapper import SPARQLWrapper, JSON, POST

def new_sparqlwrapper(endpoint,user=None,password=None):
  sparql = SPARQLWrapper(endpoint)
  sparql.setReturnFormat(JSON)
  sparql.addCustomHttpHeader('Accept','application/sparql-results+json')
  sparql.addCustomHttpHeader('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
  sparql.setMethod(POST)
  if not user==None:
    sparql.setCredentials(user,password)
  return sparql

def execute_count_query(sparql, query):
  sparql.setQuery(query)
  result = sparql.query()
  count_dict = result.convert()
  count = None
  index = 0
  for result in count_dict["results"]["bindings"]: # Take the first entry of iterator; only one row
    if index>=1:
      raise Exception("Count queries are supposed to only have one row.")
    count = int(result['count']['value'])
    index += 1
  if count==None:
    raise Exception("No results returned from query:\n"+query)
  return count

def execute_query(sparql, query):
  sparql.setQuery(query)
  result = sparql.query().convert()
  return result["results"]["bindings"]
