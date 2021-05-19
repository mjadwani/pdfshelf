import os
import PyPDF2
import sys
''' Who : Manoj K Jadwani                                                                '''
''' Simple pdf organiser                                                                 '''
''' Reads all pdf document info and generates a html page with links to access those pdf.'''
''' uses 3rd party PyPDF2 package                                                        '''
''' install PyPDF2 : pip install PyPDF2                                                  '''


class bookshelf:
    
    def __init__(self,folderpath=''):
        self.bookname = []      # Unique book name 
        self.booktitle = []     # Book tile read from PyPDF2 module 
        self.bookpath = []      # Filelocation of pdf doc
        self.folderpath = folderpath    #path where pdf docs are stored.
        return

    def bookindx(self):
        pass
        return

    def bookinfo(self):
        ''' 
        Grabs all files .pdf extension from a folderpath.
        stores in nfile list variable.
        function returns a list     
        '''
        
        nfile=[]        #stores filelocation of each .pdf files 
        flag=0          #flag to check if no .pdf files in a folderpath

        if len(self.folderpath) == 0 :
            cwd = os.getcwd()
        else:
            cwd = self.folderpath

        files = os.listdir(path= cwd)
        for each in files:
            if '.pdf' in each:
                nfile.append(cwd+os.sep+each)
                flag=1
            
        if flag==0 :
            print("No PDF Files Exist in this folder")
                
        #print(nfile)
        return nfile
    
    
    
    def set_pdfinfo(self,pdffiles):
        ''' Calls PdfFileRead function to create a pdf object     '''
        ''' access getDocumentInfo() function read pdf properties.'''
        
        for i,each in enumerate(pdffiles):
            with open(each,'rb') as pdfobj :
                pinfo=PyPDF2.PdfFileReader(pdfobj).getDocumentInfo()
                #print(pinfo)
                
                self.bookname.append('BOOK'+str(i))
                self.booktitle.append(pinfo.title)
                self.bookpath.append(each)
        return 

    def get_pdfinfo(self):
        ''' Can be used to display bookshelf class attributes '''
        print(self.bookname)
        print(self.booktitle)
        print(self.bookpath)
        return 

    def gen_html(self):
        
        ''' Function to generate html page '''
        
        fout = folderpath+os.sep+"pdflinks.html"
        with open(fout,mode='w',) as f:


            htmlstring='''
                <html>
                    <head>
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
                    <style>body{ margin:0 100; background:whitesmoke; }</style>
                    </head>
                    <style>
                        table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                        }
                        th, td {
                        padding: 5px;
                        text-align: left;
                        }
                        </style>
                    <body>
                        <h2>Links to Documents </h2>
                        <table style="width:50%">
                        <tr>
                            <th>BookNameIX</th>
                            <th>TITLE</th>
                        </tr> '''
            
        
        
            for i,r in enumerate(self.bookname):
                htmlstring += ''' <tr>  <td>''' + r + ''' </td> ''' 
                htmlstring += ''' <td> <a href=''' + self.bookpath[i] +  '''>''' + self.booktitle[i] 
                htmlstring += '''</a></td></tr> '''
                
        
        
            htmlstring += '''
                            </table>
                            </body>

                            </html> '''
            f.write(htmlstring)    
        return




if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        folderpath=''
    else:
        folderpath = sys.argv[1]
    print('Browse pdflinks.html file on path '+folderpath)
    b1 = bookshelf(folderpath)
    if len(b1.bookinfo()) != 0 :
        b1.set_pdfinfo(b1.bookinfo())
        b1.gen_html()
    
    