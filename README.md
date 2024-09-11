# Take home project solution - Seth Rosen
I provided solutions to both the basic and advanced options listed in the project description. The notebook calls the functions and displays the two different outputs for easy viewing.

My solution makes use of pdfplumber for OCR since the provided pdf is very clean/doesn't have scanned pages otherwise I would have needed another package to handle those better. 

To actually find the largest number in the document I extract all numbers from a page using regex and then process them into the correct types before applying the unit conversion found in the language. This solution makes a few assumptions that don't pose issues for this particular problem but would need to be fixed in a final version (multiplies all floats by conversion unit when it should only be applied to monetary values, this poses no real issue for finding the largest number but would be an issue for other tasks like finding percentages). The regex I use also pulls out all numbers from the text regardless of formatting causing it to extract a government ID or code number ( 1.2.2.3 format ) which cannot be converted into a number type but again poses no issue to the performance of the overall system. 

To run the system you just need to change the pdf path in the notebook to the desired document or import the extraction function and pass a path to the desired document into the function and it will return the largest number it finds.




## The problem

[Here is a large pdf document](https://www.saffm.hq.af.mil/Portals/84/documents/FY25/FY25%20Air%20Force%20Working%20Capital%20Fund.pdf?ver=sHG_i4Lg0IGZBCHxgPY01g%3d%3d). We want to find the largest number in this document. The unit is not important (could be dollars, years, pounds, etc), we're just looking for the greatest numerical value in the document.

For a bonus challenge if you have time, take natural language guidance from the document into consideration. For example, where the document states that values are listed in millions, a value of 3.15 would be considered to be 3,150,000 instead of 3.15.
