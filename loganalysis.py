# !/usr/bin/env python

#import the postgres sql python module
import psycopg2



def get_sql_query(psql_query):
    #connect to an existing database
    database="news"
    conn = psycopg2.connect(dbname=database)

    #Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute(psql_query)
    results = cur.fetchall()
    conn.close()
    return results


    



request_one = "What are the most popular three articles of all time?"
request_two = "Who are the most popular article authors of all time?"
request_three = "On which days did more than 1% of requests lead to errors?"

query_1 ="SELECT articles.title, count(*) as views from articles join log on log.path like concat( '%', articles.slug, '%') group by articles.title order by views DESC limit 3;"
query_2 ="SELECT authors.name, count(*) as views from authors join articles on authors.id = articles.author join log on log.path like concat( '%', articles.slug, '%') group by authors.name order by views DESC;"
query_3 ="SELECT num_failed_statuses, total_num_statuses, round((num_failed_statuses*100/total_num_statuses), 3) as percentage_of_failed_statuses, ok.time FROM (SELECT count(status) as num_failed_statuses, date(time) AS time FROM LOG WHERE status='404 NOT FOUND' GROUP BY date(LOG.time)) ok JOIN (SELECT count(status) as total_num_statuses, date(time) AS time FROM LOG GROUP BY date(LOG.time)) total ON ok.time = total.time where round((num_failed_statuses*100/total_num_statuses), 3) > 1;"

#runs the python function with the sql query to get the query results
queryResult1 = get_sql_query(query_1)
queryResult2 = get_sql_query(query_2)
queryResult3 = get_sql_query(query_3)

def print_results1(query_results):
    for results in query_results:
        title = results[0]
        views = results[1]
        print ("Articles: " + str(title) + " - " + str(views) + " VIEWS")

def print_results2(query_results):
    for results in query_results:
        title = results[0]
        views = results[1]
        print ("Authors: " + str(title) + " - " + str(views) + " VIEWS")

def print_results3(query_results):
    for results in query_results:
        date = results[3]
        error = results[2]
        print (str(date) + " - " + str(error) + "% errors")









#run python module
if __name__ == '__main__':
    print(request_one)
    print_results1(queryResult1)
    print("\n")
    print(request_two)
    print_results2(queryResult2)
    print("\n")
    print(request_three)
    print_results3(queryResult3)
