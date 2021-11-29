# website_connectivity

Uses the requests module to check the HTTP response codes from a CSV file of websites and adds them to a separate CSV file with the status.

### To-Do
* Clean up code - current code is using a combination of the CSV module and builtin readline/s and is a little sloppy.
* Documentation
* Add database website data & logging functionality in realization that CSV may not be the best solution in many cases.
* Explore ways of handling accidental blank lines in CSV files.  In the process of testing I had inadvertently added blank lines to the end of the CSV file.
