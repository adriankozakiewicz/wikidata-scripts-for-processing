from bs4 import BeautifulSoup
import re
import argparse
import os


def listDumpSorted(filename):



    input_file = open(filename, "r", encoding="utf-8")

    soup = BeautifulSoup(input_file.read(), 'html.parser')
    
    rows = soup.find_all("tr")


    lex_cat_dict = dict()
    
    for row in rows:
        
        cols = row.find_all("td")
        # data formating
        # html element example: (all are same format)
        # <tr class="odd" role="row"><td><a href="../L21197">grusza</a></td><td><a href="../Q1084">noun</a></td></tr>
        value = cols[0].find("a").getText()
        link = "https://ordia.toolforge.org/language/" + cols[0].find("a")["href"]
        
        # csv format - value;link
        word_entry = "{};{}".format(value, link)
        
        # dict check if key exisits
        lex_type = cols[1].find("a").getText()
    
        if not lex_type in lex_cat_dict.keys():
            lex_cat_dict[lex_type] = []
    
        # list append
        lex_cat_dict[lex_type].append(word_entry)
  
  
  
  
    
    
    return lex_cat_dict

if __name__ == "__main__":
    
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('htmlElementFile', type=str, help="target file \nmanual at https://github.com/adriankozakiewicz/wikidata-scripts-for-processing/ordia/scripts/listDumpSorted/README.md")
    args = arg_parser.parse_args()
  

    #
    lex_cat_dict = listDumpSorted(args.htmlElementFile)


    try: os.mkdir("./listDumpSorted-output/")
    except: None

    for key in lex_cat_dict.keys():
        
    
        output_file = open("./listDumpSorted-output/list-"+key+".txt","w",encoding="utf-8")
    
    
        word_entry_list = lex_cat_dict[key]
        for word_entry in word_entry_list:
            output_file.write(word_entry+"\n")
        
        output_file.close()

    print("lists saved in: ./listDumpSorted-output/")
    print()
