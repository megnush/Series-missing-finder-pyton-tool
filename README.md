# Series-missing-finder-pyton-tool
This Python GUI tool finds missing series and is the intellectual property of ©IndianGPT. Unauthorized reproduction, modification, or distribution of this tool, in whole or in part, is strictly prohibited without the written permission of ©IndianGPT. To use this tool, please contact ©IndianGPT at https://www.linkedin.com/in/megnush/.

The tool allows users to select an input file containing a series of numbers, sorts the numbers, and then finds the missing series between them. It exports the output in different formats, including summary, all missing series, missing series, and found series. Users can also click on the ©IndianGPT hyperlink to visit the owner's LinkedIn profile.

To use the tool, simply run the Python script and follow the prompts. The tool is built using the tkinter library for the GUI and filedialog for file selection. The tool also sets the size and icon of the GUI window for a better user experience.

Run the Missing Series Finder application. You will see a window with a "Process and Export" button.

Click the "Process and Export" button. A file dialog will open, asking you to select an input file. The input file should be a text file containing one integer per line. These integers represent the existing series available.

Example input file content:

Copy code
2150150000
2150150030
2150150033
2150150037
After selecting the input file, another file dialog will open, asking you to save the first output file. This output file will contain the start of the series, the range of missing numbers, and the count of missing numbers between the existing series.

Example output file content (first output file):

Start Series, From, To, Count
2150150000, 2150150001, 2150150029, 29
2150150030, 2150150031, 2150150032, 2
2150150033, 2150150034, 2150150036, 3
After saving the first output file, a third file dialog will open, asking you to save the second output file. This output file will contain the missing series with a count less than or equal to 12 and a remark "Not found in Whitelist".

Example output file content (second output file):


Missing Series, Remarks
2150150031, Not found in Whitelist
2150150032, Not found in Whitelist
The application also has a menu option to open a second window. Click on the "Help" menu and select "Open Second Window" to open the second window. You can customize this second window according to your requirements.

By following these steps, you can process an input file containing an existing series and generate two output files. The first output file will show the missing series ranges and their counts, while the second output file will list the missing series with a count less than or equal to 12 and a remark "Not found in Whitelist".
