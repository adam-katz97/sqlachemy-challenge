# sqlachemy-challenge
This exercise is meant to display my skills with sqlalchemy and being able to not only extract data from sqlite to jupyter notebook and to python. I was required to make queries that could find the temperatures between the end of the dataframe and 1 year before it, which i was able to do using adding group_by to the query and setting a limit. Then I had to display that data on a graph. Next i needed to determine the most active station in the sqlite data and then display the count of all stations in descending order. This was performed by putting unsing func.count(), grouping by the stations and using desc(). Finally I had to make a histogram using only the data from the most active station, which was simple once i finally figured out how to properly filter my query. translating everything to python was mostly a matter of making and defining api routes before just copy pasting my code into the appropriate definitions.