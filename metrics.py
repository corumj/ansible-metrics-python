import psycopg2  

job_id = 25 
query = '''
SELECT 
  play as "Job Template", 
  job_id, 
  host_name, 
  failed, 
  task, 
  stdout, 
  role from main_jobevent
WHERE job_id = {} and failed = true and play <> '';
'''.format(job_id)
try: 
  conn = psycopg2.connect("dbname='awx' user='postgres' host='localhost' password=''")
except Exception as err:
  print("Unable to connect to database")
  print(err)

try:
  cur = conn.cursor() 
  cur.execute(query)

  rows = cur.fetchall() 

  print("Show Job Event Rows")
  msg = {}
  for play, job, host, failed, task, stdout, role in rows:
    msg[play]
    print()
except Exception as err:
  print(err)

