# AI-preneurs using python platform

Input: research paper pdf

Output: extracted segments of research work in JSON format

Necessary tasks: extract title, authors, abstract  

Web Application: Using django framework
->dir: mydjangoproject

Approach 1: Simple extraction method
->pypdf2.py

Approach 2: Machine Learning Approach

Refered papers:

https://ieeexplore.ieee.org/document/4118530

https://ieeexplore.ieee.org/document/6021634

https://ieeexplore.ieee.org/document/1204842

Selected approach:

Step 1: Collect PDF/XML training data

The training data will come as a set of PDFs paired to XML files that describe the metadata for the PDF, including the title, authors, abstracts as well as paragraphs, tables and formulas for the full text. For typeset PDFs, we will have access to JATS XML files that have good coverage of the metadata required (as indicated below), whilst XML accompanying author-submitted PDFs may include less information.

Filename : TrainingPDF.py

Step 2: Annotate PDF with tags from XML and coordinates

The XML files contain the correct tagging for the whole document. For training, we will need to know which PDF elements correspond to which XML tags. In the case of computer vision, we will also need the exact coordinates. Therefore as the first step we need to use the XML to annotate the PDF elements at individual character level.

Step 3: Prepare annotated PDF for computer vision training

After annotating individual PDF elements with their corresponding tag, we can prepare this data for computer vision training. For this stage, we are more interested in the areas than the individual elements: we plan to convert the annotated PDF elements to coloured blocks, each representing a separate tag. The output will be a PNG file. We could map them to unique colours that humans can distinguish.

Step 4: Train CNN model using transformed PDFs

The annotated PDF training data will be an input to CNN model. 

Filename : PDFtoXML.py



